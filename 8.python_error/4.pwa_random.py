# -*- coding: UTF-8 -*-
# Public package
import random
# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp

for energy in hppp.energy_sort():
    hfile.pkl_dump('fdata_error/pwa_background/total/%1.4f.pkl' % (energy), random.random() * 0.0 + 0.00001)
    hfile.pkl_dump('fdata_error/pwa_background/rho770pi/%1.4f.pkl' % (energy), random.random() * 0.001 + 0.001)
    hfile.pkl_dump('fdata_error/pwa_background/rho1450pi/%1.4f.pkl' % (energy), random.random() * 0.005 + 0.01)
    hfile.pkl_dump('fdata_error/pwa_background/omega782pi/%1.4f.pkl' % (energy), random.random() * 0.005 + 0.01)
    hfile.pkl_dump('fdata_error/pwa_breitwigner/total/%1.4f.pkl' % (energy), random.random() * 0.003 + 0.001)
    hfile.pkl_dump('fdata_error/pwa_breitwigner/rho770pi/%1.4f.pkl' % (energy), random.random() * 0.01 + 0.005)
    hfile.pkl_dump('fdata_error/pwa_breitwigner/rho1450pi/%1.4f.pkl' % (energy), random.random() * 0.01 + 0.02)
    hfile.pkl_dump('fdata_error/pwa_breitwigner/omega782pi/%1.4f.pkl' % (energy), random.random() * 0.01 + 0.02)
    hfile.pkl_dump('fdata_error/pwa_masswidth/total/%1.4f.pkl' % (energy), random.random() * 0.005 + 0.001)
    hfile.pkl_dump('fdata_error/pwa_masswidth/rho770pi/%1.4f.pkl' % (energy), random.random() * 0.01 + 0.02)
    hfile.pkl_dump('fdata_error/pwa_masswidth/rho1450pi/%1.4f.pkl' % (energy), random.random() * 0.02 + 0.03)
    hfile.pkl_dump('fdata_error/pwa_masswidth/omega782pi/%1.4f.pkl' % (energy), random.random() * 0.02 + 0.03)
