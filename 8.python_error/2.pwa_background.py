# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp
import headpy.hbes.hnew as hnew
import headpy.hscreen.hprint as hprint


def efficiency(energy, weight_fit4c, weight_truth):
    # 读取数据
    massages = hnew.massage_read()
    trees_fit4c = hnew.trees_read(energy=energy,
                                  tree='fit4c',
                                  read=['pppmpz'])
    trees_truth = hnew.trees_read(energy=energy,
                                  tree='truth',
                                  read=['pppmpz'])
    selecters = hppp.selecters()
    # 初始化数据
    selecters['piz_m'].set_width(0.045)
    alldata_fit4c = hnew.ALLDATA(trees=trees_fit4c,
                                 selecters=selecters,
                                 massages=massages)
    alldata_truth = hnew.ALLDATA(trees=trees_truth,
                                 selecters=selecters,
                                 massages=massages)
    myweight_fit4c = weight_fit4c
    myweight_truth = weight_truth
    alldata_fit4c.trees['pppmpz']['pwa_weight'] = numpy.array(myweight_fit4c)
    alldata_truth.trees['pppmpz']['pwa_weight'] = numpy.array(myweight_truth)
    docuts = hppp.docuts()
    alldata_fit4c.selecters['t_is_isr'] = hnew.SELECTER_value(values=[1])
    entry_fit4c_isr = alldata_fit4c.statis(data='pppmpz',
                                           docuts=docuts + ['t_is_isr'],
                                           doweight=['pwa_weight'])
    alldata_fit4c.selecters['t_is_isr'] = hnew.SELECTER_value(values=[0])
    entry_fit4c_nsr = alldata_fit4c.statis(data='pppmpz',
                                           docuts=docuts + ['t_is_isr'],
                                           doweight=['pwa_weight'])
    alldata_truth.selecters['is_isr'] = hnew.SELECTER_value(values=[1])
    entry_truth_isr = alldata_truth.statis(data='pppmpz',
                                           docuts=['is_isr'],
                                           doweight=['pwa_weight'])
    entry_conexc_isr = alldata_truth.statis(data='pppmpz',
                                            docuts=['is_isr'],
                                            doweight=[])
    alldata_truth.selecters['is_isr'] = hnew.SELECTER_value(values=[0])
    entry_truth_nsr = alldata_truth.statis(data='pppmpz',
                                           docuts=['is_isr'],
                                           doweight=['pwa_weight'])
    entry_conexc_nsr = alldata_truth.statis(data='pppmpz',
                                            docuts=['is_isr'],
                                            doweight=[])
    # 输出数据
    hprint.ppoint('     ISR Generated', '%d' % (entry_conexc_isr))
    hprint.ppoint('None ISR Generated', '%d' % (entry_conexc_nsr))
    hprint.ppoint('     ISR Weighted truth', '%d' % (entry_truth_isr))
    hprint.ppoint('None ISR Weighted truth', '%d' % (entry_truth_nsr))
    hprint.ppoint('     ISR Weighted fit4c', '%d' % (entry_fit4c_isr))
    hprint.ppoint('None ISR Weighted fit4c', '%d' % (entry_fit4c_nsr))
    efficiency_isr = entry_fit4c_isr / entry_truth_isr
    efficiency_nsr = entry_fit4c_nsr / entry_truth_nsr
    hprint.ppoint('     ISR Efficiency', '%.5f' % (efficiency_isr))
    hprint.ppoint('None ISR Efficiency', '%.5f' % (efficiency_nsr))
    efficiency = (efficiency_isr * entry_conexc_isr + efficiency_nsr * entry_conexc_nsr) / (entry_conexc_isr + entry_conexc_nsr)
    efficiency_fake = (entry_fit4c_isr + entry_fit4c_nsr) / (entry_truth_isr + entry_truth_nsr)
    hprint.ppoint('     Total Efficiency', '%.5f' % (efficiency))
    hprint.ppoint('Fake Total Efficiency', '%.5f' % (efficiency_fake))
    hprint.pstar()
    detail = {}
    detail['0.ISR Generated'] = '%d' % (entry_conexc_isr)
    detail['0.None-ISR Generated'] = '%d' % (entry_conexc_nsr)
    detail['1.ISR Events efficiency'] = '{:.2%}'.format(efficiency_isr)
    detail['1.None-ISR Events efficiency'] = '{:.2%}'.format(efficiency_nsr)
    detail['2.Fix ISR efficiency'] = '{:.2%}'.format(efficiency)
    detail['2.No-Fix ISR efficiency'] = '{:.2%}'.format(efficiency_fake)
    return efficiency, detail


def std(energy):
    section_total = []
    section_rho770pi = []
    section_rho1450pi = []
    section_omega782pi = []
    fraction = hfile.pkl_read('../ppp_pwa/fdata_error/sys_background_fractions/%1.4f.pkl' % (energy))
    weight_fit4c = hfile.pkl_read('../ppp_pwa/fdata_error/sys_background_weight_fit4c/%1.4f.pkl' % (energy))
    weight_truth = hfile.pkl_read('../ppp_pwa/fdata_error/sys_background_weight_truth/%1.4f.pkl' % (energy))
    eff_out, detail_out = efficiency(energy, weight_fit4c, weight_truth)
    section_total = 1 / eff_out
    section_rho770pi = fraction['rho770pi']['rho770pi'] / eff_out
    section_rho1450pi = fraction['rho1450pi']['rho1450pi'] / eff_out
    section_omega782pi = fraction['omega782pi']['omega782pi'] / eff_out
    return section_total, section_rho770pi, section_rho1450pi, section_omega782pi


# 读取信息
massage = hnew.massage_read()
energy_sort = hppp.energy_sort()
origin_total = hfile.pkl_read('%s.pkl' % (massage['efficiency']))
origin_rho770pi = hfile.pkl_read('%s.pkl' % (massage['efficiency_rho770pi']))
origin_rho1450pi = hfile.pkl_read('%s.pkl' % (massage['efficiency_rho1450pi']))
origin_omega782pi = hfile.pkl_read('%s.pkl' % (massage['efficiency_omega782pi']))
# 进行统计
for energy in energy_sort:
    #if(energy != 2.0000): continue
    section_total, section_rho770pi, section_rho1450pi, section_omega782pi = std(energy)
    error_total = abs((1 / origin_total[energy]) - section_total) / (1 / origin_total[energy])
    error_rho770pi = abs((1 / origin_rho770pi[energy]) - section_rho770pi) / (1 / origin_rho770pi[energy])
    error_rho1450pi = abs((1 / origin_rho1450pi[energy]) - section_rho1450pi) / (1 / origin_rho1450pi[energy])
    error_omega782pi = abs((1 / origin_omega782pi[energy]) - section_omega782pi) / (1 / origin_omega782pi[energy])

    hfile.pkl_dump('fdata_error/pwa_background/total/%1.4f.pkl' % (energy), error_total)
    hfile.pkl_dump('fdata_error/pwa_background/rho770pi/%1.4f.pkl' % (energy), error_rho770pi)
    hfile.pkl_dump('fdata_error/pwa_background/rho1450pi/%1.4f.pkl' % (energy), error_rho1450pi)
    hfile.pkl_dump('fdata_error/pwa_background/omega782pi/%1.4f.pkl' % (energy), error_omega782pi)
