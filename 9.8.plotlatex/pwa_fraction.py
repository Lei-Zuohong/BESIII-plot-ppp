# -*- coding: UTF-8 -*-
# Public package

# Private package
import headpy.hfile as hfile
import headpy.hbes.hppp as hppp
import headpy.hscreen.hprint as hprint

energy_sort = hppp.energy_sort()


def format_energy(*argv):
    output = '%1.4f' % (argv[0])
    return output


def format_value(*argv):
    try:
        output = '%1.2f' % (float(argv[0]))
    except:
        print(argv[0])
    return output


def format_value_3(*argv):
    try:
        output = '%1.3f' % (float(argv[0]))
    except:
        print(argv[0])
    return output


dict_fraction = {}
for energy in energy_sort:
    #
    dict_fraction[energy] = {}

    data = hfile.pkl_read('../ppp_pwa/output_nominal/%1.4f.pkl' % (energy))
    error_rho770pi = hfile.pkl_read('../ppp_pwa/fdata_error/sta_fraction_rho770pi/%1.4f.pkl' % (energy))
    error_rho1450pi = hfile.pkl_read('../ppp_pwa/fdata_error/sta_fraction_rho1450pi/%1.4f.pkl' % (energy))
    error_omega782pi = hfile.pkl_read('../ppp_pwa/fdata_error/sta_fraction_omega782pi/%1.4f.pkl' % (energy))

    fraction = data.fraction
    dict_fraction[energy]['Rho'] = '%.3f +- %.3f' % (fraction['rho770pi']['rho770pi'],
                                                     fraction['rho770pi']['rho770pi'] * error_rho770pi)
    dict_fraction[energy]['Rho1450'] = '%.3f +- %.3f' % (fraction['rho1450pi']['rho1450pi'],
                                                         fraction['rho1450pi']['rho1450pi'] * error_rho1450pi)
    dict_fraction[energy]['Rho1450-Rho'] = '%.3f' % (fraction['rho1450pi']['rho770pi'] + fraction['rho770pi']['rho1450pi'])
    dict_fraction[energy]['Omega'] = '%.3f +- %.3f' % (fraction['omega782pi']['omega782pi'],
                                                       fraction['omega782pi']['omega782pi'] * error_omega782pi)
    #
    table_energy = hprint.TABLE()
    table_energy.add_dict(fraction)
    table_energy.set_order(['rho770pi', 'rho1450pi', 'rho1700pi', 'omega782pi', 'rho1690pi'],
                           ['rho770pi', 'rho1450pi', 'rho1700pi', 'omega782pi', 'rho1690pi'])
    table_energy.set_format(format_value_3)
    table_energy.ptable()
table = hprint.TABLE()
table.add_dict(dict_fraction, key1='Energy')
table.set_format(format_energy, list2=['Energy'])
#table.set_format(format_value, list2=['Rho', 'Rho1450', 'Rho1450-Rho', 'Omega'])
table.set_order([], ['Rho', 'Rho1450', 'Rho1450-Rho', 'Omega'])
table.ptable()
