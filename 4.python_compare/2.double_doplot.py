# -*- coding: UTF-8 -*-
# Public package
import os
import sys
# Private package
import ROOT
import headpy.hbes.hppp as hppp
import headpy.hbes.hnew as hnew
import headpy.hbes.hstyle as hstyle


def plot(energy=0,
         tree='',
         branch1='',
         branch2='',
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
    alldata1 = hnew.ALLDATA(trees=trees,
                            selecters=selecters,
                            massages=massages)
    alldata2 = hnew.ALLDATA(trees=trees,
                            selecters=selecters,
                            massages=massages)
    alldata.get_weight(data='pppmpz',
                       energy=energy,
                       name_weight='pipm_m_pipz_m',
                       name_branch='pipmpipz',
                       dimension=2)
    namef = {}
    nameh = {}
    docuts = ['chisq', 'chisq_1g', 'chisq_4g',
              'a_pippim', 'pip_ep', 'pim_ep',
              'gamma1_heli', 'gamma2_heli', 'piz_m']
    selecters['piz_m'].set_width(0.015)
    namef['r1'], nameh['r1'] = alldata.hist(data='real',
                                            branchs=[branch1],
                                            docuts=docuts,
                                            name='real')
    namef['m1'], nameh['m1'] = alldata.hist(data='pppmpz',
                                            branchs=[branch1],
                                            docuts=docuts,
                                            doweight=['pipmpipz'],
                                            name='pppmpz')
    namef['r2'], nameh['r2'] = alldata.hist(data='real',
                                            branchs=[branch2],
                                            docuts=docuts,
                                            name='real')
    namef['m2'], nameh['m2'] = alldata.hist(data='pppmpz',
                                            branchs=[branch2],
                                            docuts=docuts,
                                            doweight=['pipmpipz'],
                                            name='pppmpz')
    alldata1.selecters['piz_m'].shift(-0.045)
    namef['b11'], nameh['b11'] = alldata1.hist(data='real',
                                               branchs=[branch1],
                                               docuts=docuts,
                                               name='back1')
    namef['b12'], nameh['b12'] = alldata1.hist(data='real',
                                               branchs=[branch2],
                                               docuts=docuts,
                                               name='back1')
    alldata2.selecters['piz_m'].shift(0.045 + 0.045)
    namef['b21'], nameh['b21'] = alldata2.hist(data='real',
                                               branchs=[branch1],
                                               docuts=docuts,
                                               name='back2')
    namef['b22'], nameh['b22'] = alldata2.hist(data='real',
                                               branchs=[branch2],
                                               docuts=docuts,
                                               name='back2')
    # 读取数据对象
    tfile = {}
    thist = {}
    entries = {}
    for i in namef:
        tfile[i] = ROOT.TFile(namef[i])
        thist[i] = tfile[i].Get(nameh[i])
        entries[i] = thist[i].GetEntries()
    # 整合数据
    thist['r1'].Add(thist['r2'])
    thist['m1'].Add(thist['m2'])
    thist['b11'].Add(thist['b12'])
    thist['b21'].Add(thist['b22'])
    thist['r'] = thist['r1']
    thist['m'] = thist['m1']
    thist['b1'] = thist['b11']
    thist['b2'] = thist['b21']
    # 1.calculation
    er = thist['r'].GetEntries()
    em = thist['m'].GetEntries()
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
    xtitle, ytitle = alldata.selecters[branch1].get_title()
    hstyle.set_axis(thist['r'], xtitle, ytitle)
    hstyle.set_height(thist['r'], 1.5)
    hstyle.set_marker(thist['r'])
    hstyle.set_background(thist['m'])
    hstyle.set_background(thist['b1'], Fillcolor=2, Linecolor=2)
    hstyle.set_background(thist['b2'], Fillcolor=3, Linecolor=3)
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
option4 = sys.argv[4]  # branch名
energy_list = hppp.energy_list()

if(sys.argv[1] == '-1'):
    os.system('mkdir picture/1_compare/%s' % (option2))
    for i in energy_list:
        plot(energy=i,
             tree='fit4c',
             branch1=option3,
             branch2=option4,
             pictures=['picture/1_compare/%s/%05d.pdf' % (option2, 10000 * i),
                       'picture/1_compare/%s/%05d.jpg' % (option2, 10000 * i)],
             stop='')
elif(float(option1) in energy_list):
    plot(energy=float(option1),
         tree='fit4c',
         branch1=option3,
         branch2=option4,
         pictures=[],
         stop='yes')
else:
    print('Error energy point')
