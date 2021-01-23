# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package
import headpy.hfile as hfile
################################################################################
# SND的rhopi截面
################################################################################
output = []
output.append([(1.15 + 1.18) / 2, 4.40, (0.48 + 0.26) / 2])
output.append([(1.20 + 1.23) / 2, 4.68, (0.32 + 0.24) / 2])
output.append([(1.25 + 1.30) / 2, 4.25, (0.22 + 0.15) / 2])
output.append([(1.32 + 1.38) / 2, 4.29, (0.18 + 0.22) / 2])
output.append([(1.42 + 1.48) / 2, 3.43, (0.25 + 0.28) / 2])
output.append([(1.50 + 1.55) / 2, 2.73, (0.23 + 0.23) / 2])
output.append([(1.57 + 1.60) / 2, 2.76, (0.28 + 0.29) / 2])
output.append([(1.65 + 1.68) / 2, 2.12, (0.22 + 0.23) / 2])
output.append([(1.70 + 1.72) / 2, 2.02, (0.26 + 0.26) / 2])
output.append([(1.75 + 1.78) / 2, 2.00, (0.24 + 0.25) / 2])
output.append([(1.80 + 1.85) / 2, 1.20, (0.20 + 0.24) / 2])
output.append([(1.87 + 1.90) / 2, 1.14, (0.11 + 0.15) / 2])
output.append([(1.92 + 1.94) / 2, 0.30, (0.12 + 0.11) / 2])
output.append([(1.96 + 2.00) / 2, 0.32, (0.10 + 0.10) / 2])
# print
output = numpy.array(output)
output = output.T
output[1] *= 1000
output[2] *= 1000
hfile.pkl_dump('fdata/section_snd_rhopi.pkl', output)
