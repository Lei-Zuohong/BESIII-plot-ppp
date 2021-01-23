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


energy = 2.1250
tree = 'fit4c'
pictures = ['opicture/analysis/dalitz_phsp.pdf',
            'opicture/analysis/dalitz_phsp.jpg']
stop = 'yes'


# 读取数据
massages = hnew.massage_read()
trees = hnew.trees_read(energy=energy,
                        tree=tree,
                        read=['pppmpz'])
selecters = hppp.selecters()
# 初始化数据
alldata = hnew.ALLDATA(trees=trees,
                       selecters=selecters,
                       massages=massages)
namef = {}
nameh = {}
docuts = hppp.docuts()
selecters['piz_m'].set_width(0.015)
alldata.trees['pppmpz']['dalitz_pm'] = alldata.trees['pppmpz']['pipm_m']**2
alldata.trees['pppmpz']['dalitz_pz'] = alldata.trees['pppmpz']['pipz_m']**2
namef['r'], nameh['r'] = alldata.hist(data='pppmpz',
                                      branchs=['dalitz_pm', 'dalitz_pz'],
                                      docuts=docuts,
                                      name='pppmpz')
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
xtitle1, ytitle1 = alldata.selecters['dalitz_pm'].get_title()
xtitle2, ytitle2 = alldata.selecters['dalitz_pz'].get_title()
hstyle.set_axis(thist['r'], xtitle1, xtitle2)
################################
# 2. get legend & arrow
################################
drawlist = []
################################
# 3. draw
################################
thist['r'].Draw('COLZ')
for i in drawlist:
    i.Draw('same')
for i in pictures:
    canvas.Print(i)
    print('Done print to:')
    print('%s' % (i))
if(stop != ''):
    input()
