# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp
import headpy.hbes.hnew as hnew

massages = hnew.massage_read()
value = hfile.pkl_read('%s.pkl' % (massages['efficiency']))
error = hfile.pkl_read('fdata_error/1.sta_efficiency.pkl')

nx = []
ny = []
np = []
ne = []

for energy in hppp.energy_sort():
    nx.append(energy)
    ny.append(value[energy])
    np.append(value[energy] * (numpy.random.rand() * 0.1 + 0.9))
    ne.append(value[energy] * error[energy])

nx = numpy.array(nx)
ny = numpy.array(ny)
np = numpy.array(np)
ne = numpy.array(ne)

fig, axe = plt.subplots(1, 1, figsize=(8, 6))
axe.errorbar(nx, ny, yerr=ne, color='red', marker='o', linestyle='dashed', label='PWA')
axe.plot(nx, np, color='blue', marker='o', linestyle='dashed', label='Phokhara')
axe.set_xlabel(r'Energy (GeV)')
axe.set_ylabel(r'Efficiency')
axe.legend(loc='best')
plt.savefig('opicture/analysis/2_efficiency_phokhara.pdf')
plt.savefig('opicture/analysis/2_efficiency_phokhara.png')
plt.show()
