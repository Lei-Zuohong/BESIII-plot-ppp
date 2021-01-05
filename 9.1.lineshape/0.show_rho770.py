# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
# Private package
import default as default

################################################################################
# 拟合并绘制BES的结果 -  rho770pi
################################################################################


def my_function(e, mr, wr, sigma, phi, a, b):
    output = default.bar_function(e, mr, wr, sigma, phi, a, b)
    return output


def poly2d(e, a, b):
    output = default.bar_none(e, a, b)
    output = output**2
    return output


# 读取数据
print('开始读取数据')
data_bes_rho770 = default.data_bes_pppmpz_fraction('rho770pi')
data_bes_omega782 = default.data_bes_pppmpz_fraction('omega782pi')
data_bes_rho1450 = default.data_bes_pppmpz_fraction('rho1450pi')
data_bes_omegapi = default.data_bes_omegapi()
print('读取数据完毕')
# 合并数据
print('开始处理数据')
data_bes_rho770 = default.delete_point(data_bes_rho770, [2.5, 2.7, 2.8])
data_bes_omega782 = default.delete_point(data_bes_omega782, [2.5, 2.7, 2.8])
print('处理数据完毕')
# 绘制原图
plt.rcParams['figure.figsize'] = (9, 6)
fig, axes = plt.subplots(1)
axe = axes
axe.errorbar(data_bes_rho770['x'],
             data_bes_rho770['y'],
             yerr=data_bes_rho770['e'],
             fmt='bo:',
             label=r'$\rho\pi$ by PWA')
axe.errorbar(data_bes_omega782['x'],
             data_bes_omega782['y'],
             yerr=data_bes_omega782['e'],
             fmt='ro:',
             label=r'$\omega\pi$ by PWA')
axe.errorbar(data_bes_omegapi['x'],
             data_bes_omegapi['y'],
             yerr=data_bes_omegapi['e'],
             fmt='go:',
             label=r'$\omega\pi$')

axe.legend(loc=1)
axe.set_xlabel(r'Energy (GeV)')
axe.set_ylabel(r'Born Cross Section (pb)')
axe.set_title(r'Born Cross Section')
plt.xlim((1.9, 3.2))
plt.ylim((0, 1500))
plt.savefig('9.1.lineshape/0.show_rho770.pdf')
plt.show()
plt.close()
