# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package
import default as default
import headpy.hfile as hfile
import headpy.hbes.hfit as hfit
import headpy.hbes.hnew as hnew
import headpy.hbes.hppp as hppp


parameters = {}
parameters['gmean'] = default.set_parameter(0.0, 0.0, 0.001, -0.01, 0.01)
parameters['gsigm'] = default.set_parameter(0.00001, 0.0, 0.0001, 0.0, 0.005)
parameters['npdf1'] = default.set_parameter(500.0, 0.0, 1000.0, 0.0, 20000.0)
parameters['npdf2'] = default.set_parameter(50.0, 0.0, 500.0, 0.0, 10000.0)
parameters['p0'] = default.set_parameter(0.1, -1.0, 1.0, -1000.0, 1000.0)
parameters['p1'] = default.set_parameter(0.1, -1.0, 1.0, -1000.0, 1000.0)
parameters['p2'] = default.set_parameter(0.1, -1.0, 1.0, -1000.0, 1000.0)
parameters['p3'] = default.set_parameter(0.1, -1.0, 1.0, -1000.0, 1000.0)

output = {}
for energy in hppp.energy_sort():
    # if(energy != 2.125): continue
    # 建立fit
    myfit = hfit.MYFIT()
    # 设定能量参数
    argv = {}
    argv['energy'] = energy
    # 设定拟合参数
    argv['backfunction'] = 'd2polynomial'
    argv['signfunction'] = 'evolution'
    argv['selecters'] = hppp.selecters()
    argv['selecters']['piz_m'].set_width(0.045)
    argv['selecters']['piz_m'].set_width_show(0.045)
    argv['branch'] = 'piz_m'
    argv['pictures'] = []
    # 设定fit参数
    argv['spread_times'] = 1
    argv['func_fit'] = hfit.dofit
    myfit.path_temp = '/besfs5/users/leizh/ftemp/fitplot'
    myfit.script = '6.python_fit/script/normal.py'
    # 输入参数拟合
    myfit.do_dump(default.dump, **argv)
    myfit.set_parameters(parameters)
    myfit.set_best_parameters(hfile.pkl_read('6.python_fit/output/%1.4f_best_parameters.pkl' % (energy)))
    argv['pictures'] = ['picture/3_fitting/%05d.jpg' % (10000 * energy),
                        'picture/3_fitting/%05d.pdf' % (10000 * energy)]
    argv['picture_xtitle'], argv['picture_ytitle'] = argv['selecters']['piz_m'].get_title()
    argv['picture_stop'] = ''
    fit_data = myfit.do_fit_plot(**argv)
    # 返回结果
    output[energy] = {}
    output[energy]['nevent'] = fit_data['nevent']
    output[energy]['enevent'] = fit_data['enevent']
print(output)

massages = hnew.massage_read()
hfile.pkl_dump('%s.pkl' % (massages['nevent']), output)
