# -*- coding: UTF-8 -*-
# Public package
# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp

error_list = ['luminosity', 'track_charge', 'track_pid', 'track_neutral', 'four_c', 'branch', 'isr', 'fit_back', 'fit_signal', 'fit_window']
output = ''
output += '{:^8}&'.format('Energy')
for i in error_list:
    output += '{:^12} &'.format(i)
output += '{:^12} &'.format('total')
output = output[:-1]
output += '\\\\\n'
for energy in hppp.energy_sort():
    error_total = 0.0
    output += '{:^8}&'.format('%1.4f' % (energy))
    for i in error_list:
        value = hfile.pkl_read('fdata_error/npwa_%s/%1.4f.pkl' % (i, energy))
        if(value < 0.0001):
            output += '{:^12} &'.format('$<$0.01')
        else:
            output += '{:^12} &'.format('%.2f' % (100 * value))
        error_total += value**2
    error_total = pow(error_total, 0.5)
    output += '{:^12} &'.format('%.2f' % (100 * error_total))
    output = output[:-1]
    output += '\\\\\n'
    hfile.pkl_dump('fdata_error/npwa_total/%1.4f.pkl' % (energy), error_total)
print(output)
