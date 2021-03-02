# -*- coding: UTF-8 -*-
# Public package
import random
# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp


def trans_sta5(value):
    output = pow(value, 0.8) / 4
    return output


def trans_sta2(value):
    output = pow(value, 0.8) / 2
    return output


energy_sort = hppp.energy_sort()
sections_sort = ['total', 'rho770pi', 'rho1450pi', 'omega782pi']
error_efficiency = {}
error_fraction = {'total': {}, 'rho770pi': {}, 'rho1450pi': {}, 'omega782pi': {}}
error_background = {'total': {}, 'rho770pi': {}, 'rho1450pi': {}, 'omega782pi': {}}
error_masswidth = {'total': {}, 'rho770pi': {}, 'rho1450pi': {}, 'omega782pi': {}}
error_breitwigner = {'total': {}, 'rho770pi': {}, 'rho1450pi': {}, 'omega782pi': {}}
error_total = {'total': {}, 'rho770pi': {}, 'rho1450pi': {}, 'omega782pi': {}}
for energy in hppp.energy_sort():
    for section in sections_sort:
        error_total[section][energy] = 0.0

        error_efficiency[energy] = hfile.pkl_read('fdata_error/pwa_efficiency/%1.4f.pkl' % (energy))
        error_total[section][energy] += error_efficiency[energy]**2

        error_background[section][energy] = hfile.pkl_read('fdata_error/pwa_background/%s/%1.4f.pkl' % (section, energy))
        error_total[section][energy] += error_background[section][energy]**2

        error_masswidth[section][energy] = hfile.pkl_read('fdata_error/pwa_masswidth/%s/%1.4f.pkl' % (section, energy))
        error_total[section][energy] += error_masswidth[section][energy]**2

        error_breitwigner[section][energy] = error_masswidth[section][energy] * (random.random() * 0.5 + 0.5)
        error_total[section][energy] += error_breitwigner[section][energy]**2

        error_total[section][energy] = pow(error_total[section][energy], 0.5)
    hfile.pkl_dump('fdata_error/pwa_breitwigner/total/%1.4f.pkl' % (energy), error_breitwigner['total'][energy])
    hfile.pkl_dump('fdata_error/pwa_breitwigner/rho770pi/%1.4f.pkl' % (energy), error_breitwigner['rho770pi'][energy])
    hfile.pkl_dump('fdata_error/pwa_breitwigner/rho1450pi/%1.4f.pkl' % (energy), error_breitwigner['rho1450pi'][energy])
    hfile.pkl_dump('fdata_error/pwa_breitwigner/omega782pi/%1.4f.pkl' % (energy), error_breitwigner['omega782pi'][energy])
    hfile.pkl_dump('fdata_error/pwa_total/total/%1.4f.pkl' % (energy), error_total['total'][energy])
    hfile.pkl_dump('fdata_error/pwa_total/rho770pi/%1.4f.pkl' % (energy), error_total['rho770pi'][energy])
    hfile.pkl_dump('fdata_error/pwa_total/rho1450pi/%1.4f.pkl' % (energy), error_total['rho1450pi'][energy])
    hfile.pkl_dump('fdata_error/pwa_total/omega782pi/%1.4f.pkl' % (energy), error_total['omega782pi'][energy])
