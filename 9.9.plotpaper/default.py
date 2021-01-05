# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package


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

