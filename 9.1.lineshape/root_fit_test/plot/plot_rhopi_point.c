#pragma region 1.include
#include <iostream>
#include <fstream>
#include "TComplex.h"
#include <complex>

#include <iostream>
#include <fstream>
#include "TGraphAsymmErrors.h"
#include "TGraphErrors.h"
#include "TLegend.h"
#include "TLegendEntry.h"
#include "bes3plotstyle.c"
#include "Math/QuantFuncMathCore.h"

#include <iomanip>
#include <TTree.h>
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TH2F.h>
#include <TMinuit.h>
#include <TComplex.h>
#include <TLorentzVector.h>
#include <TGraph.h>

#include <cassert>

#include "Riostream.h"
#include "TMatrixD.h"
#include "TVectorD.h"
#include "TGraphErrors.h"
#include "TDecompChol.h"
#include "TDecompSVD.h"
#include "TF1.h"

#include "headc/bes_func.h"
#include "headc/bes_data.h"

using namespace std;
#pragma endregion
/*
double Func_pipipi(double *var, double *par)
{
    double e = var[0];
    double output = bes_func::snd_pipipi_line_shape(e,
                                                    1.019461, 0.004249, par[0], 3.1415926 * 163 / 180,
                                                    par[1], par[2], par[3], 3.1415926,
                                                    par[4], par[5], par[6], 0.0,
                                                    2.300000, 0.050000, 0.0, 0.0,
                                                    par[7], par[8]);
    return output;
}*/

int plot_rhopi_point()
{
    const int npar = 9;
    gStyle->SetPalette(1);
    gStyle->SetCanvasBorderMode(0);
    gStyle->SetCanvasBorderSize(0);
    gStyle->SetCanvasColor(10);
    gStyle->SetLabelFont(42, "xyz");
    gStyle->SetLabelSize(0.07, "xyz");
    gStyle->SetLabelOffset(0.01, "xyz");
    gStyle->SetNdivisions(510, "xyz");
    gStyle->SetTitleFont(42, "xyz");
    gStyle->SetTitleColor(1, "xyz");
    gStyle->SetTitleSize(0.08, "xyz");
    gStyle->SetTitleOffset(1.15, "xyz");
    gStyle->SetPadBorderMode(0);
    gStyle->SetPadBorderSize(0);
    gStyle->SetPadColor(10);
    gStyle->SetPadLeftMargin(0.2);
    gStyle->SetPadBottomMargin(0.2);
    gStyle->SetPadRightMargin(0.15);
    gStyle->SetPadTopMargin(0.05);
    gStyle->SetPadRightMargin(0.05);
    gStyle->SetPadTopMargin(0.05);
    gStyle->SetLegendBorderSize(0);
    gStyle->SetOptDate(0);
    gStyle->SetOptStat(0);
    gStyle->SetOptFit(0);
    gStyle->SetOptTitle(0);
    gStyle->SetOptTitle(kFALSE);
    TCanvas *c1 = new TCanvas("c1", "c1", 1600, 1200);
    TLegend *legend = new TLegend(0.65, 0.7, 0.94, 0.94);
    double xv[1] = {0.0};
    double xe[1] = {0.0};
    double yv[1] = {0.0};
    double ye[1] = {0.0};
    bes_data::DATA usedata(xv, xe, yv, ye, 1);
    bes_data::rhopi_snd.cut(1.1, 3.2);
    bes_data::rhopi_bes.cut(1.1, 3.2);
    usedata = bes_data::add_DATA(bes_data::rhopi_snd, bes_data::rhopi_bes);
    if (1 == 1)
    {
        TGraph *Ddata_use = new TGraphAsymmErrors(usedata.ndata,
                                                  usedata.xv,
                                                  usedata.yv,
                                                  usedata.xe,
                                                  usedata.xe,
                                                  usedata.ye,
                                                  usedata.ye);
        NameAxes(Ddata_use, "#sqrt{s} (GeV)", "#sigma(e^{+}e^{-} #rightarrow #rho#pi) (pb)");
        FormatData(Ddata_use, 1, 20);
        Ddata_use->SetMarkerStyle(21);
        Ddata_use->SetMarkerSize(1.3);
        Ddata_use->SetMarkerColor(5);
        Ddata_use->SetLineColor(5);
        Ddata_use->SetLineWidth(2);
        Ddata_use->Draw("AP");
    }
    if (1 == 1)
    {
        TGraph *Ddata_snd = new TGraphAsymmErrors(bes_data::rhopi_snd.ndata,
                                                  bes_data::rhopi_snd.xv,
                                                  bes_data::rhopi_snd.yv,
                                                  bes_data::rhopi_snd.xe,
                                                  bes_data::rhopi_snd.xe,
                                                  bes_data::rhopi_snd.ye,
                                                  bes_data::rhopi_snd.ye);
        FormatData(Ddata_snd, 1, 20);
        Ddata_snd->SetMarkerStyle(21);
        Ddata_snd->SetMarkerSize(1.3);
        Ddata_snd->SetMarkerColor(4);
        Ddata_snd->SetLineColor(4);
        Ddata_snd->SetLineWidth(2);
        Ddata_snd->Draw("Psame");
        legend->AddEntry(Ddata_snd, "SND", "PEL")->SetTextColor(4);
    }
    if (1 == 1)
    {
        TGraph *Ddata_bes = new TGraphAsymmErrors(bes_data::rhopi_bes.ndata,
                                                  bes_data::rhopi_bes.xv,
                                                  bes_data::rhopi_bes.yv,
                                                  bes_data::rhopi_bes.xe,
                                                  bes_data::rhopi_bes.xe,
                                                  bes_data::rhopi_bes.ye,
                                                  bes_data::rhopi_bes.ye);
        FormatData(Ddata_bes, 1, 20);
        Ddata_bes->SetMarkerStyle(21);
        Ddata_bes->SetMarkerSize(1.3);
        Ddata_bes->SetMarkerColor(2);
        Ddata_bes->SetLineColor(2);
        Ddata_bes->SetLineWidth(2);
        Ddata_bes->Draw("Psame");
        legend->AddEntry(Ddata_bes, "BESIII", "PEL")->SetTextColor(2);
    }
    /*
    if (1 == 1)
    {
        TF1 *func_test = new TF1("func_test", Func_pipipi, 1.1, 2.0, 10);
        double func_test_start[9] = {2.10160e+03,
                                     1.46048e+00, 9.99059e-01, 1.12192e+02,
                                     1.62766e+00, 2.36609e-01, 7.66721e+02,
                                     2.83825e+01, 3.96547e+00};
        func_test->SetParameters(func_test_start);
        func_test->SetLineColor(1);
        func_test->SetLineStyle(9);
        func_test->SetLineWidth(3);
        func_test->Draw("same");
        legend->AddEntry(func_test, "Fitting", "L")->SetTextColor(1);
    }*/
    legend->Draw("same");
    c1->Update();
    c1->Print("plot_rhopi_point.pdf");
    c1->Print("plot_rhopi_point.jpg");
    return 0;
}
