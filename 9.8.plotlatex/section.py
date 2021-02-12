# -*- coding: UTF-8 -*-
# Public package

# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp
import headpy.hbes.hnew as hnew
import headpy.hbes.hconst as hconst

massages = hnew.massage_read()

data1 = hfile.pkl_read('fdata/4.section-00-04.pkl')
data2 = hfile.pkl_read('fdata/4.section_rho770pi-00-04.pkl')
data3 = hfile.pkl_read('fdata/4.section_rho1450pi-00-04.pkl')

energy_list = hppp.energy_list()
energy_sort = hppp.energy_sort()

output1 = ''
output2 = ''
output3 = ''
for energy in energy_sort:
    output1 += '{:^8}'.format('%1.4f' % (energy))
    output2 += '{:^8}'.format('%1.4f' % (energy))
    output3 += '{:^8}'.format('%1.4f' % (energy))

    output1 += '&{:^8}'.format('%.2f' % (data1[energy]['Nsignal']))
    output1 += '&$\pm$'
    output1 += '&{:^8}'.format('%.2f' % (data1[energy]['eNsignal']))
    output2 += '&{:^8}'.format('%.2f' % (data2[energy]['Nsignal']))
    output2 += '&$\pm$'
    output2 += '&{:^8}'.format('%.2f' % (data2[energy]['eNsignal']))
    output3 += '&{:^8}'.format('%.2f' % (data3[energy]['Nsignal']))
    output3 += '&$\pm$'
    output3 += '&{:^8}'.format('%.2f' % (data3[energy]['eNsignal']))

    string_lumin = '&{:^16}'.format('%s' % (hconst.energy_list()[energy][3]))
    output1 += string_lumin.replace(r'$\pm$',r'&$\pm$&')
    output2 += string_lumin.replace(r'$\pm$',r'&$\pm$&')
    output3 += string_lumin.replace(r'$\pm$',r'&$\pm$&')

    delta1 = data1[energy]['isr'] * data1[energy]['vpf']
    delta2 = data2[energy]['isr'] * data2[energy]['vpf']
    delta3 = data3[energy]['isr'] * data3[energy]['vpf']

    output1 += '&{:^7}'.format('%.2f' % (data1[energy]['Efficiency']))
    output2 += '&{:^7}'.format('%.2f' % (data2[energy]['Efficiency'] * pow(delta1 / delta2, 0.5)))
    output3 += '&{:^7}'.format('%.2f' % (data3[energy]['Efficiency'] * pow(delta1 / delta3, 0.5)))

    output1 += '&{:^7}'.format('%.2f' % (delta1))
    output2 += '&{:^7}'.format('%.2f' % (delta2 / pow(delta1 / delta2, 0.5)))
    output3 += '&{:^7}'.format('%.2f' % (delta3 / pow(delta1 / delta3, 0.5)))

    output1 += '&{:^8}'.format('%.2f' % (data1[energy]['Section']))
    output1 += '&$\pm$'
    output1 += '&{:^8}'.format('%.2f' % (data1[energy]['Section'] * data1[energy]['error_sta']))
    output1 += '&$\pm$'
    output1 += '&{:^8}'.format('%.2f' % (data1[energy]['Section'] * data1[energy]['error_sys']))

    output2 += '&{:^8}'.format('%.2f' % (data2[energy]['Section']))
    output2 += '&$\pm$'
    output2 += '&{:^8}'.format('%.2f' % (data2[energy]['Section'] * data2[energy]['error_sta']))
    output2 += '&$\pm$'
    output2 += '&{:^8}'.format('%.2f' % (data2[energy]['Section'] * data2[energy]['error_sys']))

    output3 += '&{:^8}'.format('%.2f' % (data3[energy]['Section']))
    output3 += '&$\pm$'
    output3 += '&{:^8}'.format('%.2f' % (data3[energy]['Section'] * data3[energy]['error_sta']))
    output3 += '&$\pm$'
    output3 += '&{:^8}'.format('%.2f' % (data3[energy]['Section'] * data3[energy]['error_sys']))

    output1 += '\\\\\n'
    output2 += '\\\\\n'
    output3 += '\\\\\n'
print(output1)
print(output2)
print(output3)
