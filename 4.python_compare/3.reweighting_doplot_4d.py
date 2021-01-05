# -*- coding: UTF-8 -*-
# Public package
import os
import sys
import numpy
# Private package
import ROOT
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp
import headpy.hbes.hnew as hnew
import headpy.hbes.hstyle as hstyle


def plot(energy=0,
         tree='',
         branch='',
         pictures=[],
         stop=''):
    # 读取数据
    massages = hnew.massage_read()
    trees = hnew.trees_read(energy=energy,
                            tree=tree,
                            read=['real', 'pppmpz'])
    selecters = hppp.selecters()
    # 初始化数据
    alldata = hnew.ALLDATA(trees=trees,
                           selecters=selecters,
                           massages=massages)
    docuts = hppp.docuts()
    namef = {}
    nameh = {}
    alldata.selecters['piz_m'].set_width(0.015)
    alldata.get_weighter(data='pppmpz',
                         energy=energy,
                         name_weight='pipm_m_pipz_m_piz_a_pip_a',
                         name_branch='pwa_weight')
    namef['r'], nameh['r'] = alldata.hist(data='real',
                                          branchs=[branch],
                                          docuts=docuts,
                                          name='doplot_real')
    namef['m'], nameh['m'] = alldata.hist(data='pppmpz',
                                          branchs=[branch],
                                          docuts=docuts,
                                          doweight=['pwa_weight'],
                                          name='doplot_pppmpz')
    alldata.selecters['piz_m'].shift(-0.045)
    namef['b1'], nameh['b1'] = alldata.hist(data='real',
                                            branchs=[branch],
                                            docuts=docuts,
                                            name='doplot_back1')
    alldata.selecters['piz_m'].shift(0.045 + 0.045)
    namef['b2'], nameh['b2'] = alldata.hist(data='real',
                                            branchs=[branch],
                                            docuts=docuts,
                                            name='doplot_back2')
    alldata.selecters['piz_m'].shift(-0.045)
    # 读取数据对象
    tfile = {}
    thist = {}
    entries = {}
    for i in namef:
        tfile[i] = ROOT.TFile(namef[i])
        thist[i] = tfile[i].Get(nameh[i])
        entries[i] = thist[i].GetEntries()
    # 1.calculation
    er = thist['r'].GetEntries()
    em = alldata.statis(data='pppmpz',
                        docuts=docuts,
                        doweight=['pwa_weight'],)
    eb1 = thist['b1'].GetEntries()
    eb2 = thist['b2'].GetEntries()
    thist['m'].Scale((er - 0.5 * eb1 - 0.5 * eb2) / em)
    thist['b1'].Scale(0.5)
    thist['b2'].Scale(0.5)
    # 2.set style
    hstyle.set_style()
    # 2.get canvas
    canvas = hstyle.get_canvas(1200, 900, 1, 1)
    # 2.set style
    xtitle, ytitle = alldata.selecters[branch].get_title()
    hstyle.set_axis(thist['r'], xtitle, ytitle)
    hstyle.set_height(thist['r'], 1.5)
    hstyle.set_marker(thist['r'])
    hstyle.set_background(thist['m'])
    hstyle.set_background(thist['b1'], Fillcolor=2, Linecolor=2)
    hstyle.set_background(thist['b2'], Fillcolor=3, Linecolor=3)
    if(branch in ['pipm_m', 'pipz_m', 'pimz_m']):
        hstyle.set_xrange(thist['r'])
    thist['stack'] = ROOT.THStack('stack', '')
    thist['stack'].Add(thist['b1'])
    thist['stack'].Add(thist['b2'])
    thist['stack'].Add(thist['m'])
    ################################
    # 2. get legend & arrow
    ################################
    drawlist = []
    legendlist = hstyle.get_legend([[thist['r'], 'Energy: %1.4f GeV' % (energy), ''],
                                    [thist['r'], 'Real data', 'lp'],
                                    [thist['m'], 'Signal MC', 'f'],
                                    [thist['b1'], 'Background (Left)', 'f'],
                                    [thist['b2'], 'Background (Right)', 'f']])
    drawlist.append(legendlist)
    ################################
    # 3. draw
    ################################
    thist['r'].Draw('E1')
    thist['stack'].Draw('sameHIST')
    for i in drawlist:
        i.Draw('same')
    for i in pictures:
        canvas.Print(i)
        print('Done print to:')
        print('%s' % (i))
    if(stop != ''):
        input()


option1 = sys.argv[1]  # 判断单个能量点测试，或者批量输出文件
option2 = sys.argv[2]  # 文件夹名
option3 = sys.argv[3]  # branch名
energy_list = hppp.energy_list()

if(sys.argv[1] == '-1'):
    os.system('mkdir picture/1_compare/%s' % (option2))
    for i in energy_list:
        plot(energy=i,
             tree='fit4c',
             branch=option3,
             pictures=['picture/1_compare/%s/%05d.pdf' % (option2, 10000 * i),
                       'picture/1_compare/%s/%05d.jpg' % (option2, 10000 * i)],
             stop='')
elif(float(option1) in energy_list):
    plot(energy=float(option1),
         tree='fit4c',
         branch=option3,
         pictures=[],
         stop='yes')
else:
    print('Error energy point')
