# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp
import headpy.hbes.hnew as hnew
import headpy.hscreen.hprint as hprint

################################################################################
# 通过 Correlated parameter 计算效率分布
################################################################################


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
    fractions = hfile.pkl_read('../ppp_pwa/fdata_error/sta_fractions/%1.4f.pkl' % (energy))
    for i in range(100):
        weight_fit4c = hfile.pkl_read('../ppp_pwa/fdata_error/sta_weight_fit4c/%1.4f_%03d.pkl' % (energy, i))
        weight_truth = hfile.pkl_read('../ppp_pwa/fdata_error/sta_weight_truth/%1.4f_%03d.pkl' % (energy, i))
        eff_out, detail_out = efficiency(energy, weight_fit4c, weight_truth)
        section_total.append(1 / eff_out)
    error = numpy.std(section_total) / numpy.mean(section_total)
    return error


# 读取信息
massage = hnew.massage_read()
energy_sort = hppp.energy_sort()
# 进行统计
for energy in energy_sort:
    # if(energy != 2.0000): continue
    error_total = std(energy)
    hfile.pkl_dump('fdata_error/pwa_efficiency/%1.4f.pkl' % (energy), error_total)
