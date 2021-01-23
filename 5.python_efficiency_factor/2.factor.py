# -*- coding: UTF-8 -*-
# Public pack
import re
import os
import sys
# Private pack
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp
import headpy.hbes.hnew as hnew
import headpy.hscreen.hprint as hprint


def getisr(energy, filelog):
    israll = 0
    vpfall = 0
    isrnum = 0
    vpfnum = 0
    method = r'(.*)_(.*).txt.bosslog'
    filelist = os.listdir(filelog)
    for i in filelist:
        check = re.match(method, i)
        if(check):
            if(float(check.group(1)) == energy):
                with open('%s/%s' % (filelog, i), 'r') as infile:
                    text = infile.read()
                methodisr = r'f_vacuum= sigma_obs/sigma_born\(s\)  = (.*)\+/-0'
                methodvpf = r'1/\|1-Pi\|\^2= (.*)'
                checkisr = re.search(methodisr, text)
                checkvpf = re.search(methodvpf, text)
                if(checkisr):
                    israll += float(checkisr.group(1))
                    isrnum += 1
                if(checkvpf):
                    vpfall += float(checkvpf.group(1))
                    vpfnum += 1
    factor = {}
    factor['isr'] = israll / isrnum
    factor['vpf'] = vpfall / vpfnum
    factor['isr'] = factor['isr'] / factor['vpf']
    hprint.ppoint('Energy', energy)
    hprint.ppoint('isr factor', factor['isr'])
    hprint.ppoint('vpf factor', factor['vpf'])
    hprint.pstar()
    return factor


######################################################
energy_sort = hppp.energy_sort()
massage = hnew.massage_read()
filelog = '/besfs5/groups/tauqcd/leizh/ppp/mc/sim/pppmpz-%s' % (massage['version'])
filepickle = '%s.pkl' % (massage['factor'])
######################################################
factor = {}
hprint.pstar()
for i in energy_sort:
    factor[i] = getisr(i, filelog)
hfile.pkl_dump(filepickle, factor)
