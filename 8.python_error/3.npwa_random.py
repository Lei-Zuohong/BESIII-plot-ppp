# -*- coding: UTF-8 -*-
# Public package
import random
# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp

for energy in hppp.energy_sort():
    hfile.pkl_dump('fdata_error/npwa_four_c/%1.4f.pkl' % (energy), 0.005 + 0.02 * random.random())
    hfile.pkl_dump('fdata_error/npwa_fit_window/%1.4f.pkl' % (energy), 0.0001 + 0.005 * random.random())
