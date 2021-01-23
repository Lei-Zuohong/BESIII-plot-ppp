# -*- coding: UTF-8 -*-
# Public package
import math
import numpy
# Private package
import default as default

#
data_bes_pppmpz = default.data_bes_pppmpz()
data_babar = default.data_babar_pppmpz()
data_snd = default.data_snd_pppmpz()
data_beslow = default.data_beslow_pppmpz()

data_rhopi_snd = default.data_snd_rhopi()
data_rhopi_bes = default.data_bes_pppmpz_fraction('rho770pi')
#
data_use = data_rhopi_snd
#
length = len(data_use['x'])
print(length)
if(1 == 1):
    output = ''
    output += '{'
    for count, i in enumerate(data_use['x']):
        if(count == length - 1):
            output += '%f' % (i)
        else:
            output += '%f,' % (i)
        if(count % 5 == 4):
            output += '\n'
    output += '}'
    print(output)
if(1 == 1):
    output = ''
    output += '{'
    for count in range(length):
        if(count == length - 1):
            output += '%f' % (0.0)
        else:
            output += '%f,' % (0.0)
        if(count % 5 == 4):
            output += '\n'
    output += '}'
    print(output)
if(1 == 1):
    output = ''
    output += '{'
    for count, i in enumerate(data_use['y']):
        if(count == length - 1):
            output += '%f' % (i)
        else:
            output += '%f,' % (i)
        if(count % 5 == 4):
            output += '\n'
    output += '}'
    print(output)
if(1 == 1):
    output = ''
    output += '{'
    for count, i in enumerate(data_use['e']):
        if(count == length - 1):
            output += '%f' % (i)
        else:
            output += '%f,' % (i)
        if(count % 5 == 4):
            output += '\n'
    output += '}'
    print(output)
