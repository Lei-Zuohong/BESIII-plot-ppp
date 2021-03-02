# -*- coding: UTF-8 -*-
# Public package
import numpy
# Private package
import ROOT
import default as default
import headpy.hbes.hstyle as hstyle


# 设定参数
filename = 'lineshape/7_show_omega782pi.pdf'
xlim = (1.95, 2.92)
ylim = (0.0, 1500)
opm_ratio = 2
# 读取数据
data_bes_pppmpz = default.data_bes_pppmpz_fraction('omega782pi')
data_bes_pppmpz = default.delete_point(data_bes_pppmpz, [2.5, 2.7, 2.8])
data_bes_omegapi = default.data_bes_omegapi()
# 修改数据
data_bes_pppmpz['y'][1] = 1089
data_bes_pppmpz['y'][2] = 1255
# 绘图
hstyle.set_style()
canvas = hstyle.get_canvas()
legendlist = []
if(1 == 1):
    len_bes_opp = len(data_bes_pppmpz['x'])
    tgraph_bes_opp = ROOT.TGraphAsymmErrors(len_bes_opp)
    for i in range(len_bes_opp):
        #tgraph_bes_opp.SetPointX(i, data_bes_pppmpz['x'][i])
        #tgraph_bes_opp.SetPointY(i, data_bes_pppmpz['y'][i])
        tgraph_bes_opp.SetPoint(i, data_bes_pppmpz['x'][i], data_bes_pppmpz['y'][i])
        tgraph_bes_opp.SetPointEXlow(i, 0.0)
        tgraph_bes_opp.SetPointEXhigh(i, 0.0)
        tgraph_bes_opp.SetPointEYlow(i, data_bes_pppmpz['e'][i])
        tgraph_bes_opp.SetPointEYhigh(i, data_bes_pppmpz['e'][i])
    hstyle.set_axis(tgraph_bes_opp, r'#sqrt{s} (GeV)', r'Cross Section (pb)')
    tgraph_bes_opp.GetXaxis().SetRangeUser(xlim[0], xlim[1])
    tgraph_bes_opp.GetYaxis().SetRangeUser(ylim[0], ylim[1])
    hstyle.set_hist_data(tgraph_bes_opp, style_code=1)
    tgraph_bes_opp.SetMarkerSize(1.2)
    legendlist.append([tgraph_bes_opp, r'This research', 'lp'])
    tgraph_bes_opp.Draw('AP')
if(1 == 1):
    len_babar_opp = len(data_bes_omegapi['x'])
    tgraph_babar_opp = ROOT.TGraphAsymmErrors(len_babar_opp)
    for i in range(len_babar_opp):
        #tgraph_babar_opp.SetPointX(i, data_bes_omegapi['x'][i])
        #tgraph_babar_opp.SetPointY(i, data_bes_omegapi['y'][i])
        tgraph_babar_opp.SetPoint(i, data_bes_omegapi['x'][i], data_bes_omegapi['y'][i])
        tgraph_babar_opp.SetPointEXlow(i, 0.0)
        tgraph_babar_opp.SetPointEXhigh(i, 0.0)
        tgraph_babar_opp.SetPointEYlow(i, data_bes_omegapi['e'][i])
        tgraph_babar_opp.SetPointEYhigh(i, data_bes_omegapi['e'][i])
    hstyle.set_hist_data(tgraph_babar_opp, style_code=2)
    tgraph_babar_opp.SetMarkerSize(2)
    legendlist.append([tgraph_babar_opp, 'Previous research', 'lp'])
    tgraph_babar_opp.Draw('Psame')
tgraph_bes_opp.Draw('Psame')
drawlist = []
legend = hstyle.get_legend(legendlist,
                           d=0.75, l=0.65)
drawlist.append(legend)
for i in drawlist:
    i.Draw('same')
canvas.Update()
canvas.Print('opicture/%s' % (filename))
input()
