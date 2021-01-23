# -*- coding: UTF-8 -*-
# Public package
import math
import numpy
import matplotlib.pyplot as plt
from lmfit import Model
from scipy.optimize import curve_fit
# Private package
import default as default
import headpy.hbes.hfunc as hfunc


data_bes_pppmpz = default.data_bes_pppmpz()
data_babar = default.data_babar_pppmpz()
data_snd = default.data_snd_pppmpz()
data_beslow = default.data_beslow_pppmpz()

data_use = data_bes_pppmpz

x = numpy.linspace(0.1, 3, 290)
length = len(data_use['x'])
print(length)
if(1 == 1):
    output = ''
    output += '{'
    for count, i in enumerate(data_use['x']):
        if(count == length - 1):
            output += '%f' % (i)
        else:
            output += '%f,' % (i)
        if(count % 5 == 4):
            output += '\n'
    output += '}'
    print(output)
if(1 == 1):
    output = ''
    output += '{'
    for count in range(length):
        if(count == length - 1):
            output += '%f' % (0.0)
        else:
            output += '%f,' % (0.0)
        if(count % 5 == 4):
            output += '\n'
    output += '}'
    print(output)
if(1 == 1):
    output = ''
    output += '{'
    for count, i in enumerate(data_use['y']):
        if(count == length - 1):
            output += '%f' % (i)
        else:
            output += '%f,' % (i)
        if(count % 5 == 4):
            output += '\n'
    output += '}'
    print(output)
if(1 == 1):
    output = ''
    output += '{'
    for count, i in enumerate(data_use['e']):
        if(count == length - 1):
            output += '%f' % (i)
        else:
            output += '%f,' % (i)
        if(count % 5 == 4):
            output += '\n'
    output += '}'
    print(output)


'''
module_all = Model(hfunc.snd_line_shape, independent_vars=['e'])
params = module_all.make_params(mr_omega1450=1.450, wr_omega1450=0.88, b1b2_omega1450=73,
                                mr_omega1680=1.680, wr_omega1680=0.31, b1b2_omega1680=156,
                                back=0.0,
                                phase_omega1450=0.0,
                                phase_omega1680=0.0,
                                phase_back=0.0)
result = module_all.fit(data_snd['y'],
                        e=data_snd['x'],
                        params=params)
print(result.fit_report())
y = hfunc.snd_line_shape(x,
                         result.best_values['mr_omega1450'], result.best_values['wr_omega1450'], result.best_values['b1b2_omega1450'],
                         result.best_values['mr_omega1680'], result.best_values['wr_omega1680'], result.best_values['b1b2_omega1680'],
                         result.best_values['back'],
                         result.best_values['phase_omega1450'],
                         result.best_values['phase_omega1680'],
                         result.best_values['phase_back'])
y = hfunc.snd_line_shape(x,
                         1.27589e+00, 8.58246e-01, 3.85164e+01,
                         1.65721e+00, 2.09581e-01, 8.37485e+01,
                         6.97066e+01,
                         -3.70040e-01,
                         1.66152e+00,
                         -3.68536e+00)
plt.rcParams['figure.figsize'] = (9, 6)
fig, axes = plt.subplots(1)
axe = axes
axe.plot(x, y, color='red', linewidth=1.0, linestyle='--')
axe.errorbar(data_snd['x'],
             data_snd['y'],
             yerr=data_snd['e'],
             fmt='go',
             label=r'SND')
plt.xlim((1.0, 2.0))
plt.ylim((0, 8000))
plt.show()
'''
