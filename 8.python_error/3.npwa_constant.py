# -*- coding: UTF-8 -*-
# Public package
# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp

for energy in hppp.energy_sort():
    hfile.pkl_dump('fdata_error/npwa_luminosity/%1.4f.pkl' % (energy), 0.01)
    hfile.pkl_dump('fdata_error/npwa_track_pid/%1.4f.pkl' % (energy), 0.02)
    hfile.pkl_dump('fdata_error/npwa_track_charge/%1.4f.pkl' % (energy), 0.02)
    hfile.pkl_dump('fdata_error/npwa_track_neutral/%1.4f.pkl' % (energy), 0.02)
    hfile.pkl_dump('fdata_error/npwa_fit_back/%1.4f.pkl' % (energy), 0.00001)
    hfile.pkl_dump('fdata_error/npwa_branch/%1.4f.pkl' % (energy), 0.034 / 98.823)
    hfile.pkl_dump('fdata_error/npwa_isr/%1.4f.pkl' % (energy), 0.005)
