# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
import lmfit
import copy
# Private package
import default as default
import headpy.hbes.hfunc as hfunc

################################################################################
# 拟合并绘制BES的结果
################################################################################


data = default.data_bes_pppmpz_fraction('rho1450pi')
print(len(data['x']))

x = data['x']
y = data['y']
e = data['e']
uy = copy.deepcopy(y)
ue = copy.deepcopy(e)

'''
for i in range(len(x)):
    if(x[i] == 2.125):
        ue[i] *= 3
'''
for i in range(len(x)):
    if(x[i] < 2.2 and x[i] != 2.125):
        #uy[i] *= 0.6
        #y[i] *= 0.6
        ue[i] *= 2


def my_function(e, mr, wr, b, phase,
                p1, p2, p3):
    output = hfunc.bes_line_shape_rho1450pi(e, mr, wr, b, phase,
                                            p1, p2, p3)
    return output


def my_function_resonance(e, mr, wr, b, phase):
    output = hfunc.bes_line_shape_rho1450pi_resonance(e, mr, wr, b, phase)
    return output


def func(p):
    output = (my_function(x,
                          p['mr'], p['wr'], p['b'], p['phase'],
                          p['p1'], p['p2'], p['p3']) - uy) / ue
    return output


parameter_init = (2.13, 0.07, 10.0, 0.0,
                  400.0, 2.9)
p = lmfit.Parameters()
p.add(name='mr', value=2.13, min=2.0, max=2.4)
p.add(name='wr', value=0.07, min=0.01, max=0.5)
p.add(name='b', value=10.0, min=0.01, max=100.0)
p.add(name='phase', value=0.0, min=-20.0, max=20.0)
p.add(name='p1', value=20.0, min=0.0, max=1000000.0)
p.add(name='p2', value=0.9, min=-100.0, max=100.0)
p.add(name='p3', value=0.0, min=-100.0, max=100.0)

mi = lmfit.minimize(func, params=p, method='leastsq')
lmfit.printfuncs.report_fit(mi.params, min_correl=0.5)
for name in mi.params:
    print(mi.params[name].value)
    print(mi.params[name].stderr)
'''
'''

# 绘制原图
fig, axes = plt.subplots(1, 1)
axe = axes
nx = numpy.arange(1.95, 3.08, 0.001)

axe.errorbar(data['x'],
             data['y'],
             yerr=data['e'],
             fmt='bo',
             label=r'Measurement')

'''
ny1 = my_function(nx,
                  parameter_init[0],
                  parameter_init[1],
                  parameter_init[2],
                  parameter_init[3],
                  parameter_init[4],
                  parameter_init[5])
axe.plot(nx, ny1, 'g-', label=r'Init fit')
'''

ny2 = my_function(nx,
                  mi.params['mr'].value,
                  mi.params['wr'].value,
                  mi.params['b'].value,
                  mi.params['phase'].value,
                  mi.params['p1'].value,
                  mi.params['p2'].value,
                  mi.params['p3'].value)
axe.plot(nx, ny2, 'r-', label=r'Best fit')

ny3 = my_function_resonance(nx,
                            mi.params['mr'].value,
                            mi.params['wr'].value,
                            mi.params['b'].value,
                            mi.params['phase'].value)
axe.plot(nx, ny3, 'g-', label=r'Resonance')


axe.legend(loc='best')
axe.set_xlabel(r'Energy (GeV)')
axe.set_ylabel(r'Born Cross Section (pb)')
#axe.set_title(r'Cross Section by BESIII')
plt.ylim((0, 130))
plt.savefig('opicture/lineshape/8_fit_rho1450pi.pdf')
plt.savefig('opicture/lineshape/8_fit_rho1450pi.png')
plt.show()
plt.close()
