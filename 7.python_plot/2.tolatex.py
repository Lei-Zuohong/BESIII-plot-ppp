# -*- coding: UTF-8 -*-
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp
import headpy.hbes.hconst as hconst


data = hfile.pkl_read('fdata/4.section-00-01.pkl')
energy_list = hppp.energy_list()
energy_order = energy_list.keys()
energy_order.sort()
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
for i in energy_order:
    output = ''
    output += '{:^20}'.format('%1.4f' % (i))
    output += '&{:^20}'.format('%.2f$\\pm$%.2f' % (data[i]['Nsignal'], data[i]['eNsignal']))
    output += '&{:^20}'.format('%s' % (hconst.energy_list()[i][3]))
    output += '&{:^20}'.format('%.2f' % (data[i]['Effect']))
    output += '&{:^20}'.format('%.2f' % (data[i]['isr']))
    output += '&{:^20}'.format('%.2f' % (data[i]['vpf']))
    output += '&{:^50}'.format('%.2f$\\pm$%.2f(%.1f\\%%)' % (data[i]['Section'],
                                                             data[i]['eSection'],
                                                             100 * data[i]['eSection'] / data[i]['Section']))
    print(output)
