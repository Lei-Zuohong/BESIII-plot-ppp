# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
import lmfit
import copy
# Private package
import default as default
import headpy.hbes.hfunc as hfunc
import headpy.hfile as hfile

################################################################################
# 拟合并绘制BES的结果
################################################################################


data = default.data_bes_pppmpz_fraction('rho1450pi')
data = default.delete_point(data, [2.5, 2.7, 2.8])
print(len(data['x']))

x = data['x']
y = data['y']
e = data['e']
ue = copy.deepcopy(e)

for i in numpy.where(x < 2.45):
    ue[i] = e[i] / 2
for i in numpy.where(x > 2.45):
    ue[i] = 5 * e[i]
'''
'''


def my_function(e,
                mr, wr, b, phase,
                mr_c, wr_c, b_c, phase_c,
                p0):
    output = hfunc.bes_line_shape_rho770pi(e,
                                           mr, wr, b, phase,
                                           mr_c, wr_c, b_c, phase_c,
                                           p0)
    return output


def my_function_resonance(e, mr, wr, b, phase):
    output = hfunc.bes_line_shape_rho770pi_resonance(e, mr, wr, b, phase)
    return output


def func(p):
    output = (my_function(x,
                          p['mr'], p['wr'], p['b'], p['phase'],
                          p['mr_c'], p['wr_c'], p['b_c'], p['phase_c'],
                          p['p0']) - y) / ue
    return output


parameter_init = (2.13, 0.07, 10.0, 0.0,
                  400.0, 2.9)
p = lmfit.Parameters()
p.add(name='mr', value=2.23, min=2.0, max=2.4)
p.add(name='wr', value=0.07, min=0.01, max=0.4)
p.add(name='b', value=10.0, min=0.01, max=100.0)
p.add(name='phase', value=0.0, min=-200.0, max=200.0)
p.add(name='mr_c', value=1.5, min=1.0, max=2.0)
p.add(name='wr_c', value=1.0, min=0.01, max=5.0)
p.add(name='b_c', value=1000.0, min=0.01, max=10000.0)
p.add(name='phase_c', value=0.0, min=-200.0, max=200.0)
p.add(name='p0', value=0.0, min=-1000.0, max=1000.0)

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
nx = numpy.arange(1.95, 3.10, 0.0001)

axe.errorbar(data['x'],
             data['y'],
             yerr=data['e'],
             fmt='ro',
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
                  mi.params['mr_c'].value,
                  mi.params['wr_c'].value,
                  mi.params['b_c'].value,
                  mi.params['phase_c'].value,
                  mi.params['p0'].value)
axe.plot(nx, ny2, 'b-', label=r'Best fit')

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
plt.ylim((0, 100))
plt.savefig('opicture/lineshape/8_fit_rho770pi.pdf')
plt.savefig('opicture/lineshape/8_fit_rho770pi.png')
plt.show()
plt.close()

output = ''
for i in range(len(nx)):
    output += '%.5f %.5f 0\n' % (nx[i], ny2[i])
hfile.txt_write('9.1.lineshape/xs_user.txt', output)
