# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp

################################################################################
# 读取fraction
# 读取fractions
# 将fraction的中心值放入    pwa_fraction_nominal
# 将fraction的误差放入      pwa_fraction_mean_error
################################################################################

processes = ['rho770pi', 'rho1450pi', 'omega782pi']
multi_fraction = {}
for energy in hppp.energy_sort():
    nominal = hfile.pkl_read('../ppp_pwa/output_nominal/%1.4f.pkl' % (energy)).fraction
    multi = hfile.pkl_read('../ppp_pwa/fdata_error/sta_fractions/%1.4f.pkl' % (energy))
    multi_fraction[energy] = {}
    for process in processes:
        multi_list = []
        for i in range(len(multi)):
            multi_list.append(multi[i][process][process])
        multi_fraction[energy][process] = {}
        multi_fraction[energy][process]['nominal'] = nominal[process][process]
        multi_fraction[energy][process]['multi_mean'] = numpy.mean(multi_list)
        multi_fraction[energy][process]['multi_error'] = numpy.std(multi_list) / numpy.mean(multi_list)
        hfile.pkl_dump('fdata_error/pwa_fraction_nominal/%s/%1.4f.pkl' % (process, energy), nominal[process][process])
        hfile.pkl_dump('fdata_error/pwa_fraction_mean_error/%s/%1.4f.pkl' % (process, energy), {'mean': numpy.mean(multi_list),
                                                                                                'error': numpy.std(multi_list) / numpy.mean(multi_list)})
    print(energy)
    for process in processes:
        print('{:<12}: nominal: {:<10} multi_mean: {:<10} multi_error: {:<10}'.format(process,
                                                                                      '%.4f' % (multi_fraction[energy][process]['nominal']),
                                                                                      '%.4f' % (multi_fraction[energy][process]['multi_mean']),
                                                                                      '%.4f' % (multi_fraction[energy][process]['multi_error'])))
