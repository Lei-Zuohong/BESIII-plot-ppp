# -*- coding: UTF-8 -*-
# Public package

# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp

data = hfile.pkl_read('fdata_error/1.sta_efficiency.pkl')
output = ''
for energy in hppp.energy_sort():
    output += '%1.4f & %.2f \\\\\n' % (energy, data[energy] * 100)
print(output)

data1 = hfile.pkl_read('fdata_error/1.sta_fraction_rho770pi.pkl')
data2 = hfile.pkl_read('fdata_error/1.sta_fraction_rho1450pi.pkl')
data3 = hfile.pkl_read('fdata_error/1.sta_fraction_omega782pi.pkl')
output = ''
for energy in hppp.energy_sort():
    output += '%1.4f & %.2f & %.2f & %.2f \\\\\n' % (energy,
                                                     data1[energy] * 100,
                                                     data2[energy] * 100,
                                                     data3[energy] * 100)
print(output)
