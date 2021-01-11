# -*- coding: UTF-8 -*-
# Public package

# Private package
import headpy.hfile as hfile
import headpy.hscreen.hprint as hprint


def funcformat(*args):
    value = args[0]
    value = float(value)
    if(value == 0):
        output = '-'
    else:
        output = '%.4f' % (float(value))
    return output


nominal = hfile.pkl_read('../ppp_pwa/output_nominal/2.1250.pkl')
fraction = nominal.fraction

table = hprint.TABLE()
table.add_dict(fraction)
hprint.ppika()
table.ptable()
table.set_order(in_order1=['rho770pi', 'rho1450pi', 'rho1700pi', 'omega782pi', 'rho1690pi'],
                in_order2=['rho770pi', 'rho1450pi', 'rho1700pi', 'omega782pi', 'rho1690pi'])
table.set_format(funcformat)
table.platex()
