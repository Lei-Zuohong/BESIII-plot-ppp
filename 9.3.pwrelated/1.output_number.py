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


def dump(energy):
    # region 初始化数据
    massages = hnew.massage_read()
    trees = hnew.trees_read(energy=energy,
                            tree='fit4c',
                            read=['real', 'pppmpz'])
    selecters = hppp.selecters()
    docuts = hppp.docuts()
    # endregion
    # region 筛选数据
    tree_source_r = trees['real']
    tree_source_m = trees['pppmpz']
    selecters['piz_m'].set_width(0.015)
    tree_r = hnew.tree_cut(tree_source_r,
                           selecters,
                           branchs=docuts)
    tree_m = hnew.tree_cut(tree_source_m,
                           selecters,
                           branchs=docuts)
    selecters['piz_m'].shift(-0.045)
    tree_b1 = hnew.tree_cut(tree_source_r,
                            selecters,
                            branchs=docuts)
    selecters['piz_m'].shift(0.045 + 0.045)
    tree_b2 = hnew.tree_cut(tree_source_r,
                            selecters,
                            branchs=docuts)
    # endregion
    # region 裁剪数据
    output = {}
    output['signal'] = len(tree_r['piz_m'])
    output['sideband'] = len(tree_b1['piz_m']) + len(tree_b2['piz_m'])
    output['sideband'] = int(output['sideband'] / 2)
    return output


energy_sort = hppp.energy_sort()
output = ''
for energy in energy_sort:
    number = dump(energy)
    output += '{:^10} & {:^10} & {:^10} & {:^10} \\\\\n'.format('%.4f' % (energy),
                                                                '%d' % (number['signal']),
                                                                '%d' % (number['sideband']),
                                                                '%.2f' % (100 * float(number['sideband']) / float(number['signal'])))
print(output)
