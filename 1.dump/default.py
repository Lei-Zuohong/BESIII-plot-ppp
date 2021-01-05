# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package
import ROOT

branchs_truth = ['gamma1_m', 'gamma1_p', 'gamma1_a',  # 'gamma1_pe', 'gamma1_px', 'gamma1_py', 'gamma1_pz',
                 'gamma2_m', 'gamma2_p', 'gamma2_a',  # 'gamma2_pe', 'gamma2_px', 'gamma2_py', 'gamma2_pz',
                 'pip_m', 'pip_p', 'pip_a', 'pip_pe', 'pip_px', 'pip_py', 'pip_pz',
                 'pim_m', 'pim_p', 'pim_a', 'pim_pe', 'pim_px', 'pim_py', 'pim_pz',
                 'piz_m', 'piz_p', 'piz_a', 'piz_pe', 'piz_px', 'piz_py', 'piz_pz',
                 'pipm_m', 'pipm_p', 'pipm_a',  # 'pipm_pe', 'pipm_px', 'pipm_py', 'pipm_pz',
                 'pipz_m', 'pipz_p', 'pipz_a',  # 'pipz_pe', 'pipz_px', 'pipz_py', 'pipz_pz',
                 'pimz_m', 'pimz_p', 'pimz_a',  # 'pimz_pe', 'pimz_px', 'pimz_py', 'pimz_pz',
                 'is_isr'
                 ]

branchs_fit4c = ['flag2',
                 'flag3',

                 'pip_ep',
                 'pim_ep',
                 'pip_pid_pi',
                 'pim_pid_pi',
                 'pip_pid_e',
                 'pim_pid_e',
                 'pip_pid_mu',
                 'pim_pid_mu',

                 'ngamma',
                 'vertex',
                 'chisq',

                 'a_pippim',
                 'b_pippim',
                 'gamma1_heli',
                 'gamma2_heli',

                 'gamma1_m', 'gamma1_p', 'gamma1_a',  # 'gamma1_pe', 'gamma1_px', 'gamma1_py', 'gamma1_pz',
                 'gamma2_m', 'gamma2_p', 'gamma2_a',  # 'gamma2_pe', 'gamma2_px', 'gamma2_py', 'gamma2_pz',
                 'pip_m', 'pip_p', 'pip_a', 'pip_pe', 'pip_px', 'pip_py', 'pip_pz',
                 'pim_m', 'pim_p', 'pim_a', 'pim_pe', 'pim_px', 'pim_py', 'pim_pz',
                 'piz_m', 'piz_p', 'piz_a', 'piz_pe', 'piz_px', 'piz_py', 'piz_pz',
                 'pipm_m', 'pipm_p', 'pipm_a',  # 'pipm_pe', 'pipm_px', 'pipm_py', 'pipm_pz',
                 'pipz_m', 'pipz_p', 'pipz_a',  # 'pipz_pe', 'pipz_px', 'pipz_py', 'pipz_pz',
                 'pimz_m', 'pimz_p', 'pimz_a',  # 'pimz_pe', 'pimz_px', 'pimz_py', 'pimz_pz',

                 'dalitz_pm',
                 'dalitz_pz',
                 'dalitz_mz',
                 ]

branchs_fit4c_truth = branchs_fit4c + [
    't_pip_m', 't_pip_p', 't_pip_a', 't_pip_pe', 't_pip_px', 't_pip_py', 't_pip_pz',
    't_pim_m', 't_pim_p', 't_pim_a', 't_pim_pe', 't_pim_px', 't_pim_py', 't_pim_pz',
    't_gamma1_m', 't_gamma1_p', 't_gamma1_a',  # 't_gamma1_pe', 't_gamma1_px', 't_gamma1_py', 't_gamma1_pz',
    't_gamma2_m', 't_gamma2_p', 't_gamma2_a',  # 't_gamma2_pe', 't_gamma2_px', 't_gamma2_py', 't_gamma2_pz',
    't_piz_m', 't_piz_p', 't_piz_a', 't_piz_pe', 't_piz_px', 't_piz_py', 't_piz_pz',
    't_pipm_m', 't_pipm_p', 't_pipm_a',  # 't_pipm_pe', 't_pipm_px', 't_pipm_py', 't_pipm_pz',
    't_pipz_m', 't_pipz_p', 't_pipz_a',  # 't_pipz_pe', 't_pipz_px', 't_pipz_py', 't_pipz_pz',
    't_pimz_m', 't_pimz_p', 't_pimz_a',  # 't_pimz_pe', 't_pimz_px', 't_pimz_py', 't_pimz_pz'
    't_is_isr'
]


def root_dict(**kwargs):
    # 读取root文件
    tfile = ROOT.TFile(kwargs['file_root'])
    ttree = tfile.Get(kwargs['tree'])
    num = ttree.GetEntries()
    # 初始化输出字典
    output = {}
    for branch in kwargs['branchs']:
        output[branch] = []
    # 输入字典
    for entry in range(num):
        ttree.GetEntry(entry)
        if(kwargs['tree_cut'] == 1):
            ############################################################
            ####################选择条件#################################
            if(hasattr(ttree, 'pip_ep')):
                if(ttree.pip_ep > 1.2): continue
            if(hasattr(ttree, 'pim_ep')):
                if(ttree.pim_ep > 1.2): continue
            if(hasattr(ttree, 'piz_m')):
                if(abs(ttree.piz_m - 0.135) > 0.60): continue
            if(hasattr(ttree, 'chisq')):
                if(ttree.chisq > 200): continue
            ############################################################
        for branch in kwargs['branchs']:
            exec("output[branch].append(ttree.%s)" % (branch))
    # 输出字典
    for branch in kwargs['branchs']:
        output[branch] = numpy.array(output[branch])
    return output
