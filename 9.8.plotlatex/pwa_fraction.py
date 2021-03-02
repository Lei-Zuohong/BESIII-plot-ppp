# -*- coding: UTF-8 -*-
# Public package
# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp

waves = ['rho770pi', 'rho1450pi', 'rho1700pi', 'omega782pi', 'rho1690pi']
energy_sort = hppp.energy_sort()

for energy in energy_sort:
    if(energy not in [2.125, 2.396, 2.9]): continue
    data = hfile.pkl_read('../ppp_pwa/output_nominal/%1.4f.pkl' % (energy))
    fraction = data.fraction
    print(fraction)
    for count1, i1 in enumerate(waves):
        output = ''
        for count2, i2 in enumerate(waves):
            if(count2 < count1):
                output += '{:^10} &'.format('-')
            elif(count1 == count2):
                output += '{:^10} &'.format('%.4f' % (fraction[i1][i2]))
            else:
                output += '{:^10} &'.format('%.4f' % (fraction[i1][i2] + fraction[i2][i1]))
        output = output[:-2]
        output += '\\\\'
        print(output)
