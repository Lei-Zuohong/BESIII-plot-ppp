# -*- coding: UTF-8 -*-
# Public package
import re
import os
# Private package

################################################################################
# 读取产生子，得到scale因子的截面值
################################################################################

data_30800 = 0.0
data_21000 = 0.0
data_21500 = 0.0
data_23960 = 0.0
data_29000 = 0.0

filelist = os.listdir('inclusive')
for file in filelist:
    with open('inclusive/%s' % (file), 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            check = re.match(r'(.*)  (.*)  (.*)', line)
            if(check):
                if(int(check.group(1)) == 21000):
                    data_21000 += float(check.group(2))
                if(int(check.group(1)) == 21500):
                    data_21500 += float(check.group(2))
                if(int(check.group(1)) == 30800):
                    data_30800 += float(check.group(2))
                if(int(check.group(1)) == 23960):
                    data_23960 += float(check.group(2))
                if(int(check.group(1)) == 29000):
                    data_29000 += float(check.group(2))
                
print('2.1250'),
print((data_21000+data_21500)/2)
print('2.3960'),
print(data_23960)
print('2.9000'),
print(data_29000)
print('3.0800'),
print(data_30800)
