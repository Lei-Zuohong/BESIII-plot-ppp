# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp

nx = []
ny1 = []
ny2 = []
ne2 = []

for energy in hppp.energy_sort():
    nx.append(energy)
    ny1.append(hfile.pkl_read('fdata_error/sta_efficiency_nominal/omega782pi/%1.4f.pkl' % (energy)))
    ny2.append(hfile.pkl_read('fdata_error/sta_efficiency_mean/omega782pi/%1.4f.pkl' % (energy)))
    ne2.append(hfile.pkl_read('fdata_error/sta_efficiency_error/omega782pi/%1.4f.pkl' % (energy)))
nx = numpy.array(nx)
ny1 = numpy.array(ny1)
ny2 = numpy.array(ny2)
ne2 = numpy.array(ne2)


plt.rcParams['figure.figsize'] = (9, 6)
fig, axes = plt.subplots(1)
axe = axes
axe.errorbar(nx, ny2, yerr=ne2,
             fmt='bo', label='Sta')
axe.errorbar(nx, ny1,
             fmt='ro', label='One')
plt.show()
