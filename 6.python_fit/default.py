# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package
import headpy.hfile as hfile
import headpy.hbes.hnew as hnew
import headpy.hbes.hppp as hppp


def dump(**argv):
    # 打开参数
    energy = argv['energy']
    # 读取数据
    massages = hnew.massage_read()
    trees = hnew.trees_read(energy=energy,
                            tree='fit4c',
                            read=['real', 'pppmpz'])
    selecters = hppp.selecters()
    selecters['piz_m'].set_width(0.045)
    selecters['piz_m'].set_width_show(0.045)
    # 初始化数据
    alldata = hnew.ALLDATA(trees=trees,
                           selecters=selecters,
                           massages=massages)
    myweight = hfile.pkl_read('../ppp_pwa/root_fit4c/%1.4f_weight.pkl' % (energy))
    alldata.trees['pppmpz']['pwa_weight'] = numpy.array(myweight)
    namef = {}
    nameh = {}
    docuts = ['pip_ep', 'pim_ep', 'pip_pid_pi', 'pim_pid_pi',
              'chisq',
              'a_pippim',
              'gamma1_heli', 'gamma2_heli',
              'piz_m']
    namef['r'], nameh['r'] = alldata.tree(data='real',
                                          branch='piz_m',
                                          docuts=docuts,
                                          name='fit_real')
    namef['m'], nameh['m'] = alldata.hist(data='pppmpz',
                                          branchs=['piz_m'],
                                          docuts=docuts,
                                          doweight=['pwa_weight'],
                                          name='fit_pppmpz')
    return namef, nameh


def set_parameter(init, left_init, right_init, left, right):
    output = {}
    output['init'] = init
    output['left_init'] = left_init
    output['right_init'] = right_init
    output['left'] = left
    output['right'] = right
    return output
