# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package
import headpy.hfile as hfile
################################################################################
# SND的1-2GeV的pi+pi-pi0截面
################################################################################
output = []
# region part1
output.append([1.050, 0.98, 0.48, 0.34])
output.append([1.075, 3.07, 0.27, 0.67])
output.append([1.100, 3.96, 0.31, 0.58])
output.append([1.125, 4.52, 0.25, 0.28])
output.append([1.150, 5.13, 0.28, 0.26])
output.append([1.175, 5.29, 0.27, 0.23])
output.append([1.200, 5.07, 0.27, 0.22])
output.append([1.225, 5.72, 0.27, 0.25])
output.append([1.250, 5.93, 0.27, 0.25])
output.append([1.275, 5.50, 0.29, 0.24])
output.append([1.300, 4.87, 0.26, 0.21])
output.append([1.325, 4.86, 0.22, 0.21])
output.append([1.350, 4.97, 0.24, 0.21])
output.append([1.375, 4.75, 0.22, 0.20])
output.append([1.400, 4.12, 0.24, 0.18])
output.append([1.425, 3.99, 0.23, 0.17])
output.append([1.450, 4.04, 0.24, 0.17])
output.append([1.475, 4.25, 0.21, 0.18])
output.append([1.500, 4.39, 0.19, 0.19])
output.append([1.525, 4.47, 0.24, 0.19])
output.append([1.550, 4.58, 0.24, 0.20])
output.append([1.575, 4.66, 0.24, 0.20])
output.append([1.600, 5.73, 0.27, 0.25])
output.append([1.625, 5.03, 0.28, 0.22])
output.append([1.650, 4.64, 0.25, 0.20])
output.append([1.675, 3.45, 0.22, 0.15])
output.append([1.700, 2.65, 0.23, 0.11])
output.append([1.725, 2.18, 0.19, 0.09])
output.append([1.750, 1.85, 0.18, 0.08])
output.append([1.775, 1.66, 0.16, 0.07])
output.append([1.800, 1.08, 0.18, 0.05])
output.append([1.825, 1.31, 0.14, 0.06])
output.append([1.850, 1.30, 0.17, 0.06])
output.append([1.870, 0.93, 0.13, 0.04])
output.append([1.890, 0.68, 0.12, 0.03])
output.append([1.900, 1.03, 0.14, 0.04])
output.append([1.925, 0.65, 0.10, 0.03])
output.append([1.950, 0.49, 0.12, 0.02])
output.append([1.975, 0.66, 0.13, 0.03])
output.append([2.000, 0.81, 0.15, 0.03])
# endregion
# print
output = numpy.array(output)
output = output.T
# 转换系统，统计误差
output[2] = (output[2]**2 + output[3]**2)**0.5
output = output[0:3, ]
output[1] *= 1000
output[2] *= 1000
hfile.pkl_dump('fdata/section_snd.pkl', output)
