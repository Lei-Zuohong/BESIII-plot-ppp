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

use_error = 0
unuse_points = [2.5, 2.7, 2.8]

data = default.data_bes_pppmpz_fraction('rho770pi')
data = default.delete_point(data, unuse_points)
print(len(data['x']))

x = data['x']
y = data['y']
e = data['e']
ue = copy.deepcopy(e)


def my_function(e, mr, wr, b, phase,
                p1, p2, p3):
    output = hfunc.snd_line_shape_rho770pi(e, mr, wr, b, phase,
                                           p1, p2, p3)
    return output


def func(p):
    if(use_error == 1):
        output = (my_function(x,
                              p['mr'], p['wr'], p['b'], p['phase'],
                              p['p1'], p['p2'], p['p3']) - y) / ue
    else:
        output = (my_function(x,
                              p['mr'], p['wr'], p['b'], p['phase'],
                              p['p1'], p['p2'], p['p3']) - y) / 1
    return output


p = lmfit.Parameters()
p.add(name='mr', value=2.2, min=2.0, max=2.5)
p.add(name='wr', value=0.15, min=0.01, max=0.2)
p.add(name='b', value=10.0, min=0.01, max=100.0)
p.add(name='phase', value=0.0, min=-20.0, max=20.0)
p.add(name='p1', value=1000000000.0, min=0.0, max=1000000000.0)
p.add(name='p2', value=7.09268368, min=-100.0, max=100.0)
p.add(name='p3', value=-8.32936732, min=-100.0, max=100.0)
mi = lmfit.minimize(func, params=p, method='leastsq')
lmfit.printfuncs.report_fit(mi.params, min_correl=0.5)
for name in mi.params:
    print(mi.params[name].value)
    print(mi.params[name].stderr)

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
                  mi.params['p1'].value,
                  mi.params['p2'].value,
                  mi.params['p3'].value)
axe.plot(nx, ny2, 'b-', label=r'Best fit')

ny3 = my_function(nx,
                  mi.params['mr'].value,
                  mi.params['wr'].value,
                  mi.params['b'].value,
                  mi.params['phase'].value,
                  0.0,
                  mi.params['p2'].value,
                  mi.params['p3'].value)
axe.plot(nx, ny3, 'g-', label=r'Resonance')


axe.legend(loc='best')
axe.set_xlabel(r'Energy (GeV)')
axe.set_ylabel(r'Born Cross Section (pb)')
#axe.set_title(r'Cross Section by BESIII')
plt.ylim((0, 600))
# plt.savefig('opicture/lineshape/8_fit_rho770pi.pdf')
# plt.savefig('opicture/lineshape/8_fit_rho770pi.png')
plt.show()
plt.close()

output = ''
for i in range(len(nx)):
    output += '%.5f %.5f 0\n' % (nx[i], ny2[i])
hfile.txt_write('9.1.lineshape/xs_user.txt', output)
