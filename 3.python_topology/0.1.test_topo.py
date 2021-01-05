# -*- coding: UTF-8 -*-
# Public package
import sys
# Private package
import ROOT
import headpy.hbes.hppp as hppp
import headpy.hbes.hstyle as hstyle
import headpy.hbes.hnew as hnew
import default as default

################################################################################
# Topology作图，单个branch
################################################################################


def plot(energy=0,
         tree='',
         branch='',
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
    docuts = ['pip_ep', 'pim_ep', 'pip_pid_pi', 'pim_pid_pi',
              'chisq',
              'a_pippim',
              'gamma1_heli', 'gamma2_heli', 'piz_m']
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
    topo_scale = default.topo_scale()
    scale = {}
    scale['10'] = topo_scale[energy]['001']
    scale['20'] = topo_scale[energy]['002']
    scale['30'] = topo_scale[energy]['003']
    scale['00'] = topo_scale[energy]['004']
    scale['01'] = topo_scale[energy]['004']
    scale['02'] = topo_scale[energy]['004']
    scale['08'] = topo_scale[energy]['004']
    allentry = 0
    for i in scale:
        allentry += entries[i] * scale[i]
    for i in scale:
        scale[i] = scale[i] * entries['real'] / allentry
    for i in scale:
        thist[i].Scale(scale[i])
        entries[i] = entries[i] * scale[i]
    # endregion
    # 2.set style
    hstyle.set_style()
    # 2.get canvas
    canvas = hstyle.get_canvas(1200, 900, 1, 1)
    # 2.set style
    xtitle, ytitle = selecters[branch].get_title()
    hstyle.set_axis(thist['real'], xtitle, ytitle)
    hstyle.set_height(thist['real'], 2.5)
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
    legendlist = hstyle.get_legend([[thist['real'], 'Data sample:%d' % (entries['real']), 'lp'],
                                    [thist['10'], 'BhaBha:%d' % (entries['10']), 'f'],
                                    [thist['20'], 'Digamma:%d' % (entries['20']), 'f'],
                                    [thist['30'], 'Dimiu:%d' % (entries['30']), 'f'],
                                    [thist['00'], 'CONEXC:%d' % (entries['00']), 'f'],
                                    [thist['01'], '#pi^{+}#pi^{-}:%d' % (entries['01']), 'f'],
                                    [thist['02'], '#pi^{+}#pi^{-}#pi^{0}#pi^{0}:%d' % (entries['02']), 'f'],
                                    [thist['08'], '#pi^{+}#pi^{-}#pi^{0}:%d' % (entries['08']), 'f']])
    drawlist.append(legendlist)
    # 3.draw
    thist['real'].Draw('E1')
    thist['stack'].Draw('sameHIST')
    thist['real'].Draw('E1same')
    for i in drawlist:
        i.Draw('same')
    if(stop != ''):
        input()
    return 0


energy_list = hppp.energy_list()
if(sys.argv[1] == '-1'):
    print('No option for -1')
elif(float(sys.argv[1]) in energy_list):
    plot(float(sys.argv[1]),
         tree='fit4c',
         branch=sys.argv[2],
         pictures=[],
         stop='yes')
else:
    print('Error energy point')
