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
option4 = 'picture/2_topology/1.topo_ep'


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
    docuts = default.docuts()
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
    # 2.set style
    hstyle.set_style()
    # 2.get canvas
    canvas = hstyle.get_canvas(1200, 900, 1, 1)
    # 2.set style
    xtitle, ytitle = selecters[branch1].get_title()
    hstyle.set_axis(thist['real'], xtitle, ytitle)
    hstyle.set_height(thist['real'], 2)
    hstyle.set_marker(thist['real'])
    hstyle.set_background(thist['10'], Fillcolor=5, Linecolor=5, Fillstyle=3244)
    hstyle.set_background(thist['20'], Fillcolor=6, Linecolor=6, Fillstyle=3244)
    hstyle.set_background(thist['30'], Fillcolor=7, Linecolor=7, Fillstyle=3244)
    hstyle.set_background(thist['00'], Fillcolor=2, Linecolor=2, Fillstyle=3244)
    hstyle.set_background(thist['01'], Fillcolor=3, Linecolor=3, Fillstyle=3244)
    hstyle.set_background(thist['02'], Fillcolor=4, Linecolor=4, Fillstyle=3244)
    hstyle.set_background(thist['08'], Fillcolor=1, Linecolor=1, Fillstyle=3244)
    thist['stack'] = ROOT.THStack('stack', '123')
    thist['stack'].Add(thist['10'])
    thist['stack'].Add(thist['20'])
    thist['stack'].Add(thist['30'])
    thist['stack'].Add(thist['00'])
    thist['stack'].Add(thist['01'])
    thist['stack'].Add(thist['02'])
    thist['stack'].Add(thist['08'])
    drawlist = []
    legendlist = hstyle.get_legend([[thist['real'], 'Energy: %1.4f GeV' % (energy), ''],
                                    [thist['real'], 'Data sample:%d' % (entries['real']), 'lp'],
                                    [thist['10'], 'BhaBha:%d' % (entries['10']), 'f'],
                                    [thist['20'], 'Digamma:%d' % (entries['20']), 'f'],
                                    [thist['30'], 'Dimiu:%d' % (entries['30']), 'f'],
                                    [thist['00'], 'CONEXC:%d' % (entries['00']), 'f'],
                                    [thist['01'], '#pi^{+}#pi^{-}:%d' % (entries['01']), 'f'],
                                    [thist['02'], '#pi^{+}#pi^{-}#pi^{0}#pi^{0}:%d' % (entries['02']), 'f'],
                                    [thist['08'], '#pi^{+}#pi^{-}#pi^{0}:%d' % (entries['08']), 'f']],
                                   l=0.63, r=0.9, d=0.6, u=0.93)
    drawlist.append(legendlist)
    drawlist = hstyle.add_arrow(drawlist,
                                0.9, 0,
                                0.9, 0.5 * thist['real'].GetMaximum(),
                                Linecolor=2, Linewidth=3)
    # 3.draw
    thist['real'].Draw('E1')
    thist['stack'].Draw('sameHIST')
    thist['real'].Draw('E1same')
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
