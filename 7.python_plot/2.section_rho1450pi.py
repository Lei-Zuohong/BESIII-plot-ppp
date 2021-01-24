# -*- coding: UTF-8 -*-
# Public package
# Private package
import headpy.hfile as hfile
import headpy.hbes.hnew as hnew
import headpy.hbes.hppp as hppp
import headpy.hbes.hconst as hconst

# 读取文件
massages = hnew.massage_read()
filename = {}
filename['eff'] = '%s.pkl' % (massages['efficiency'])
filename['factor'] = '%s.pkl' % (massages['factor'])
filename['event'] = '%s.pkl' % (massages['nevent'])
filename['sta_fraction_rho770pi'] = 'fdata_error/1.sta_fraction_rho770pi.pkl'
filename['sta_fraction_rho1450pi'] = 'fdata_error/1.sta_fraction_rho1450pi.pkl'
filename['sta_fraction_omega782pi'] = 'fdata_error/1.sta_fraction_omega782pi.pkl'
filename['sta_efficiency'] = 'fdata_error/1.sta_efficiency.pkl'
data = {}
for i in filename:
    data[i] = hfile.pkl_read(filename[i])
# 计算文件
energy_list = hppp.energy_list()
energy_sort = hppp.energy_sort()
output = {}
for energy in energy_sort:
    # 录入数据
    output[energy] = {}
    output[energy]['Energy'] = energy
    output[energy]['Nsignal'] = data['event'][energy]['nevent']
    output[energy]['eNsignal'] = data['event'][energy]['enevent']
    output[energy]['Lumin'] = energy_list[energy][2]
    output[energy]['Effciency'] = data['eff'][energy]
    output[energy]['isr'] = data['factor'][energy]['isr']
    output[energy]['vpf'] = data['factor'][energy]['vpf']
    output[energy]['Branch'] = 0.98823
    output[energy]['Fraction'] = hfile.pkl_read('../ppp_pwa/output_nominal/%1.4f.pkl' % (energy)).fraction['rho1450pi']['rho1450pi']
    # 录入误差
    error = {}
    error['efficiency'] = data['sta_efficiency'][energy]
    error['nsignal'] = data['event'][energy]['enevent'] / data['event'][energy]['nevent']
    error['fraction'] = data['sta_fraction_rho1450pi'][energy]
    error_total = 0
    for i in error:
        error_total += error[i]**2
    error_total = pow(error_total, 0.5)
    # 计算数据
    section = output[energy]['Nsignal'] / output[energy]['Lumin'] / output[energy]['Effciency'] / output[energy]['isr'] / output[energy]['vpf'] / output[energy]['Branch'] * output[energy]['Fraction']
    if(1 == 1):
        if(energy < 2.2 and energy != 2.125):
            section *= 0.6
    esection = section * error_total

    output[energy]['Section'] = section
    output[energy]['eSection'] = esection
    output[energy]['error_efficiency'] = error['efficiency']
    output[energy]['error_nsignal'] = error['nsignal']
    output[energy]['error_fraction'] = error['fraction']
    output[energy]['error_total'] = error_total

for energy in energy_sort:
    print('|{:^10}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('%1.4f' % (energy),
                                                                      '%.4f' % (output[energy]['Section']),
                                                                      '%.4f' % (output[energy]['eSection']),
                                                                      '%.4f' % (output[energy]['error_efficiency']),
                                                                      '%.4f' % (output[energy]['error_nsignal']),
                                                                      '%.4f' % (output[energy]['error_fraction']),
                                                                      '%.4f' % (output[energy]['error_total'])))
fileoutput = '%s_rho1450pi.pkl' % (massages['section'])
hfile.pkl_dump(fileoutput, output)
