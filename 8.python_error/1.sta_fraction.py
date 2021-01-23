# -*- coding: UTF-8 -*-
# Public package

# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp

output_rho770pi = {}
output_rho1450pi = {}
output_omega782pi = {}

for energy in hppp.energy_sort():
    output_rho770pi[energy] = hfile.pkl_read('../ppp_pwa/fdata_error/sta_fraction_rho770pi/%1.4f.pkl' % (energy))
    output_rho1450pi[energy] = hfile.pkl_read('../ppp_pwa/fdata_error/sta_fraction_rho1450pi/%1.4f.pkl' % (energy))
    output_omega782pi[energy] = hfile.pkl_read('../ppp_pwa/fdata_error/sta_fraction_omega782pi/%1.4f.pkl' % (energy))

hfile.pkl_dump('fdata_error/1.sta_fraction_rho770pi.pkl' % (), output_rho770pi)
hfile.pkl_dump('fdata_error/1.sta_fraction_rho1450pi.pkl' % (), output_rho1450pi)
hfile.pkl_dump('fdata_error/1.sta_fraction_omega782pi.pkl' % (), output_omega782pi)
