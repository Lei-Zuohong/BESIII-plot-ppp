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

option2 = 'chisq'
option4 = 'picture/2_topology/4.topo_chisq_fom'


def plot(energy=0,
         tree='fit4c',
         branch=option2,
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
        if(i != option2):
            new_docuts.append(i)
    docuts = new_docuts
    for i in range(3):
        index = i + 1
        alldata.selecters['flag3'].values = [index]
        namef['%d0' % (index)], nameh['%d0' % (index)] = alldata.hist(data='back_back',
                                                                      branchs=[branch],
                                                                      docuts=docuts + ['flag3'],
                                                                      name='hist%d0' % (index))
    # endregion
    # region 数据 Inclusive部分
    alldata.selecters['flag3'].values = [4]
    alldata.selecters['flag2'].values = [0]
    namef['00'], nameh['00'] = alldata.hist(data='back_back',
                                            branchs=[branch],
                                            docuts=docuts + ['flag3', 'flag2'],
                                            name='hist00')
    alldata.selecters['flag2'].values = [1]
    namef['01'], nameh['01'] = alldata.hist(data='back_back',
                                            branchs=[branch],
                                            docuts=docuts + ['flag3', 'flag2'],
                                            name='hist01')
    alldata.selecters['flag2'].values = [2]
    namef['02'], nameh['02'] = alldata.hist(data='back_back',
                                            branchs=[branch],
                                            docuts=docuts + ['flag3', 'flag2'],
                                            name='hist02')
    alldata.selecters['flag2'].values = [8]
    namef['08'], nameh['08'] = alldata.hist(data='back_back',
                                            branchs=[branch],
                                            docuts=docuts + ['flag3', 'flag2'],
                                            name='hist08')
    namef['real'], nameh['real'] = alldata.hist(data='real',
                                                branchs=[branch],
                                                docuts=docuts,
                                                name='histreal')
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
    default.scale(energy, thist, entries)
    # endregion
    inter = selecters[branch].inter
    left = selecters[branch].left_show
    right = selecters[branch].right_show
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
    xtitle, ytitle = selecters[branch].get_title()
    hstyle.set_axis(error_ratio,
                    xtitle,
                    'S/#sqrt{S+B}')
    error_ratio.SetMarkerStyle(7)
    error_ratio.GetXaxis().SetRangeUser(0, 100)
    error_ratio.GetYaxis().SetRangeUser(0, 2 * hr)
    # 2.get legend & arrow
    drawlist = []
    drawlist = hstyle.add_arrow(drawlist,
                                50, 0,
                                50, 2 * hr,
                                2, 3)
    # 3.draw
    error_ratio.Draw('AP')
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
