# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
import scipy.optimize
# Private package
import default as default
import headpy.hbes.hfunc as hfunc

################################################################################
# 拟合并绘制BES的结果
################################################################################


data = default.data_bes_pppmpz()
data = default.delete_point(data, [2.5, 2.7, 2.8])
print(len(data['x']))


def my_function(e, mr, wr, sigma, phi, a, b):
    output = hfunc.bar_function(e, mr, wr, sigma, phi, a, b)
    return output


def func(x):
    output = 0
    for i in range(len(data['x'])):
        #output += ((my_function(data['x'][i], x[0], x[1], x[2], x[3], x[4], x[5]) - data['y'][i]) / data['e'][i])**2
        output += ((my_function(data['x'][i], x[0], x[1], x[2], x[3], x[4], x[5]) - data['y'][i]))**2
    output = pow(output, 0.5)
    return output


parameter_init = (2.13, 0.07, 25, 2.5, 55, 1.3)
parameter_bound = ((2.0, 2.3), (0.01, 0.2), (0.0, 100.0), (-4.0, 4.0), (0.0, 1000.0), (0.0, 10.0))
result = scipy.optimize.minimize(func,
                                 x0=parameter_init,
                                 method='SLSQP',
                                 bounds=parameter_bound)
print(result)


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
                         result.x[0],
                         result.x[1],
                         result.x[2],
                         result.x[3],
                         result.x[4],
                         result.x[5])
axe.plot(nx, ny2, 'r-', label=r'Best fit')

axe.legend(loc=1)
axe.set_xlabel(r'Energy (GeV)')
axe.set_ylabel(r'Cross Section (pb)')
axe.set_title(r'Cross Section by BESIII')
plt.ylim((0, 600))
plt.show()
plt.close()
