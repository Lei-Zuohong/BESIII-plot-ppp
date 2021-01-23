# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp

data1 = hfile.pkl_read('fdata/1.factor-00-01.pkl')
data2 = hfile.pkl_read('fdata/1.factor-00-02.pkl')
data3 = hfile.pkl_read('fdata/1.factor-00-03.pkl')


nx = []
ny1 = []
ny2 = []
ny3 = []
for energy in hppp.energy_sort():
    nx.append(energy)
    ny1.append(data1[energy]['isr'] * data1[energy]['vpf'])
    ny2.append(data2[energy]['isr'] * data2[energy]['vpf'])
    ny3.append(data3[energy]['isr'] * data3[energy]['vpf'])


fig, axe = plt.subplots(1, 1, figsize=(8, 6))
axe.plot(nx, ny1, color='yellow', marker='o', linestyle='dashed', label='Iteration-1')
axe.plot(nx, ny2, color='green', marker='o', linestyle='dashed', label='Iteration-2')
axe.plot(nx, ny3, color='red', marker='o', linestyle='dashed', label='Iteration-3')
axe.set_xlabel(r'Energy (GeV)')
axe.set_ylabel(r'1+$\delta$')
axe.legend(loc='best')
plt.savefig('opicture/analysis/2_isrieration.pdf')
plt.savefig('opicture/analysis/2_isrieration.png')
plt.show()
