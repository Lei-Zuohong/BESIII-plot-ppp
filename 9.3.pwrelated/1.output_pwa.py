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
folder_file_root = '../ppp_pwa/root_pwa'
folder_file_pkl = '../ppp_pwa/pkl_pwa'
########################################


def dump(energy):
    # region 初始化数据
    massages = hnew.massage_read()
    trees = hnew.trees_read(energy=energy,
                            tree='fit4c',
                            read=['real', 'pppmpz'])
    selecters = hppp.selecters()
    docuts = ['pip_ep', 'pim_ep', 'pip_pid_pi', 'pim_pid_pi',
              'chisq',
              'a_pippim',
              'gamma1_heli', 'gamma2_heli',
              'piz_m']
    # endregion
    # region 筛选数据
    tree_r = trees['real']
    tree_m = trees['pppmpz']
    selecters['piz_m'].set_width(0.015)
    tree_r = hnew.tree_cut(tree_r,
                           selecters,
                           branchs=docuts)
    tree_m = hnew.tree_cut(tree_m,
                           selecters,
                           branchs=docuts)
    selecters['piz_m'].shift(-0.045)
    tree_b1 = hnew.tree_cut(tree_r,
                            selecters,
                            branchs=docuts)
    selecters['piz_m'].shift(0.045 + 0.045)
    tree_b2 = hnew.tree_cut(tree_r,
                            selecters,
                            branchs=docuts)
    # endregion
    # region 裁剪数据
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
    otree_r = {}
    otree_m = {}

    samples = {}
    samples['signal'] = len(tree_r['piz_m'])
    samples['sideband'] = len(tree_b1['piz_m']) + len(tree_b2['piz_m'])
    samples['mc'] = len(tree_m['piz_m'])
    samples['signal'] = samples['signal'] - samples['signal'] % 4
    samples['sideband'] = samples['sideband'] - samples['sideband'] % 4
    samples['mc'] = samples['mc'] - samples['mc'] % 4

    for obranch in obranchs:
        a = tree_r[obranchs[obranch]][0:samples['signal']]
        b = numpy.hstack((tree_b1[obranchs[obranch]],
                          tree_b2[obranchs[obranch]]))
        b = b[0:samples['sideband']]
        otree_r[obranch] = numpy.hstack((a, b))
        otree_m[obranch] = tree_m[obranchs[obranch][0:samples['mc']]]
    # endregion
    # region 输出数据
    hnew.treend(name_tfile='%s/%1.4f_data.root' % (folder_file_root, energy),
                name_ttree='data',
                branchs=otree_r)
    hnew.treend(name_tfile='%s/%1.4f_mc.root' % (folder_file_root, energy),
                name_ttree='data',
                branchs=otree_m)
    hfile.pkl_dump('%s/%1.4f_entries.pkl' % (folder_file_root, energy), samples)

    hfile.pkl_dump('%s/%1.4f_data.pkl' % (folder_file_pkl, energy), otree_r)
    hfile.pkl_dump('%s/%1.4f_mc.pkl' % (folder_file_pkl, energy), otree_m)
    hfile.pkl_dump('%s/%1.4f_entries.pkl' % (folder_file_pkl, energy), samples)


energy_sort = hppp.energy_sort()
for energy in energy_sort:
    dump(energy)
