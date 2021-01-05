# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
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


# 读取数据
print('开始读取数据')
data_bes_pppmpz = default.data_bes_pppmpz()
data_babar = default.data_babar_pppmpz()
data_snd = default.data_snd_pppmpz()
data_beslow = default.data_beslow_pppmpz()
print('读取数据完毕')
# 绘制原图
plt.rcParams['figure.figsize'] = (9, 6)
fig, axes = plt.subplots(1)
axe = axes
axe.errorbar(data_babar['x'],
             data_babar['y'],
             yerr=data_babar['e'],
             fmt='ro:',
             label=r'BABAR')
axe.errorbar(data_snd['x'],
             data_snd['y'],
             yerr=data_snd['e'],
             fmt='go:',
             label=r'SND')
axe.errorbar(data_beslow['x'],
             data_beslow['y'],
             yerr=data_beslow['e'],
             fmt='yo:',
             label=r'BESIII ISR data')
axe.errorbar(data_bes_pppmpz['x'],
             data_bes_pppmpz['y'],
             yerr=data_bes_pppmpz['e'],
             fmt='bo:',
             label=r'BESIII R-scan data')

axe.legend(loc=1)
axe.set_xlabel(r'Energy (GeV)')
axe.set_ylabel(r'Born Cross Section (pb)')
axe.set_title(r'Born Cross Section of $e^{+}e^{-}\rightarrow\pi^{+}\pi^{-}\pi^{0}$')
plt.xlim((1.9, 3.2))
plt.ylim((0, 700))
plt.savefig('9.1.lineshape/1.show.pdf')
plt.show()
plt.close()