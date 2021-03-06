# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
import lmfit
# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp

################################################################################
# 读取pwa_fraction_nominal
# 读取pwa_fraction_mean_error
# 进行拟合
# 存入pwa_mean_use
################################################################################

section = 'rho770pi'
nx = []
ny = []
ne = []
nn = []
for energy in hppp.energy_sort():
    nx.append(energy)
    multi_data = hfile.pkl_read('fdata_error/pwa_fraction_mean_error/%s/%1.4f.pkl' % (section, energy))
    nomin_data = hfile.pkl_read('fdata_error/pwa_fraction_nominal/%s/%1.4f.pkl' % (section, energy))
    ny.append(multi_data['mean'])
    ne.append(multi_data['error'])
    nn.append(nomin_data)
nx = numpy.array(nx)
ny = numpy.array(ny)
ne = numpy.array(ne)
ne = ne * ny
nn = numpy.array(nn)


def func_5(e, p0, p1, p2, p3, p4):
    return p0 + p1 * e + p2 * (e**2) + p3 * (e**3) + p4 * (e**4)


def func_error(p):
    p0 = p['p0']
    p1 = p['p1']
    p2 = p['p2']
    p3 = p['p3']
    p4 = p['p4']
    output = (func_5(nx, p0, p1, p2, p3, p4) - ny) / ne
    return output


plt.rcParams['figure.figsize'] = (9, 6)
fig, axes = plt.subplots(1)
axe = axes
axe.errorbar(nx, ny, yerr=ne,
             fmt='bo', label='Multi')
axe.errorbar(nx, nn,
             fmt='yo', label='Nominal')


if(1 == 1):
    parameters = lmfit.Parameters()
    parameters.add(name='p0', value=0.0, min=-1000.0, max=1000.0)
    parameters.add(name='p1', value=0.0, min=-1000.0, max=1000.0)
    parameters.add(name='p2', value=0.0, min=-1000.0, max=1000.0)
    parameters.add(name='p3', value=0.0, min=-1000.0, max=1000.0)
    parameters.add(name='p4', value=0.0, min=-1000.0, max=1000.0)
    result = lmfit.minimize(func_error, params=parameters, method='leastsq')
    lmfit.printfuncs.report_fit(result.params, min_correl=0.5)
    fx = numpy.arange(1.95, 3.10, 0.001)
    fy = func_5(fx, result.params['p0'].value,
                result.params['p1'].value,
                result.params['p2'].value,
                result.params['p3'].value,
                result.params['p4'].value)
    axe.plot(fx, fy, 'g-', label='Fitting')
    if(1 == 1):
        new_y = func_5(nx, result.params['p0'].value,
                       result.params['p1'].value,
                       result.params['p2'].value,
                       result.params['p3'].value,
                       result.params['p4'].value)
        new_y = (new_y - ny) * (ne / ny) + ny
        axe.errorbar(nx, new_y,
                     fmt='ro', label='Flated')
        if(1 == 1):
            for count, energy in enumerate(hppp.energy_sort()):
                hfile.pkl_dump('fdata_error/pwa_fraction_mean_use/%s/%1.4f.pkl' % (section, energy), (nn[count] + ny[count]) / 2)

axe.legend(loc='best')
plt.show()
plt.close()
