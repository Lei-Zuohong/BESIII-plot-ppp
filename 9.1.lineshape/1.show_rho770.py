# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
# Private package
import default as default

################################################################################
# 拟合并绘制BES的结果
################################################################################


# 读取数据
print('开始读取数据')
data_bes_pppmpz = default.data_bes_pppmpz_fraction('rho770pi')
data_snd = default.data_snd_rhopi()
print('读取数据完毕')
# 绘制原图
plt.rcParams['figure.figsize'] = (9, 6)
fig, axes = plt.subplots(1)
axe = axes
axe.errorbar(data_snd['x'],
             data_snd['y'],
             yerr=data_snd['e'],
             fmt='go',
             label=r'SND')
axe.errorbar(data_bes_pppmpz['x'],
             data_bes_pppmpz['y'],
             yerr=data_bes_pppmpz['e'],
             fmt='bo',
             label=r'BESIII R-scan data')

axe.legend(loc=1)
axe.set_xlabel(r'Energy (GeV)')
axe.set_ylabel(r'Born Cross Section (pb)')
#axe.set_title(r'Born Cross Section of $e^{+}e^{-}\rightarrow\pi^{+}\pi^{-}\pi^{0}$')
plt.xlim((2.0, 3.2))
plt.ylim((0, 600))
plt.savefig('opicture/lineshape/7_show_rho770pi.pdf')
plt.savefig('opicture/lineshape/7_show_rho770pi.png')
plt.show()
plt.close()
