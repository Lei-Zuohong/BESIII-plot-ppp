# -*- coding: UTF-8 -*-
# Public package
import numpy as numpy
import math
import re
# Private package
import headpy.hfile as hfile


def data_bes_pppmpz():
    data = hfile.pkl_read('fdata/4.section-00-01.pkl')
    x = []
    y = []
    e = []
    energy_list = data.keys()
    energy_list.sort()
    for energy in energy_list:
        if(energy in data):
            x.append(data[energy]['Energy'])
            y.append(data[energy]['Section'])
            e.append(data[energy]['eSection'])
    output = {}
    output['x'] = numpy.array(x)
    output['y'] = numpy.array(y)
    output['e'] = numpy.array(e)
    return output


def data_bes_pppmpz_fraction(wave):
    output = data_bes_pppmpz()
    for count, energy in enumerate(output['x']):
        result = hfile.pkl_read('../ppp_pwa/output_nominal/%1.4f.pkl' % (energy))
        fraction = result.fraction[wave][wave]
        branch = 1
        if(re.match(r'rho770(.*)', wave)): branch = 1
        if(re.match(r'omega782(.*)', wave)): branch = 0.0153
        output['y'][count] = output['y'][count] * fraction / branch
        output['e'][count] = output['e'][count] * fraction / branch
    return output


def data_babar_pppmpz():
    data = hfile.pkl_read('fdata/section_babar.pkl')
    output = {}
    output['x'] = data[0]
    output['y'] = data[1]
    output['e'] = data[2]
    return output


def data_snd_pppmpz():
    data = hfile.pkl_read('fdata/section_snd.pkl')
    output = {}
    output['x'] = data[0]
    output['y'] = data[1]
    output['e'] = data[2]
    return output


def data_snd_rhopi():
    data = hfile.pkl_read('fdata/section_snd_rhopi.pkl')
    output = {}
    output['x'] = data[0]
    output['y'] = data[1]
    output['e'] = data[2]
    return output


def data_beslow_pppmpz():
    data = hfile.pkl_read('fdata/section_beslow.pkl')
    output = {}
    output['x'] = data[0]
    output['y'] = data[1]
    output['e'] = data[2]
    return output


def data_bes_omegapi():
    data = hfile.pkl_read('fdata/section_omegapi.pkl')
    output = {}
    output['x'] = data[0]
    output['y'] = data[1]
    output['e'] = data[2]
    return output


def delete_point(data, points):
    x = []
    y = []
    e = []
    for count, i in enumerate(data['x']):
        if(i in points): continue
        x.append(data['x'][count])
        y.append(data['y'][count])
        e.append(data['e'][count])
    output = {}
    output['x'] = numpy.array(x)
    output['y'] = numpy.array(y)
    output['e'] = numpy.array(e)
    return output
