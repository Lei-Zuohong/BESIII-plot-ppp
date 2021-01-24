# -*- coding: UTF-8 -*-
# Public package

# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp
import headpy.hbes.hnew as hnew
import headpy.hbes.hconst as hconst

massages = hnew.massage_read()

data = hfile.pkl_read('fdata/4.section-00-03.pkl')
data1 = hfile.pkl_read('fdata/4.section-00-03_rho770pi.pkl')
data2 = hfile.pkl_read('fdata/4.section-00-03_rho1450pi.pkl')


energy_list = hppp.energy_list()
energy_sort = hppp.energy_sort()
#
output = ''
output += '{:^20}'.format('$\\sqrt{S}$ (GeV)')
output += '&{:^20}'.format('Events')
output += '&{:^20}'.format('$L(pb^{-1})$')
output += '&{:^20}'.format('$\\varepsilon$')
output += '&{:^20}'.format('ISR factor')
output += '&{:^20}'.format('VP factor')
output += '&{:^50}'.format('Cross section(pb)')
output += '{:^20}'.format('\\\\\\hline')
print(output)
for energy in energy_sort:
    output = ''
    output += '{:^10}'.format('%1.4f' % (energy))
    output += '&{:^20}'.format('%.2f$\\pm$%.2f' % (data[energy]['Nsignal'], data[energy]['eNsignal']))
    output += '&{:^20}'.format('%s' % (hconst.energy_list()[energy][3]))
    output += '&{:^10}'.format('%.2f' % (data[energy]['Efficiency']))
    output += '&{:^10}'.format('%.2f' % (data[energy]['isr']))
    output += '&{:^10}'.format('%.2f' % (data[energy]['vpf']))
    output += '&{:^30}'.format('%.2f$\\pm$%.2f(%.1f\\%%)' % (data[energy]['Section'],
                                                             data[energy]['eSection'],
                                                             100 * data[energy]['eSection'] / data[energy]['Section']))
    output += '&{:^30}'.format('%.2f$\\pm$%.2f(%.1f\\%%)' % (data1[energy]['Section'],
                                                             data1[energy]['eSection'],
                                                             100 * data1[energy]['eSection'] / data1[energy]['Section']))
    output += '&{:^30}'.format('%.2f$\\pm$%.2f(%.1f\\%%)' % (data2[energy]['Section'],
                                                             data2[energy]['eSection'],
                                                             100 * data2[energy]['eSection'] / data2[energy]['Section']))
    
    output += '\\\\'
    print(output)
