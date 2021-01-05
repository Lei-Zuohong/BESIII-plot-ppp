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


def weight(energy):
    # region 初始化数据
    massages = hnew.massage_read()
    trees = hnew.trees_read(energy=energy,
                            tree='fit4c',
                            read=['real', 'pppmpz'])
    selecters = hppp.selecters()
    docuts = hppp.docuts()
    # endregion
    # region 筛选数据
    tree_real = trees['real']
    tree_pppmpz = trees['pppmpz']
    selecters['piz_m'].set_width(0.015)
    tree_r = hnew.tree_cut(tree_real,
                           selecters,
                           branchs=docuts)
    tree_m = hnew.tree_cut(tree_pppmpz,
                           selecters,
                           branchs=docuts)
    selecters['piz_m'].shift(-0.045)
    tree_b1 = hnew.tree_cut(tree_real,
                            selecters,
                            branchs=docuts)
    selecters['piz_m'].shift(0.045 + 0.045)
    tree_b2 = hnew.tree_cut(tree_real,
                            selecters,
                            branchs=docuts)
    # endregion
    weighter = hnew.WEIGHTER()
    weighter.set_branch(['pipm_m', 'pipz_m', 'piz_a'])
    weighter.set_data_m(data=[tree_m['pipm_m'], tree_m['pipz_m'], tree_m['piz_a']])
    weighter.set_data_r(data=[tree_r['pipm_m'], tree_r['pipz_m'], tree_r['piz_a']])
    weighter.set_data_b(data1=[tree_b1['pipm_m'], tree_b1['pipz_m'], tree_b1['piz_a']],
                        data2=[tree_b2['pipm_m'], tree_b2['pipz_m'], tree_b2['piz_a']])
    weighter.set_bins()
    weighter.set_matrix()
    weighter.set_weight()
    weighter.clean()
    return weighter


name_weight = 'pipm_m_pipz_m_piz_a'
massage = hnew.massage_read()
weight_folder = 'fdata/weight-%s' % (massage['version'])
os.system('mkdir %s/%s' % (weight_folder, name_weight))
energy_sort = hppp.energy_sort()
for energy in energy_sort:
    # if(energy != 2.1250): continue
    output = weight(energy)
    hfile.pkl_dump('%s/%s/%1.4f.pkl' % (weight_folder, name_weight, energy), output)
