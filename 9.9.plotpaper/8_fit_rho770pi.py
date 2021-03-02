# -*- coding: UTF-8 -*-
# Public package
import numpy
import lmfit
import copy
# Private package
import ROOT
import default as default
import headpy.hbes.hstyle as hstyle
import headpy.hbes.hfunc as hfunc

################################################################################
# 拟合并绘制BES的结果
################################################################################


data = default.data_bes_pppmpz_fraction('rho770pi')
data = default.delete_point(data, [2.5, 2.7, 2.8])
print(len(data['x']))

x = data['x']
y = data['y']
e = data['e']
ue = copy.deepcopy(e)


def my_function(e, mr, wr, b, phase,
                p1, p2, p3):
    output = hfunc.snd_line_shape_rho770pi(e, mr, wr, b, phase,
                                           p1, p2, p3)
    return output


def func(p):
    output = (my_function(x,
                          p['mr'], p['wr'], p['b'], p['phase'],
                          p['p1'], p['p2'], p['p3']) - y) / 1
    return output


p = lmfit.Parameters()
p.add(name='mr', value=2.2, min=2.0, max=2.5)
p.add(name='wr', value=0.15, min=0.01, max=0.2)
p.add(name='b', value=10.0, min=0.01, max=100.0)
p.add(name='phase', value=0.0, min=-20.0, max=20.0)
p.add(name='p1', value=1000000000.0, min=0.0, max=1000000000.0)
p.add(name='p2', value=7.09268368, min=-100.0, max=100.0)
p.add(name='p3', value=-8.32936732, min=-100.0, max=100.0)
mi = lmfit.minimize(func, params=p, method='leastsq')
lmfit.printfuncs.report_fit(mi.params, min_correl=0.5)

# 设定参数
filename = 'lineshape/8_fit_rho770pi.pdf'
xlim = (1.95, 3.1)
ylim = (0.0, 600)
steps = 0.001
# 读取数据
data_pppmpz = default.data_bes_pppmpz_fraction('rho770pi')
# 绘图
hstyle.set_style()
canvas = hstyle.get_canvas()
legendlist = []
if(1 == 1):
    len_bes_opp = len(data_pppmpz['x'])
    tgraph_bes_opp = ROOT.TGraphAsymmErrors(len_bes_opp)
    for i in range(len_bes_opp):
        #tgraph_bes_opp.SetPointX(i, data_pppmpz['x'][i])
        #tgraph_bes_opp.SetPointY(i, data_pppmpz['y'][i])
        tgraph_bes_opp.SetPoint(i, data_pppmpz['x'][i], data_pppmpz['y'][i])
        tgraph_bes_opp.SetPointEXlow(i, 0.0)
        tgraph_bes_opp.SetPointEXhigh(i, 0.0)
        tgraph_bes_opp.SetPointEYlow(i, data_pppmpz['e'][i])
        tgraph_bes_opp.SetPointEYhigh(i, data_pppmpz['e'][i])
    hstyle.set_axis(tgraph_bes_opp, r'#sqrt{s} (GeV)', r'Cross Section (pb)')
    tgraph_bes_opp.GetXaxis().SetRangeUser(xlim[0], xlim[1])
    tgraph_bes_opp.GetYaxis().SetRangeUser(ylim[0], ylim[1])
    hstyle.set_hist_data(tgraph_bes_opp, style_code=1)
    tgraph_bes_opp.SetMarkerSize(1.2)
    legendlist.append([tgraph_bes_opp, r'Measurement', 'lp'])
    tgraph_bes_opp.Draw('AP')
