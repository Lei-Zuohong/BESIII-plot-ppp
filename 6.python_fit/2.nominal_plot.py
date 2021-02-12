# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package
import default as default
import headpy.hfile as hfile
import headpy.hbes.hfit as hfit
import headpy.hbes.hnew as hnew
import headpy.hbes.hppp as hppp
import headpy.hmath.hstatis as hstatis


parameter_gmean = hstatis.PARAMETER(name='gmean', value=0.0, error=1.0, limitl=-0.01, limitr=0.01)
parameter_gmean.set_gen_range(0.0, 0.001)
parameter_gsigm = hstatis.PARAMETER(name='gsigm', value=0.00001, error=1.0, limitl=0.0, limitr=0.005)
parameter_gsigm.set_gen_range(0.0, 0.0001)
parameter_npdf1 = hstatis.PARAMETER(name='npdf1', value=500.0, error=1.0, limitl=0.0, limitr=20000.0)
parameter_npdf1.set_gen_range(0.0, 1000.0)
parameter_npdf2 = hstatis.PARAMETER(name='npdf2', value=10.0, error=1.0, limitl=0.0, limitr=10000.0)
parameter_npdf2.set_gen_range(0.0, 500.0)
parameter_p0 = hstatis.PARAMETER(name='p0', value=0.1, error=1.0, limitl=-1000.0, limitr=1000.0)
parameter_p0.set_gen_range(-1.0, 1.0)
parameter_p1 = hstatis.PARAMETER(name='p1', value=0.1, error=1.0, limitl=-1000.0, limitr=1000.0)
parameter_p1.set_gen_range(-1.0, 1.0)
parameter_p2 = hstatis.PARAMETER(name='p2', value=0.1, error=1.0, limitl=-1000.0, limitr=1000.0)
parameter_p2.set_gen_range(-1.0, 1.0)
parameter_p3 = hstatis.PARAMETER(name='p3', value=0.1, error=1.0, limitl=-1000.0, limitr=1000.0)
parameter_p3.set_gen_range(-1.0, 1.0)

parameters = hstatis.PARAMETERS()
parameters.add(parameter_gmean)
parameters.add(parameter_gsigm)
parameters.add(parameter_npdf1)
parameters.add(parameter_npdf2)
parameters.add(parameter_p0)
parameters.add(parameter_p1)
parameters.add(parameter_p2)
parameters.add(parameter_p3)

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
