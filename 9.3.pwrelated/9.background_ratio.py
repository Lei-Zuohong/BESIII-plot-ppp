# -*- coding: UTF-8 -*-
# Public package
import os
import sys
# Private package
import ROOT
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp
import headpy.hbes.hnew as hnew

########################################
# 输出3pi粒子的数目绘制表格
########################################


def get_number(energy=0):
    # 初始化数据
    massages = hnew.massage_read()
    trees = hnew.trees_read(energy=energy,
                            tree='fit4c',
                            read=['real', 'pppmpz'])
    selecters = hppp.selecters()
    docuts = ['pip_ep', 'pim_ep', 'pip_pid_pi', 'pim_pid_pi',
              # 'vertex',
              'chisq',
              'a_pippim',
              'gamma1_heli', 'gamma2_heli',
              'piz_m']
    # 筛选数据
    tree = trees['real']
    selecters['piz_m'].set_width(0.015)
    tree_signal = hnew.tree_cut(tree,
                                selecters,
                                branchs=docuts)
    selecters['piz_m'].shift(-0.045)
    tree_left = hnew.tree_cut(tree,
                              selecters,
                              branchs=docuts)
    selecters['piz_m'].shift(+0.045 + 0.045)
    tree_right = hnew.tree_cut(tree,
                               selecters,
                               branchs=docuts)
    num_signal = len(tree_signal['piz_m'])
    num_sideband = (len(tree_left['piz_m']) + len(tree_right['piz_m'])) / 2
    return [num_signal, num_sideband]


num = {}
energy_list = hppp.energy_list()
energy_order = energy_list.keys()
energy_order.sort()
for energy in energy_order:
    num[energy] = get_number(energy=energy)
for energy in energy_order:
    output = ''
    output += '{:^10} &'.format('%.4f' % (energy))
    output += '{:^10} &'.format(num[energy][0])
    output += '{:^10} '.format(num[energy][1])
    output += '\\\\'
    print(output)