if(1 == 1):
    data_fit = {}
    nx = numpy.arange(xlim[0], xlim[1], steps)
    ny = numpy.arange(xlim[0], xlim[1], steps)
    len_fit_opp = int((xlim[1] - xlim[0]) / steps)
    for i in range(len_fit_opp):
        ny[i] = my_function(nx[i],
                            mi.params['mr'].value,
                            mi.params['wr'].value,
                            mi.params['b'].value,
                            mi.params['phase'].value,
                            mi.params['p1'].value,
                            mi.params['p2'].value,
                            mi.params['p3'].value)
    data_fit['x'] = nx
    data_fit['y'] = ny
    tgraph_fit_opp = ROOT.TGraph(len_fit_opp)
    for i in range(len_fit_opp):
        tgraph_fit_opp.SetPoint(i, data_fit['x'][i], data_fit['y'][i])
    tgraph_fit_opp.SetLineColor(hstyle.style_color[2])
    tgraph_fit_opp.SetLineWidth(3)
    tgraph_fit_opp.SetLineStyle(1)
    legendlist.append([tgraph_fit_opp, r'Fitting', 'l'])
    tgraph_fit_opp.Draw('Lsame')
if(1 == 1):
    data_fit_opp_r = {}
    nx = numpy.arange(xlim[0], xlim[1], steps)
    ny = numpy.arange(xlim[0], xlim[1], steps)
    len_fit_opp_r = int((xlim[1] - xlim[0]) / steps)
    for i in range(len_fit_opp_r):
        ny[i] = my_function(nx[i],
                            mi.params['mr'].value,
                            mi.params['wr'].value,
                            mi.params['b'].value,
                            mi.params['phase'].value,
                            0.0,
                            mi.params['p2'].value,
                            mi.params['p3'].value)
    data_fit_opp_r['x'] = nx
    data_fit_opp_r['y'] = ny
    tgraph_fit_opp_r = ROOT.TGraph(len_fit_opp_r)
    for i in range(len_fit_opp_r):
        tgraph_fit_opp_r.SetPoint(i, data_fit_opp_r['x'][i], data_fit_opp_r['y'][i])
    tgraph_fit_opp_r.SetLineColor(hstyle.style_color[3])
    tgraph_fit_opp_r.SetLineWidth(3)
    tgraph_fit_opp_r.SetLineStyle(2)
    legendlist.append([tgraph_fit_opp_r, r'Resonance', 'l'])
    tgraph_fit_opp_r.Draw('Lsame')
if(1 == 1):
    data_fit_opp_n = {}
    nx = numpy.arange(xlim[0], xlim[1], steps)
    ny = numpy.arange(xlim[0], xlim[1], steps)
    len_fit_opp_n = int((xlim[1] - xlim[0]) / steps)
    for i in range(len_fit_opp_n):
        ny[i] = my_function(nx[i],
                            mi.params['mr'].value,
                            mi.params['wr'].value,
                            0.0,
                            mi.params['phase'].value,
                            mi.params['p1'].value,
                            mi.params['p2'].value,
                            mi.params['p3'].value)
    data_fit_opp_n['x'] = nx
    data_fit_opp_n['y'] = ny
    tgraph_fit_opp_n = ROOT.TGraph(len_fit_opp_n)
    for i in range(len_fit_opp_n):
        tgraph_fit_opp_n.SetPoint(i, data_fit_opp_n['x'][i], data_fit_opp_n['y'][i])
    tgraph_fit_opp_n.SetLineColor(hstyle.style_color[4])
    tgraph_fit_opp_n.SetLineWidth(3)
    tgraph_fit_opp_n.SetLineStyle(3)
    legendlist.append([tgraph_fit_opp_n, r'Continum', 'l'])
    tgraph_fit_opp_n.Draw('Lsame')
tgraph_bes_opp.Draw('Psame')
drawlist = []
legend = hstyle.get_legend(legendlist,
                           d=0.75, l=0.65)
drawlist.append(legend)
for i in drawlist:
    i.Draw('same')
canvas.Update()
canvas.Print('opicture/%s' % (filename))
canvas.Print('opicture/%s' % (filename.replace('.pdf', '.jpg')))
input()
