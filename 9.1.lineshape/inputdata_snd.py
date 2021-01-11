# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package
import headpy.hfile as hfile
################################################################################
# SND的1-2GeV的pi+pi-pi0截面
################################################################################
output = []
output.append([1.050, 1.27, 0.48, 0.26])
output.append([1.075, 3.30, 0.26, 0.40])
output.append([1.100, 4.27, 0.32, 0.34])
output.append([1.125, 4.64, 0.26, 0.32])
output.append([1.150, 5.24, 0.29, 0.31])
output.append([1.175, 5.42, 0.27, 0.24])
output.append([1.200, 5.13, 0.28, 0.23])
output.append([1.225, 5.80, 0.27, 0.26])
output.append([1.250, 6.00, 0.28, 0.26])
output.append([1.275, 5.55, 0.29, 0.24])

output.append([1.300, 4.92, 0.26, 0.22])
output.append([1.325, 4.91, 0.22, 0.22])
output.append([1.350, 5.02, 0.24, 0.22])
output.append([1.375, 4.81, 0.22, 0.21])
output.append([1.400, 4.18, 0.24, 0.18])
output.append([1.425, 4.06, 0.23, 0.18])
output.append([1.450, 4.10, 0.25, 0.18])
output.append([1.475, 4.30, 0.21, 0.19])
output.append([1.500, 4.44, 0.19, 0.20])
output.append([1.525, 4.52, 0.24, 0.20])

output.append([1.550, 4.63, 0.24, 0.20])
output.append([1.575, 4.71, 0.24, 0.21])
output.append([1.600, 5.81, 0.27, 0.26])
output.append([1.625, 5.06, 0.28, 0.22])
output.append([1.650, 4.65, 0.26, 0.20])
output.append([1.675, 3.42, 0.22, 0.15])
output.append([1.700, 2.61, 0.23, 0.12])
output.append([1.725, 2.15, 0.19, 0.09])
output.append([1.750, 1.80, 0.18, 0.08])
output.append([1.775, 1.62, 0.16, 0.07])

output.append([1.800, 1.05, 0.18, 0.05])
output.append([1.825, 1.28, 0.14, 0.06])
output.append([1.850, 1.28, 0.17, 0.06])
output.append([1.870, 0.92, 0.13, 0.04])
output.append([1.890, 0.68, 0.12, 0.03])
output.append([1.900, 1.04, 0.15, 0.05])
output.append([1.925, 0.66, 0.11, 0.03])
output.append([1.950, 0.51, 0.13, 0.02])
output.append([1.975, 0.69, 0.14, 0.03])
output.append([2.000, 0.84, 0.16, 0.04])
# print
output = numpy.array(output)
output = output.T
output[2] = (output[2]**2 + output[3]**2)**0.5
output = output[0:3, ]
output[1] *= 1000
output[2] *= 1000
hfile.pkl_dump('fdata/section_snd.pkl', output)
