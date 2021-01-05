# -*- coding: UTF-8 -*-
# Public package
import os
import sys
# Private package
import ROOT
import headpy.hbes.hppp as hppp
import headpy.hbes.hnew as hnew
import headpy.hbes.hstyle as hstyle

################################################################################
# 绘制dalitz图，数据使用data sample
# 第一个参数为能量点
################################################################################


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
                            read=['back_back'])
    selecters = hppp.selecters()
    selecters['flag2'] = hnew.SELECTER_value(values=[])
    selecters['flag3'] = hnew.SELECTER_value(values=[])
    docuts = ['pip_ep', 'pim_ep', 'pip_pid_pi', 'pim_pid_pi',
              # 'vertex',
              'chisq',
              'a_pippim',
              'gamma1_heli', 'gamma2_heli',
              'piz_m',
              'flag2','flag3']
    # 初始化数据
    alldata = hnew.ALLDATA(trees=trees,
                           selecters=selecters,
                           massages=massages)
    namef = {}
    nameh = {}
    selecters['piz_m'].set_width(0.015)
    alldata.selecters['flag3'].values = [4]
    alldata.selecters['flag2'].values = [8]
    namef['m'], nameh['m'] = alldata.hist(data='back_back',
                                          branchs=[branch1, branch2],
                                          docuts=docuts,
                                          name='back_back')
    # 读取数据对象
    tfile = {}
    thist = {}
    entries = {}
    for i in namef:
        tfile[i] = ROOT.TFile(namef[i])
        thist[i] = tfile[i].Get(nameh[i])
        entries[i] = thist[i].GetEntries()
    # 2.set style
    hstyle.set_style()
    # 2.get canvas
    canvas = hstyle.get_canvas(1200, 900, 2, 1)
    # 2.set style
    xtitle1, ytitle1 = alldata.selecters[branch1].get_title()
    xtitle2, ytitle2 = alldata.selecters[branch2].get_title()
    hstyle.set_axis(thist['m'], xtitle1, xtitle2)
    ################################
    # 2. get legend & arrow
    ################################
    drawlist = []
    ################################
    # 3. draw
    ################################
    thist['m'].Draw('COLZ')
    for i in drawlist:
        i.Draw('same')
    for i in pictures:
        canvas.Print(i)
        print('Done print to:')
        print('%s' % (i))
    if(stop != ''):
        input()


option1 = sys.argv[1]  # 判断单个能量点测试，或者批量输出文件
option2 = 'dalitz_pm'  # branch名
option3 = 'dalitz_pz'  # branch名
energy_list = hppp.energy_list()

if(sys.argv[1] == '-1'):
    print('no option for -1')
elif(float(option1) in energy_list):
    plot(energy=float(option1),
         tree='fit4c',
         branch1=option2,
         branch2=option3,
         pictures=['opicture/analysis/dalitz_%05d_mc.jpg' % (10000 * float(option1)),
                   'opicture/analysis/dalitz_%05d_mc.pdf' % (10000 * float(option1))],
         stop='yes')
else:
    print('Error energy point')
