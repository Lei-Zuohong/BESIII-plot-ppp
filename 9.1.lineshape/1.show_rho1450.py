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
data_bes_rho1450 = default.data_bes_pppmpz_fraction('rho1450pi')
data_bes_rho770 = default.data_bes_pppmpz_fraction('rho770pi')
data_snd = default.data_snd_rhopi()
print('读取数据完毕')
# 绘制原图
plt.rcParams['figure.figsize'] = (9, 6)
fig, axes = plt.subplots(1)
axe = axes
axe.errorbar(data_bes_rho1450['x'],
             data_bes_rho1450['y'],
             yerr=data_bes_rho1450['e'],
             fmt='bo',
             label=r'$\sigma$($\rho$(1450)$\pi$)')
if(1 == 0):
    axe.errorbar(data_bes_rho770['x'],
                 data_bes_rho770['y'],
                 yerr=data_bes_rho770['e'],
                 fmt='ro',
                 label=r'$\sigma$($\rho$(770)$\pi$)')

axe.legend(loc=1)
axe.set_xlabel(r'Energy (GeV)')
axe.set_ylabel(r'Born Cross Section (pb)')
#axe.set_title(r'Born Cross Section')
plt.xlim((2.0, 3.2))
plt.ylim((0, 120))
plt.savefig('opicture/lineshape/7_show_rho1450pi.pdf')
plt.savefig('opicture/lineshape/7_show_rho1450pi.png')
plt.show()
plt.close()
