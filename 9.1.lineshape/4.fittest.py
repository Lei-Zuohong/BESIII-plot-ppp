# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
import lmfit
# Private package
import default as default
import headpy.hbes.hfunc as hfunc

################################################################################
# 拟合并绘制BES的结果
################################################################################


data = default.data_bes_pppmpz()
data = default.delete_point(data, [2.5, 2.7, 2.8])
print(len(data['x']))

x = data['x']
y = data['y']
e = data['e']


def my_function(e, mr, wr, sigma, phi, a, b):
    output = hfunc.bar_function(e, mr, wr, sigma, phi, a, b)
    return output


def func(p):
    output = (my_function(x, p['mr'], p['wr'], p['sigma'], p['phi'], p['a'], p['b']) - y) / 1.0
    return output


parameter_init = (2.13, 0.07, 25, 2.5, 55, 1.3)
parameter_bound = ((2.0, 2.3), (0.01, 0.2), (0.0, 100.0), (-4.0, 4.0), (0.0, 1000.0), (0.0, 10.0))


p = lmfit.Parameters()
p.add(name='mr', value=2.13, min=2.0, max=2.3)
p.add(name='wr', value=0.07, min=0.01, max=0.2)
p.add(name='sigma', value=25, min=0.0, max=100.0)
p.add(name='phi', value=2.5, min=-4.0, max=4.0)
p.add(name='a', value=55.0, min=0.0, max=1000.0)
p.add(name='b', value=1.3, min=0.0, max=10.0)

mi = lmfit.minimize(func, params=p, method='leastsq')
lmfit.printfuncs.report_fit(mi.params, min_correl=0.5)
for name in mi.params:
    print(mi.params[name].value)
    print(mi.params[name].stderr)

# 绘制原图
fig, axes = plt.subplots(1, 1)
axe = axes
nx = numpy.arange(1.95, 3.08, 0.001)

axe.errorbar(data['x'],
             data['y'],
             yerr=data['e'],
             fmt='bo',
             label=r'Born cross section (BESIII)')

ny1 = hfunc.bar_function(nx,
                         parameter_init[0],
                         parameter_init[1],
                         parameter_init[2],
                         parameter_init[3],
                         parameter_init[4],
                         parameter_init[5])
axe.plot(nx, ny1, 'g-', label=r'Init fit')

ny2 = hfunc.bar_function(nx,
                         mi.params['mr'].value,
                         mi.params['wr'].value,
                         mi.params['sigma'].value,
                         mi.params['phi'].value,
                         mi.params['a'].value,
                         mi.params['b'].value)
axe.plot(nx, ny2, 'r-', label=r'Best fit')

axe.legend(loc=1)
axe.set_xlabel(r'Energy (GeV)')
axe.set_ylabel(r'Cross Section (pb)')
axe.set_title(r'Cross Section by BESIII')
plt.ylim((0, 600))
plt.show()
plt.close()
