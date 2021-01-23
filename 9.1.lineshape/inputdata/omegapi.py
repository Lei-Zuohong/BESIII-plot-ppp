# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package
import headpy.hfile as hfile
################################################################################
# BESIII直接测量omegapi0的截面
################################################################################
output = []
output.append([2.0000, 946, 28, 70])
output.append([2.0500, 1086, 52, 73])
output.append([2.1000, 1181, 28, 80])
output.append([2.1250, 1136, 9, 76])
output.append([2.1500, 1021, 52, 55])
output.append([2.1750, 914, 26, 59])
output.append([2.2000, 791, 21, 54])
output.append([2.2324, 659, 20, 43])
output.append([2.3094, 452, 13, 30])
output.append([2.3864, 366, 11, 26])
output.append([2.3960, 352, 6, 19])
output.append([2.5000, 247, 38, 18])
output.append([2.6444, 195, 6, 11])
output.append([2.6464, 184, 6, 12])
output.append([2.7000, 163, 30, 10])
output.append([2.8000, 101, 30, 7])
output.append([2.9000, 93.8, 2.4, 5.3])
output.append([2.9500, 89, 5.8, 5.2])
output.append([2.9810, 74, 5.5, 4.1])
output.append([3.0000, 76.1, 5.3, 4.1])
output.append([3.0200, 73.3, 5, 4.3])
output.append([3.0800, 61.8, 1.7, 4.1])
# print
output = numpy.array(output)
output = output.T
# 转换系统，统计误差
output[2] = (output[2]**2 + output[3]**2)**0.5
output = output[0:3, ]
hfile.pkl_dump('fdata/section_omegapi.pkl', output)
