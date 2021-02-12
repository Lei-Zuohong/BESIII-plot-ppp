# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package
import headpy.hfile as hfile
import headpy.hbes.hnew as hnew
import headpy.hbes.hppp as hppp

waves = ['rho770pi', 'rho1450pi', 'omega782pi']
massages = hnew.massage_read()
total_event = hfile.pkl_read('%s.pkl' % (massages['nevent']))
for wave in waves:
    output = {}
    for energy in hppp.energy_sort():
        fraction = hfile.pkl_read('../ppp_pwa/output_nominal/%1.4f.pkl' % (energy)).fraction[wave][wave]
        factor = total_event[energy]['enevent'] / pow(total_event[energy]['nevent'], 0.5)

        wave_nevent = total_event[energy]['nevent'] * fraction
        wave_enevent = pow(total_event[energy]['nevent'] * fraction, 0.5) * factor
        print('%s %1.4f %f %f' % (wave, energy, wave_nevent, wave_enevent))
        output[energy] = {}
        output[energy]['nevent'] = wave_nevent
        output[energy]['enevent'] = wave_enevent
    hfile.pkl_dump('fdata/3.nevent_%s.pkl' % (wave), output)
