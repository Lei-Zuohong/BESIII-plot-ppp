# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
from lmfit import Model
# Private package
import default as default

################################################################################
# 拟合并绘制BES的结果
################################################################################


def my_function(e, mr, wr, sigma, phi, a, b):
    output = default.bar_function(e, mr, wr, sigma, phi, a, b)
    return output


def poly2d(e, a, b):
    output = default.bar_none(e, a, b)
    output = output**2
    return output


test_resonance = 1
test_nonresonance = 0
plot_test = 0
# 读取数据
print('开始读取数据')
data_bes_pppmpz = default.data_bes_pppmpz_fraction('rho770pi')
print('读取数据完毕')
# 合并数据
print('开始处理数据')
data_bes_pppmpz = default.delete_point(data_bes_pppmpz, [2.5, 2.7, 2.8])
print('处理数据完毕')
# 拟合共振态
if(test_resonance == 1):
    module_all = Model(my_function, independent_vars=['e'])
    params = module_all.make_params(mr=2.13,
                                    wr=0.05,
                                    sigma=30,
                                    phi=1.57,
                                    a=35,
                                    b=1.6)
    result = module_all.fit(data_bes_pppmpz['y'], e=data_bes_pppmpz['x'], params=params)
    print(result.fit_report())
# 拟合非共振态
if(test_nonresonance == 1):
    module_none = Model(poly2d, independent_vars=['e'])
    params = module_none.make_params(a=1,
                                     b=1)
    result2 = module_none.fit(data_bes_pppmpz['y'], e=data_bes_pppmpz['x'], params=params)
    print(result2.fit_report())
# 绘制原图
fig, axes = plt.subplots(1, 1)
axe = axes
axe.errorbar(data_bes_pppmpz['x'],
             data_bes_pppmpz['y'],
             yerr=data_bes_pppmpz['e'],
             fmt='bo:',
             label=r'$\rho(770)\pi$ Born cross section (BESIII)')
# 绘图共振态
nx = numpy.arange(1.95, 3.08, 0.001)
if(test_resonance == 1):
    ny2 = default.bar_function(nx,
                               result.best_values['mr'],
                               result.best_values['wr'],
                               result.best_values['sigma'],
                               result.best_values['phi'],
                               result.best_values['a'],
                               result.best_values['b'],)
    axe.plot(nx, ny2, 'g-', label=r'Best fit')
# 绘图非共振态
if(test_nonresonance == 1):
    ny3 = poly2d(nx,
                 result2.best_values['a'],
                 result2.best_values['b'])
    axe.plot(nx, ny3, 'r--', label=r'Polynomial fit')


# 测试共振态
if(plot_test == 1):
    ny1 = default.bar_function(nx,
                               2.13,
                               0.05,
                               30,
                               1.57,
                               35,
                               1.6)
    axe.plot(nx, ny1, 'g-', label=r'Fit with resonance')

axe.legend(loc=1)
axe.set_xlabel(r'Energy (GeV)')
axe.set_ylabel(r'Cross Section (pb)')
axe.set_title(r'Cross Section by BESIII')
plt.ylim((0, 600))
plt.savefig('9.1.lineshape/2.fitbes_rho770.pdf')
plt.show()
plt.close()

# 输出数据到txt
if(1 == 0):
    output = ''
    output_x = numpy.arange(1.95, 3.10, 0.001)
    for i in output_x:
        '''
        output += '%1.5f %1.5f 0\n' % (i, my_function(i,
                                                      result.best_values['mr'],
                                                      result.best_values['wr'],
                                                      result.best_values['sigma'],
                                                      result.best_values['phi'],
                                                      result.best_values['a'],
                                                      result.best_values['b']) / 1000)
        '''
        output += '%1.5f %1.5f 0\n' % (i, my_function(i,
                                                      2.15,
                                                      0.1,
                                                      20,
                                                      1.2,
                                                      52,
                                                      1 / 1000))
    with open('9.1.lineshape/xs_user.txt', 'w') as outfile:
        outfile.write(output)
