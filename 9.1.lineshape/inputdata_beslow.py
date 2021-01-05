# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package
import headpy.hfile as hfile
################################################################################
# BESIII的pi+pi-pi0的isr截面
################################################################################
datas = [[0.70125, 1.21, 2.23, 0.04],
         [0.88375, 13.19, 4.00, 0.50],
         [1.21250, 7.094, 0.715, 0.084],
         [0.70375, -1.74, 2.54, 0.13],
         [0.88625, 6.61, 3.40, 0.30],
         [1.23750, 6.143, 0.664, 0.102],
         [0.70625, 0.92, 3.03, 0.03],
         [0.88875, 5.98, 3.29, 0.14],
         [1.26250, 6.345, 0.634, 0.113],
         [0.70875, -0.23, 3.43, 0.02],
         [0.89125, 13.07, 4.24, 0.46],
         [1.28750, 6.336, 0.605, 0.088],
         [0.71125, 2.19, 3.61, 0.07],
         [0.89375, 14.43, 4.08, 0.30],
         [1.31250, 6.008, 0.539, 0.066],
         [0.71375, 10.46, 4.88, 0.24],
         [0.89625, 13.31, 3.83, 0.23],
         [1.33750, 5.670, 0.526, 0.062],
         [0.71625, 0.34, 3.54, 0.03],
         [0.89875, 12.31, 3.81, 0.20],
         [1.36250, 5.599, 0.468, 0.056],
         [0.71875, -0.39, 4.17, 0.03],
         [0.90125, 10.20, 3.86, 0.18],
         [1.38750, 5.565, 0.450, 0.069],
         [0.72125, 11.09, 5.55, 0.17],
         [0.90375, 12.48, 3.73, 0.40],
         [1.41250, 4.996, 0.411, 0.057],
         [0.72375, 1.77, 5.48, 0.03],
         [0.90625, 9.16, 3.96, 0.19],
         [1.43750, 4.571, 0.382, 0.050],
         [0.72625, 9.55, 4.24, 0.16],
         [0.90875, 12.89, 3.93, 0.28],
         [1.46250, 4.593, 0.353, 0.051],
         [0.72875, 9.18, 5.06, 0.25],
         [0.91125, 11.34, 4.65, 0.19],
         [1.48750, 4.084, 0.339, 0.047],
         [0.73125, 12.10, 4.31, 0.23],
         [0.91375, 7.53, 3.44, 0.19],
         [1.51250, 4.536, 0.315, 0.047],
         [0.73375, 3.31, 5.25, 0.09],
         [0.91625, 8.76, 3.62, 0.30],
         [1.53750, 4.808, 0.308, 0.049],
         [0.73625, 2.86, 3.36, 0.06],
         [0.91875, 11.57, 3.54, 0.58],
         [1.56250, 4.792, 0.292, 0.052],
         [0.73875, 11.63, 6.28, 0.25],
         [0.92125, 13.42, 3.48, 0.59],
         [1.58750, 5.660, 0.296, 0.065],
         [0.74125, 16.15, 5.14, 0.25],
         [0.92375, 4.68, 4.52, 0.16],
         [1.61250, 5.556, 0.308, 0.056],
         [0.74375, 13.34, 5.36, 0.20],
         [0.92625, 9.79, 3.24, 0.26],
         [1.63750, 5.385, 0.262, 0.062],
         [0.74625, 15.84, 5.49, 0.22],
         [0.92875, 10.35, 3.58, 0.18],
         [1.66250, 4.419, 0.234, 0.051],
         [0.74875, 15.72, 5.94, 0.25],
         [0.93125, 8.99, 3.24, 0.15],
         [1.68750, 3.018, 0.185, 0.035],
         [0.75125, 17.73, 6.28, 0.28],
         [0.93375, 10.88, 3.47, 0.17],
         [1.71250, 2.082, 0.154, 0.023],
         [0.75375, 16.55, 6.74, 0.28],
         [0.93625, 7.94, 3.60, 0.12],
         [1.73750, 1.829, 0.153, 0.021],
         [0.75625, 38.82, 8.67, 0.71],
         [0.93875, 4.28, 3.84, 0.06],
         [1.76250, 1.735, 0.147, 0.024],
         [0.75875, 23.17, 7.64, 0.69],
         [0.94125, 9.43, 3.86, 0.13],
         [1.78750, 1.504, 0.127, 0.019],
         [0.76125, 40.70, 9.43, 1.45],
         [0.94375, 11.42, 3.73, 0.17],
         [1.81250, 1.353, 0.137, 0.015],
         [0.76375, 38.12, 9.77, 1.19],
         [0.94625, 14.04, 3.56, 0.22],
         [1.83750, 1.017, 0.110, 0.012],
         [0.76625, 62.43, 12.57, 1.52],
         [0.94875, 17.07, 3.80, 0.39],
         [1.86250, 1.048, 0.102, 0.012],
         [0.76875, 91.37, 13.84, 1.36],
         [0.95125, 7.66, 2.91, 0.19],
         [1.88750, 0.937, 0.094, 0.014],
         [0.77125, 157.25, 18.61, 3.02],
         [0.95375, 7.78, 3.24, 0.23],
         [1.91250, 0.763, 0.084, 0.012],
         [0.77375, 218.35, 22.42, 3.81],
         [0.95625, 10.42, 4.03, 0.31],
         [1.93750, 0.631, 0.077, 0.008],
         [0.77625, 415.56, 21.55, 7.64],
         [0.95875, 8.73, 3.29, 0.23],
         [1.96250, 0.506, 0.072, 0.006],
         [0.77875, 828.58, 27.72, 12.36],
         [0.96125, 7.55, 3.30, 0.32],
         [1.98750, 0.498, 0.069, 0.006],
         [0.78125, 1405.30, 31.05, 19.20],
         [0.96375, 11.41, 3.78, 0.75],
         [2.01250, 0.504, 0.067, 0.009],
         [0.78375, 1534.34, 33.91, 21.67],
         [0.96625, 19.28, 4.34, 0.44],
         [2.03750, 0.432, 0.059, 0.005],
         [0.78625, 1084.16, 30.73, 14.85],
         [0.96875, 7.68, 4.17, 0.17],
         [2.06250, 0.421, 0.061, 0.005],
         [0.78875, 618.58, 25.64, 8.58],
         [0.97125, 18.63, 4.23, 0.33],
         [2.08750, 0.532, 0.070, 0.006],
         [0.79125, 399.32, 22.40, 5.70],
         [0.97375, 18.15, 4.10, 0.31],
         [2.11250, 0.420, 0.051, 0.006],
         [0.79375, 239.67, 18.35, 4.90],
         [0.97625, 19.52, 4.72, 0.48],
         [2.13750, 0.450, 0.056, 0.007],
         [0.79625, 184.05, 16.88, 5.21],
         [0.97875, 11.29, 3.92, 0.36],
         [2.16250, 0.371, 0.052, 0.005],
         [0.79875, 136.99, 13.93, 2.23],
         [0.98125, 12.31, 3.88, 0.38],
         [2.18750, 0.391, 0.046, 0.005],
         [0.80125, 122.17, 13.21, 1.88],
         [0.98375, 11.81, 3.79, 0.33],
         [2.21250, 0.318, 0.043, 0.004],
         [0.80375, 72.57, 10.83, 1.14],
         [0.98625, 15.00, 3.75, 0.73],
         [2.23750, 0.442, 0.050, 0.005],
         [0.80625, 62.03, 8.76, 1.39],
         [0.98875, 15.23, 4.57, 0.28],
         [2.26250, 0.325, 0.041, 0.006],
         [0.80875, 45.17, 7.05, 1.59],
         [0.99125, 15.75, 4.39, 0.37],
         [2.28750, 0.197, 0.031, 0.004],
         [0.81125, 49.85, 8.09, 1.78],
         [0.99375, 26.39, 4.98, 0.42],
         [2.31250, 0.194, 0.034, 0.002],
         [0.81375, 41.86, 7.36, 1.49],
         [0.99625, 24.52, 5.23, 0.62],
         [2.33750, 0.188, 0.028, 0.002],
         [0.81625, 25.44, 5.45, 0.83],
         [0.99875, 28.14, 5.91, 0.67],
         [2.36250, 0.271, 0.034, 0.003],
         [0.81875, 29.98, 6.48, 0.59],
         [1.00125, 29.94, 6.20, 0.61],
         [2.38750, 0.191, 0.029, 0.002],
         [0.82125, 31.12, 6.55, 0.50],
         [1.00375, 38.24, 7.00, 0.76],
         [2.41250, 0.193, 0.030, 0.006],
         [0.82375, 27.15, 6.33, 0.68],
         [1.00625, 50.52, 7.31, 1.48],
         [2.43750, 0.159, 0.025, 0.007],
         [0.82625, 23.82, 6.05, 0.39],
         [1.00875, 49.17, 8.35, 1.03],
         [2.46250, 0.183, 0.029, 0.003],
         [0.82875, 29.20, 6.16, 0.70],
         [1.01125, 69.59, 9.24, 2.35],
         [2.48750, 0.120, 0.021, 0.002],
         [0.83125, 10.64, 4.83, 0.29],
         [1.01375, 128.91, 11.25, 2.02],
         [2.51250, 0.108, 0.022, 0.001],
         [0.83375, 16.63, 4.95, 0.58],
         [1.01625, 302.66, 13.57, 4.12],
         [2.53750, 0.115, 0.020, 0.001],
         [0.83625, 13.95, 4.20, 0.42],
         [1.01875, 591.69, 14.57, 8.15],
         [2.56250, 0.127, 0.021, 0.002],
         [0.83875, 24.43, 5.53, 0.64],
         [1.02125, 297.73, 10.63, 4.60],
         [2.58750, 0.127, 0.019, 0.002],
         [0.84125, 27.35, 5.81, 0.71],
         [1.02375, 79.63, 8.74, 1.55],
         [2.61250, 0.094, 0.017, 0.001],
         [0.84375, 10.97, 4.17, 0.19],
         [1.02625, 18.47, 7.43, 0.54],
         [2.63750, 0.088, 0.017, 0.001],
         [0.84625, 20.91, 4.64, 0.35],
         [1.02875, 16.82, 6.38, 0.63],
         [2.66250, 0.102, 0.019, 0.001],
         [0.84875, 14.13, 4.53, 0.47],
         [1.03125, 4.53, 5.71, 0.37],
         [2.68750, 0.083, 0.017, 0.001],
         [0.85125, 15.34, 3.69, 0.46],
         [1.03375, -1.25, 3.81, 0.06],
         [2.71250, 0.089, 0.016, 0.001],
         [0.85375, 12.77, 4.08, 0.19],
         [1.03625, 7.48, 4.27, 0.29],
         [2.73750, 0.091, 0.017, 0.001],
         [0.85625, 10.81, 4.38, 0.59],
         [1.03875, 1.23, 3.28, 0.08],
         [2.76250, 0.070, 0.015, 0.001],
         [0.85875, 12.94, 4.96, 0.26],
         [1.04125, 2.68, 4.21, 0.09],
         [2.78750, 0.092, 0.014, 0.001],
         [0.86125, 20.54, 4.17, 0.65],
         [1.04375, 0.08, 2.46, 0.08],
         [2.81250, 0.067, 0.014, 0.001],
         [0.86375, 10.17, 4.31, 0.24],
         [1.04625, -0.90, 3.08, 0.17],
         [2.83750, 0.079, 0.015, 0.001],
         [0.86625, 11.80, 3.83, 0.28],
         [1.04875, 3.64, 2.87, 0.19],
         [2.86250, 0.074, 0.013, 0.001],
         [0.86875, 3.89, 3.85, 0.11],
         [1.06250, 3.351, 0.788, 0.070],
         [2.88750, 0.066, 0.012, 0.001],
         [0.87125, 18.25, 4.46, 0.65],
         [1.08750, 5.417, 0.815, 0.116],
         [2.91250, 0.048, 0.012, 0.002],
         [0.87375, 4.47, 3.37, 0.17],
         [1.11250, 4.889, 0.790, 0.071],
         [2.93750, 0.059, 0.012, 0.001],
         [0.87625, 6.48, 3.56, 0.20],
         [1.13750, 6.494, 0.810, 0.156],
         [2.96250, 0.059, 0.012, 0.001],
         [0.87875, 8.32, 3.64, 0.26],
         [1.16250, 5.106, 0.722, 0.088],
         [2.98750, 0.062, 0.012, 0.002],
         [0.88125, 7.30, 3.80, 0.30],
         [1.18750, 4.730, 0.698, 0.136]]
# 得到能量点排序
energy_data = {}
for data in datas:
    energy_data[data[0]] = [data[1], data[2], data[3]]
energy_list = energy_data.keys()
energy_list.sort()
# 输出矩阵
output = []
for i in energy_list:
    output.append([i, energy_data[i][0], energy_data[i][1], energy_data[i][2]])
# 转换统计，系统误差
output = numpy.array(output)
output = output.T
output[2] = (output[2]**2 + output[3]**2)**0.5
output = output[0:3, ]
output[1]*=1000
output[2]*=1000
#
hfile.pkl_dump('fdata/section_beslow.pkl', output)