# -*- coding: UTF-8 -*-
# Public package
import os
import sys
# Private package
import ROOT
import headpy.hbes.hppp as hppp
import headpy.hbes.hstyle as hstyle
import headpy.hbes.hnew as hnew
import default as default

option2 = 'pip_ep'
option3 = 'pim_ep'
option4 = 'picture/2_topology/1.topo_ep_fom'


def plot(energy=0,
         tree='fit4c',
         branch1=option2,
         branch2=option3,
         pictures=[],
         stop=''):
    # region 读取数据
    massages = hnew.massage_read()
    trees = hnew.trees_read(energy,
                            tree=tree,
                            read=['real', 'back_back'])
    selecters = hppp.selecters()
    selecters['flag2'] = hnew.SELECTER_value(values=[])
    selecters['flag3'] = hnew.SELECTER_value(values=[])
    # endregion
    # region 初始化数据类
    alldata = hnew.ALLDATA(trees=trees,
                           selecters=selecters,
                           massages=massages)
    namef = {}
    nameh = {}
    # endregion
    # region 数据 background部分
    docuts = hppp.docuts()
    new_docuts = []
    for i in docuts:
        if(i != option2 and i != option3):
            new_docuts.append(i)
    docuts = new_docuts
    for i in range(3):
        index = i + 1
        alldata.selecters['flag3'].values = [index]
        namef['%d01' % (index)], nameh['%d01' % (index)] = alldata.hist(data='back_back',
                                                                        branchs=[branch1],
                                                                        docuts=docuts + ['flag3'],
                                                                        name='hist%d01' % (index))
        namef['%d02' % (index)], nameh['%d02' % (index)] = alldata.hist(data='back_back',
                                                                        branchs=[branch2],
                                                                        docuts=docuts + ['flag3'],
                                                                        name='hist%d02' % (index))
    # endregion
    # region 数据 Inclusive部分
    alldata.selecters['flag3'].values = [4]
    alldata.selecters['flag2'].values = [0]
    namef['001'], nameh['001'] = alldata.hist(data='back_back',
                                              branchs=[branch1],
                                              docuts=docuts + ['flag3', 'flag2'],
                                              name='hist001')
    namef['002'], nameh['002'] = alldata.hist(data='back_back',
                                              branchs=[branch2],
                                              docuts=docuts + ['flag3', 'flag2'],
                                              name='hist002')
    alldata.selecters['flag2'].values = [1]
    namef['011'], nameh['011'] = alldata.hist(data='back_back',
                                              branchs=[branch1],
                                              docuts=docuts + ['flag3', 'flag2'],
                                              name='hist011')
    namef['012'], nameh['012'] = alldata.hist(data='back_back',
                                              branchs=[branch2],
                                              docuts=docuts + ['flag3', 'flag2'],
                                              name='hist012')
    alldata.selecters['flag2'].values = [2]
    namef['021'], nameh['021'] = alldata.hist(data='back_back',
                                              branchs=[branch1],
                                              docuts=docuts + ['flag3', 'flag2'],
                                              name='hist021')
    namef['022'], nameh['022'] = alldata.hist(data='back_back',
                                              branchs=[branch2],
                                              docuts=docuts + ['flag3', 'flag2'],
                                              name='hist022')
    alldata.selecters['flag2'].values = [8]
    namef['081'], nameh['081'] = alldata.hist(data='back_back',
                                              branchs=[branch1],
                                              docuts=docuts + ['flag3', 'flag2'],
                                              name='hist081')
    namef['082'], nameh['082'] = alldata.hist(data='back_back',
                                              branchs=[branch2],
                                              docuts=docuts + ['flag3', 'flag2'],
                                              name='hist082')
    namef['real1'], nameh['real1'] = alldata.hist(data='real',
                                                  branchs=[branch1],
                                                  docuts=docuts,
                                                  name='histreal1')
    namef['real2'], nameh['real2'] = alldata.hist(data='real',
                                                  branchs=[branch2],
                                                  docuts=docuts,
                                                  name='histreal2')
    # endregion
    # region 数据 读取数据对象
    tfile = {}
    thist = {}
    entries = {}
    for i in namef:
        tfile[i] = ROOT.TFile(namef[i])
        thist[i] = tfile[i].Get(nameh[i])
        entries[i] = thist[i].GetEntries()
    # endregion
    # region Scale因子
    default.add_hist(thist, entries, '10', '101', '102')
    default.add_hist(thist, entries, '20', '201', '202')
    default.add_hist(thist, entries, '30', '301', '302')
    default.add_hist(thist, entries, '00', '001', '002')
    default.add_hist(thist, entries, '01', '011', '012')
    default.add_hist(thist, entries, '02', '021', '022')
    default.add_hist(thist, entries, '08', '081', '082')
    default.add_hist(thist, entries, 'real', 'real1', 'real2')
    default.scale(energy, thist, entries)
    # endregion
    inter = selecters[branch1].inter
    left = selecters[branch1].left_show
    right = selecters[branch1].right_show
    # 统计序列
    x, fom, efom = default.fom([thist['08']],
                               [thist['00'], thist['01'], thist['02'], thist['10'], thist['20'], thist['30']],
                               inter,
                               left,
                               right)
    hr = fom[inter - 1]
    # 2.get canvas
    canvas = hstyle.get_canvas(1200, 900)
    canvas.SetLeftMargin(0.1697324)
    canvas.SetBottomMargin(0.1697324)
    # 2.get tgraph
    error_ratio = ROOT.TGraphErrors(inter)
    for i in range(inter):
        error_ratio.SetPoint(i, x[i], fom[i])
        error_ratio.SetPointError(i, 0, efom[i])
    # 2.set style
    hstyle.set_style()
    xtitle, ytitle = selecters[branch1].get_title()
    hstyle.set_axis(error_ratio,
                    xtitle,
                    'S/#sqrt{S+B}')
    error_ratio.SetMarkerStyle(7)
    error_ratio.GetXaxis().SetRangeUser(0, 1.2)
    error_ratio.GetYaxis().SetRangeUser(0, 2 * hr)
    # 2.get legend & arrow
    drawlist = []
    drawlist = hstyle.add_arrow(drawlist,
                                0.9, 0,
                                0.9, 2 * hr,
                                2, 3)
    # 3.draw
    error_ratio.Draw('AP')
    # error_ratio.Draw('A')
    for i in drawlist:
        i.Draw('same')
    for i in pictures:
        canvas.Print(i)
        print('Done print to:')
        print('%s' % (i))
    if(stop != ''):
        input()
    return 0


energy_list = hppp.energy_list()
if(float(sys.argv[1]) in energy_list):
    os.system('mkdir %s' % (option4))
    plot(float(sys.argv[1]),
         pictures=['%s/%d.pdf' % (option4, 10000 * float(sys.argv[1])),
                   '%s/%d.jpg' % (option4, 10000 * float(sys.argv[1]))],
         stop='yes')
else:
    print('Error energy point')
