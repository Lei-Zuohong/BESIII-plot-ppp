# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
# Private package
import default
import headpy.hplot.hmatplotlib as hplt


pdf = PdfPages('9.9.plotpaper/1_rhomwidth.pdf')
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
datain = default.rho_2150_parameter()
legendobject = []
for i in datain:
    if(i[6] == 'ee'):
        color = 'r'
        marker = '.'
        linestyle = '-'
        label = r'$e^+e^-$'
    if(i[6] == 'pp'):
        color = 'g'
        marker = '^'
        linestyle = '-'
        label = r'$p\bar{p}$'
    if(i[6] == 'nn'):
        color = 'b'
        marker = 'v'
        linestyle = '-'
        label = r'S-channel $N\bar{N}$'
    if(i[6] == 'pip'):
        color = 'y'
        marker = '*'
        linestyle = '-'
        label = r'$\pi^- p$'
    objects = hplt.plt_scatter_errorbar(ax,
                                        x=i[0], xr=i[1], xl=i[2],
                                        y=i[3], yr=i[4], yl=i[5],
                                        color=color,
                                        marker=marker,
                                        markersize=150,
                                        linestyle=linestyle,
                                        label=label)
    legendobject.append(objects['p'])
fontsize = 15
ax.legend(handles=[legendobject[0], legendobject[9], legendobject[13], legendobject[17]],
          loc=1, fontsize=fontsize)
ax.set_title(r'$\rho(2150)$ mass and width', fontsize=fontsize)
ax.set_xlabel('Mass (MeV/$c^2$)', fontsize=fontsize)
ax.set_ylabel('Width (MeV)', fontsize=fontsize)
pdf.savefig()
plt.show()
pdf.close()
