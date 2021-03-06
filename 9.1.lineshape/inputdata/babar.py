# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package
import headpy.hfile as hfile
################################################################################
# BaBar的1-3GeV的pi+pi-pi0截面
################################################################################
output = []
output.append([1.0625, 1.61, 0.53])
output.append([1.0875, 3.68, 0.61])
output.append([1.1125, 4.35, 0.63])
output.append([1.1375, 4.96, 0.66])
output.append([1.1625, 4.17, 0.62])
output.append([1.1875, 5.31, 0.65])
output.append([1.2125, 5.19, 0.65])
output.append([1.2375, 6.69, 0.75])
output.append([1.2625, 6.11, 0.65])
output.append([1.2875, 4.88, 0.62])
output.append([1.3125, 6.75, 0.65])
output.append([1.3375, 3.54, 0.55])
output.append([1.3625, 4.85, 0.56])
output.append([1.3875, 4.01, 0.53])
output.append([1.4125, 4.36, 0.54])
output.append([1.4375, 3.31, 0.49])
output.append([1.4625, 4.36, 0.54])
output.append([1.4875, 3.93, 0.52])
output.append([1.5125, 4.60, 0.53])
output.append([1.5375, 3.83, 0.50])
output.append([1.5625, 5.69, 0.56])
output.append([1.5875, 5.39, 0.56])
output.append([1.6125, 6.24, 0.58])
output.append([1.6375, 5.33, 0.55])
output.append([1.6625, 4.84, 0.50])
output.append([1.6875, 2.52, 0.40])
output.append([1.7125, 2.32, 0.36])
output.append([1.7375, 1.42, 0.31])
output.append([1.7625, 1.63, 0.31])
output.append([1.7875, 1.38, 0.29])
output.append([1.8125, 1.14, 0.26])
output.append([1.8375, 0.99, 0.27])
output.append([1.8625, 1.35, 0.26])
output.append([1.8875, 1.04, 0.24])
output.append([1.9125, 0.80, 0.22])
output.append([1.9375, 0.83, 0.21])
output.append([1.9625, 0.64, 0.19])
output.append([1.9875, 0.30, 0.16])
output.append([2.0125, 0.60, 0.18])
output.append([2.0375, 0.41, 0.17])
output.append([2.0625, 0.43, 0.15])
output.append([2.0875, 0.61, 0.17])
output.append([2.1125, 0.52, 0.16])
output.append([2.1375, 0.44, 0.15])
output.append([2.1625, 0.54, 0.16])
output.append([2.1875, 0.43, 0.15])
output.append([2.2125, 0.36, 0.14])
output.append([2.2375, 0.26, 0.13])
output.append([2.2625, 0.39, 0.14])
output.append([2.2875, 0.36, 0.14])
output.append([2.3125, 0.39, 0.14])
output.append([2.3375, 0.09, 0.11])
output.append([2.3625, 0.46, 0.14])
output.append([2.3875, 0.15, 0.11])
output.append([2.4125, 0.37, 0.12])
output.append([2.4375, 0.32, 0.12])
output.append([2.4625, 0.14, 0.10])
output.append([2.4875, 0.26, 0.11])
output.append([2.5125, 0.24, 0.11])
output.append([2.5375, 0.11, 0.09])
output.append([2.5625, 0.24, 0.10])
output.append([2.5875, 0.05, 0.08])
output.append([2.6125, 0.30, 0.10])
output.append([2.6375, 0.08, 0.08])
output.append([2.6625, 0.18, 0.10])
output.append([2.6875, 0.07, 0.09])
output.append([2.7125, 0.12, 0.09])
output.append([2.7375, 0.03, 0.08])
output.append([2.7625, -0.01, 0.07])
output.append([2.7875, 0.00, 0.07])
output.append([2.8125, 0.17, 0.09])
output.append([2.8375, 0.05, 0.08])
output.append([2.8625, 0.08, 0.07])
output.append([2.8875, 0.08, 0.07])
output.append([2.9125, 0.08, 0.07])
output.append([2.9375, 0.26, 0.09])
output.append([2.9625, -0.01, 0.06])
output.append([2.9875, 0.20, 0.08])
# print
output = numpy.array(output)
output = output.T
output[1] *= 1000
output[2] *= 1000
hfile.pkl_dump('fdata/section_babar.pkl', output)
