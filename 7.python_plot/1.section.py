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
data = {}
for i in filename:
    data[i] = hfile.pkl_read(filename[i])
# 计算文件
energy_list = hppp.energy_list()
energy_sort = hppp.energy_sort()
nsignal = {}
for i in energy_sort:
    nsignal[i] = {}
    nsignal[i]['Energy'] = i
    nsignal[i]['Nsignal'] = data['event'][i]['nevent']
    nsignal[i]['eNsignal'] = data['event'][i]['enevent']
    nsignal[i]['Effect'] = data['eff'][i]
    nsignal[i]['eEffect'] = 0
    nsignal[i]['Lumin'] = energy_list[i][2]
    nsignal[i]['isr'] = data['factor'][i]['isr']
    nsignal[i]['vpf'] = data['factor'][i]['vpf']

    a = nsignal[i]['Nsignal']
    ea = nsignal[i]['eNsignal']
    b = nsignal[i]['Effect']
    c = nsignal[i]['Lumin']
    isr = nsignal[i]['isr']
    v = nsignal[i]['vpf']
    br2 = hconst.pdg()['br_pi0']

    nsignal[i]['Section'] = a / b / c / isr / v / br2
    nsignal[i]['eSection'] = ea / b / c / isr / v / br2
for i in energy_sort:
    print('|{:^20}|{:^20}|{:^20}|'.format('%1.4f' % (i),
                                          '%.4f' % (nsignal[i]['Section']),
                                          '%.4f' % (nsignal[i]['eSection'])))
fileoutput = '%s.pkl' % (massages['section'])
hfile.pkl_dump(fileoutput, nsignal)
