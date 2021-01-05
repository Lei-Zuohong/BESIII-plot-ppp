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

########################################
# 输出3pi粒子的四动量信息作为分波使用
folder_file_root = '../ppp_pwa/root_truth'
folder_file_pkl = '../ppp_pwa/pkl_truth'

tree = 'truth'
read = 'pppmpz'
docuts = []
obranchs = {}
obranchs['px1'] = 'pip_px'
obranchs['py1'] = 'pip_py'
obranchs['pz1'] = 'pip_pz'
obranchs['E1'] = 'pip_pe'
obranchs['px2'] = 'pim_px'
obranchs['py2'] = 'pim_py'
obranchs['pz2'] = 'pim_pz'
obranchs['E2'] = 'pim_pe'
obranchs['px3'] = 'piz_px'
obranchs['py3'] = 'piz_py'
obranchs['pz3'] = 'piz_pz'
obranchs['E3'] = 'piz_pe'
########################################


def dump(energy):
    # region 初始化数据
    massages = hnew.massage_read()
    trees = hnew.trees_read(energy=energy,
                            tree=tree,
                            read=[read])
    selecters = hppp.selecters()
    # endregion
    # region 筛选数据
    tree_m = trees[read]
    selecters['piz_m'].set_width(0.015)
    tree_m = hnew.tree_cut(tree_m,
                           selecters,
                           branchs=docuts)
    # endregion
    # region 裁剪数据
    otree_m = {}

    samples = {}
    samples['signal'] = len(tree_m['piz_m'])

    for obranch in obranchs:
        otree_m[obranch] = tree_m[obranchs[obranch]]
    # endregion
    # region 输出数据
    hnew.treend(name_tfile='%s/%1.4f_mc.root' % (folder_file_root, energy),
                name_ttree='data',
                branchs=otree_m)
    hfile.pkl_dump('%s/%1.4f_entries.pkl' % (folder_file_root, energy), samples)

    hfile.pkl_dump('%s/%1.4f_mc.pkl' % (folder_file_pkl, energy), otree_m)
    hfile.pkl_dump('%s/%1.4f_entries.pkl' % (folder_file_pkl, energy), samples)


energy_sort = hppp.energy_sort()
for energy in energy_sort:
    dump(energy)
