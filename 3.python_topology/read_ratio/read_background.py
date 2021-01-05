# -*- coding: UTF-8 -*-
# Public package
import re
# Private package

output = {}
with open('back/ObsCroSec.lst') as infile:
    lines = infile.readlines()
for line in lines:
    method = r'(\S*)\s*(\S*)\s*(\S*)\s*(\S*).*\n'
    check = re.match(method, line)
    if(check):
        energy = float(check.group(1))
        section1 = float(check.group(2))
        section2 = float(check.group(3))
        section3 = float(check.group(4))
        output[energy] = {}
        output[energy]['001'] = section1
        output[energy]['002'] = section2
        output[energy]['003'] = section3

print('2.1250:')
print((output[2.1000]['001']+output[2.1500]['001'])/2)
print((output[2.1000]['002']+output[2.1500]['002'])/2)
print((output[2.1000]['003']+output[2.1500]['003'])/2)
print('')
print('2.3960:')
print(output[2.3960]['001'])
print(output[2.3960]['002'])
print(output[2.3960]['003'])
print('')
print('2.9000:')
print(output[2.9000]['001'])
print(output[2.9000]['002'])
print(output[2.9000]['003'])
print('')
print('3.0800:')
print(output[3.0800]['001'])
print(output[3.0800]['002'])
print(output[3.0800]['003'])
print('')