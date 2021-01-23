# -*- coding: UTF-8 -*-
# Public package
import numpy
import matplotlib.pyplot as plt
# Private package
import headpy.hplot.hplt as hplt


def aveg(a, b):
    output = (a**2 + b**2)**0.5
    return output


def rho_2150_parameter():
    output = []
    # ee part
    output.append([2201, 19, 19, 70, 38, 38, 'ee', 'kkg'])
    output.append([2227, aveg(9, 9), aveg(9, 9), 127, aveg(14, 4), aveg(14, 4), 'ee', 'kk_l'])
    output.append([2039, aveg(8, 36), aveg(8, 18), 196, aveg(23, 25), aveg(23, 27), 'ee', 'kkpi'])
    output.append([2239.2, aveg(7.1, 11.3), aveg(7.1, 11.3), 139.8, aveg(12.3, 20.6), aveg(12.3, 20.6), 'ee', 'kk_a'])
    output.append([2254, 22, 22, 109, 76, 76, 'ee', 'pipig'])
    output.append([2150, aveg(40, 50), aveg(40, 50), 350, aveg(40, 50), aveg(40, 50), 'ee', 'fpipig'])
    output.append([1990, 80, 80, 310, 140, 140, 'ee', 'epipig'])
    output.append([2153, 37, 37, 389, 79, 79, 'ee', 'pipikk'])
    output.append([2110, 50, 50, 410, 100, 100, 'ee', '6pi'])
    # pp part
    output.append([2191, 0, 0, 296, 0, 0, 'pp', 'pp1'])
    output.append([2070, 0, 0, 40, 0, 0, 'pp', 'pp2'])
    output.append([2170, 0, 0, 250, 0, 0, 'pp', 'pp3'])
    output.append([2100, 0, 0, 200, 0, 0, 'pp', 'pp4'])
    # nn part
    output.append([2110, 35, 35, 230, 50, 50, 'nn', '3'])
    output.append([2155, 15, 15, 135, 75, 75, 'nn', 'pp'])
    output.append([2193, 2, 2, 98, 8, 8, 'nn', 'pps'])
    output.append([2190, 10, 10, 85, 0, 0, 'nn', 'spn'])
    # pip part
    output.append([2140, 30, 30, 320, 70, 70, 'pip', 'pip1'])
    output.append([2170, 30, 30, 300, 0, 0, 'pip', 'pip2'])
    return output


fig, ax = plt.subplots(1, 1, figsize=(8, 6))
datain = rho_2150_parameter()
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
#ax.set_title(r'$\rho(2150)$ mass and width', fontsize=fontsize)
ax.set_xlabel('Mass (MeV/$c^2$)', fontsize=fontsize)
ax.set_ylabel('Width (MeV)', fontsize=fontsize)
plt.savefig('opicture/cite/1_rhomwidth.pdf')
plt.savefig('opicture/cite/1_rhomwidth.png')
plt.show()
