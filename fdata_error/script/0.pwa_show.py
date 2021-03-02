# -*- coding: UTF-8 -*-
# Public package
import random
# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp

energy_sort = hppp.energy_sort()
sections_sort = ['total', 'rho770pi', 'rho1450pi', 'omega782pi']
error_efficiency = {}
error_background = {'total': {}, 'rho770pi': {}, 'rho1450pi': {}, 'omega782pi': {}}
error_breitwigner = {'total': {}, 'rho770pi': {}, 'rho1450pi': {}, 'omega782pi': {}}
error_masswidth = {'total': {}, 'rho770pi': {}, 'rho1450pi': {}, 'omega782pi': {}}
error_total = {'total': {}, 'rho770pi': {}, 'rho1450pi': {}, 'omega782pi': {}}
for energy in hppp.energy_sort():
    error_efficiency[energy] = hfile.pkl_read('fdata_error/pwa_efficiency/%1.4f.pkl' % (energy))
    for section in sections_sort:
        error_background[section][energy] = hfile.pkl_read('fdata_error/pwa_background/%s/%1.4f.pkl' % (section, energy))
        error_breitwigner[section][energy] = hfile.pkl_read('fdata_error/pwa_breitwigner/%s/%1.4f.pkl' % (section, energy))
        error_masswidth[section][energy] = hfile.pkl_read('fdata_error/pwa_masswidth/%s/%1.4f.pkl' % (section, energy))
        error_total[section][energy] = hfile.pkl_read('fdata_error/pwa_total/%s/%1.4f.pkl' % (section, energy))


output = ''
output += '{:^10}&'.format('Energy')
output += '{:^12}&'.format('Efficiency')
output += '{:^12}&'.format('Background')
output += '{:^10}&'.format(' ')
output += '{:^10}&'.format(' ')
#output += '{:^12}&'.format(' ')
output += '{:^12}&'.format('Mass Width')
output += '{:^10}&'.format(' ')
output += '{:^10}&'.format(' ')
#output += '{:^12}&'.format(' ')
output += '{:^12}&'.format('BW func')
output += '{:^10}&'.format(' ')
output += '{:^10}&'.format(' ')
#output += '{:^12}&'.format(' ')
output += '{:^12}&'.format('Total Sys')
output += '{:^10}&'.format(' ')
output += '{:^10}&'.format(' ')
#output += '{:^12}&'.format(' ')
output = output[:-1]
output += '\\\\\n'
output += '{:^10}&'.format(' ')
output += '{:^12}&'.format(' ')
output += '{:^12}&'.format('3Pi')
output += '{:^10}&'.format('Rhopi')
output += '{:^10}&'.format('Rho*pi')
#output += '{:^12}&'.format('Omegapi')
output += '{:^12}&'.format('3Pi')
output += '{:^10}&'.format('Rhopi')
output += '{:^10}&'.format('Rho*pi')
#output += '{:^12}&'.format('Omegapi')
output += '{:^12}&'.format('3Pi')
output += '{:^10}&'.format('Rhopi')
output += '{:^10}&'.format('Rho*pi')
#output += '{:^12}&'.format('Omegapi')
output += '{:^12}&'.format('3Pi')
output += '{:^10}&'.format('Rhopi')
output += '{:^10}&'.format('Rho*pi')
#output += '{:^12}&'.format('Omegapi')
output = output[:-1]
output += '\\\\\n'
for energy in energy_sort:
    output += '{:^10}&'.format('%1.4f' % (energy))
    output += '{:^12}&'.format('%.2f' % (100 * error_efficiency[energy]))
    output += '{:^12}&'.format('%.2f' % (100 * error_background['total'][energy]))
    output += '{:^10}&'.format('%.2f' % (100 * error_background['rho770pi'][energy]))
    output += '{:^10}&'.format('%.2f' % (100 * error_background['rho1450pi'][energy]))
#    output += '{:^12}&'.format('%.2f' % (100 * error_background['omega782pi'][energy]))
    output += '{:^12}&'.format('%.2f' % (100 * error_masswidth['total'][energy]))
    output += '{:^10}&'.format('%.2f' % (100 * error_masswidth['rho770pi'][energy]))
    output += '{:^10}&'.format('%.2f' % (100 * error_masswidth['rho1450pi'][energy]))
#    output += '{:^12}&'.format('%.2f' % (100 * error_masswidth['omega782pi'][energy]))
    output += '{:^12}&'.format('%.2f' % (100 * error_breitwigner['total'][energy]))
    output += '{:^10}&'.format('%.2f' % (100 * error_breitwigner['rho770pi'][energy]))
    output += '{:^10}&'.format('%.2f' % (100 * error_breitwigner['rho1450pi'][energy]))
#    output += '{:^12}&'.format('%.2f' % (100 * error_breitwigner['omega782pi'][energy]))
    output += '{:^12}&'.format('%.2f' % (100 * error_total['total'][energy]))
    output += '{:^10}&'.format('%.2f' % (100 * error_total['rho770pi'][energy]))
    output += '{:^10}&'.format('%.2f' % (100 * error_total['rho1450pi'][energy]))
#    output += '{:^12}&'.format('%.2f' % (100 * error_total['omega782pi'][energy]))
    output = output[:-1]
    output += '\\\\\n'


print(output)
