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
filename['efficiency'] = '%s.pkl' % (massages['efficiency'])
#filename['factor'] = '%s.pkl' % (massages['factor_rho770pi'])
filename['factor'] = 'fdata/1.factor_rho770pi-00-03.pkl'
filename['event'] = 'fdata/3.nevent_rho770pi.pkl'
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

    output[energy]['Efficiency'] = data['efficiency'][energy]

    output[energy]['isr'] = data['factor'][energy]['isr']
    output[energy]['vpf'] = data['factor'][energy]['vpf']

    output[energy]['Branch'] = 0.98823
    # 录入误差
    error = {}
    error['pwa'] = hfile.pkl_read('fdata_error/pwa_total/rho770pi/%1.4f.pkl' % (energy))
    error['npwa'] = hfile.pkl_read('fdata_error/npwa_total/%1.4f.pkl' % (energy))
    error['nsignal'] = data['event'][energy]['enevent'] / data['event'][energy]['nevent']
    error_total = 0.0
    error_sta = 0.0
    error_sys = 0.0
    for i in error:
        error_total += error[i]**2
        if(i in ['nsignal']):
            error_sta += error[i]**2
        else:
            error_sys += error[i]**2
    error_total = pow(error_total, 0.5)
    error_sta = pow(error_sta, 0.5)
    error_sys = pow(error_sys, 0.5)
    # 计算数据
    section = output[energy]['Nsignal'] /output[energy]['Lumin'] / output[energy]['Efficiency'] / output[energy]['isr'] / output[energy]['vpf'] / output[energy]['Branch']
    esection = section * error_total

    output[energy]['Section'] = section
    output[energy]['eSection'] = esection
    output[energy]['error_pwa'] = error['pwa']
    output[energy]['error_npwa'] = error['npwa']
    output[energy]['error_sta'] = error_sta
    output[energy]['error_sys'] = error_sys
    output[energy]['error_total'] = error_total

for energy in energy_sort:
    print('|{:^10}|{:^12}|{:^12}|{:^12}|{:^12}|{:^12}|'.format('%1.4f' % (energy),
                                                               '%.4f' % (output[energy]['Section']),
                                                               '%.4f' % (output[energy]['eSection']),
                                                               '%.4f' % (output[energy]['error_pwa']),
                                                               '%.4f' % (output[energy]['error_npwa']),
                                                               '%.4f' % (output[energy]['error_total'])))
fileoutput = '%s.pkl' % (massages['section_rho770pi'])
hfile.pkl_dump(fileoutput, output)
