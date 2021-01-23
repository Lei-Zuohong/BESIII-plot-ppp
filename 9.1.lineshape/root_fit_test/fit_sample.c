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

double xv[1] = {0.0};
double xe[1] = {0.0};
double yv[1] = {0.0};
double ye[1] = {0.0};
bes_data::DATA usedata(xv, xe, yv, ye, 1);

double Func_pipipi(double *var, double *par)
{
    double e = var[0];
    double output = bes_func::snd_pipipi_line_shape(e,
                                                    1.019461, 0.004249, par[0], 3.1415926 * 163 / 180,
                                                    par[1], par[2], par[3], 3.1415926,
                                                    par[4], par[5], par[6], 0.0,
                                                    par[7], par[8], par[9], par[10],
                                                    par[11], par[12]);
    return output;
}

double func_pipipi(double x, double *par)
{
    double *input_var = new double[1];
    input_var[0] = x;
    double output = Func_pipipi(input_var, par);
    return output;
}

void fcn(Int_t &npar, Double_t *gin, Double_t &f, Double_t *par, Int_t iflag)
{
    Double_t chisq = 0;
    Double_t delta;
    for (Int_t i = 0; i < usedata.ndata; i++)
    {
        delta = (usedata.yv[i] - func_pipipi(usedata.xv[i], par)) / usedata.ye[i];
        chisq += delta * delta;
    }
    f = chisq;
}

int fit_pipipi_besiii()
{
    usedata = bes_data::pipipi_bes;
#pragma region 3.set_option
    int option_fit_migrad = 1;
    int option_fit_hesse = 1;
    int option_fit_minos = 0;
    int option_fit_mnprin = 1;
    int option_draw_origin = 1;
    int option_draw_test_function = 0;
    int option_draw_best_function = 1;
#pragma endregion
#pragma region 3.1.fit
    const int npar = 13;
    TMinuit *my_fit = new TMinuit(npar + 1);
    my_fit->SetFCN(fcn);
    // 初始化需要的参数
    double fit_index[10];
    Int_t fit_error = 0;
    fit_index[0] = 1;
    // 1. SET ERR
    my_fit->mnexcm("SET ERR", fit_index, 1, fit_error);
    // 设定初始值、边界、步长
    my_fit->mnparm(0, "b1b2_phi             ", 2.10160e+03, 0.1000, 0.0000, 10000, fit_error);

    my_fit->mnparm(1, "mr_omega1450         ", 1.46048e+00, 0.0010, 1.0000, 2.000, fit_error);
    my_fit->mnparm(2, "wr_omega1450         ", 9.99059e-01, 0.0010, 0.0100, 1.500, fit_error);
    my_fit->mnparm(3, "b1b2_omega1450       ", 1.12192e+02, 0.1000, 0.0000, 10000, fit_error);

    my_fit->mnparm(4, "mr_omega1680         ", 1.62766e+00, 0.0010, 1.0000, 2.000, fit_error);
    my_fit->mnparm(5, "wr_omega1680         ", 2.36609e-01, 0.0010, 0.0100, 1.000, fit_error);
    my_fit->mnparm(6, "b1b2_omega1680       ", 7.66721e+02, 0.1000, 0.0000, 10000, fit_error);

    my_fit->mnparm(7, "mr_omega_new         ", 2.20000, 0.0010, 2.0000, 2.500, fit_error);
    my_fit->mnparm(8, "wr_omega_new         ", 0.31000, 0.0010, 0.0100, 1.000, fit_error);
    my_fit->mnparm(9, "b1b2_omega_new       ", 50.0000, 0.1000, 0.0000, 10000, fit_error);
    my_fit->mnparm(10, "phase_omega_new      ", 0.00000, 0.0010, -4.000, 4.000, fit_error);

    my_fit->mnparm(11, "back                 ", 2.83825e+01, 0.0010, 0.0000, 10000, fit_error);
    my_fit->mnparm(12, "phase_back           ", -2.3177e+00, 0.0010, -4.000, 4.000, fit_error);
    fit_index[0] = 1000;
    fit_index[1] = 0.001;
    if (option_fit_migrad == 1):my_fit->mnexcm("MIGRAD", fit_index, 2, fit_error);
    if (option_fit_hesse == 1):my_fit->mnexcm("HESSE", fit_index, 2, fit_error);
    if (option_fit_minos == 1):my_fit->mnexcm("MINOS", fit_index, 2, fit_error);
    if (option_fit_mnprin == 1)
    {
        double amin, edm, errdef;
        Int_t nvpar, nparx, icstat;
        my_fit->mnstat(amin, edm, errdef, nvpar, nparx, icstat);
        my_fit->mnprin(0, amin);
    }
    double bestPar[npar];
    double bestErr[npar];
    for (int i = 0; i < npar; i++)
    {
        my_fit->GetParameter(i, bestPar[i], bestErr[i]);
    }
#pragma endregion
#pragma region 3.2.plot
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
#pragma endregion
#pragma region 3.3.draw
    TCanvas *c1 = new TCanvas("c1", "c1", 800, 600);
    if (option_draw_origin == 1)
    {
        TGraph *Ddata = new TGraphAsymmErrors(usedata.ndata,
                                              usedata.xv,
                                              usedata.yv,
                                              usedata.xe,
                                              usedata.xe,
                                              usedata.ye,
                                              usedata.ye);
        TLegend *legend = new TLegend(0.65, 0.7, 0.94, 0.94);
        FormatData(Ddata, 1, 20);
        NameAxes(Ddata, "#sqrt{s} (GeV)", "#sigma(e^{+}e^{-} #rightarrow #pi^{+}#pi^{0}#pi^{0}) (pb)");
        Ddata->SetMarkerStyle(21);
        Ddata->SetMarkerSize(1.3);
        Ddata->SetMarkerColor(2);
        Ddata->SetLineColor(2);
        Ddata->SetLineWidth(2);
        Ddata->Draw("AP");
        legend->AddEntry(Ddata, "BESIII", "PEL")->SetTextColor(2);
    }
    if (option_draw_best_function == 1)
    {
        TF1 *func_best = new TF1("func_best", Func_pipipi, 1.0, 3.2, 10);
        double func_best_start[13] = {bestPar[0], bestPar[1], bestPar[2], bestPar[3], bestPar[4],
                                      bestPar[5], bestPar[6], bestPar[7], bestPar[8], bestPar[9],
                                      bestPar[10], bestPar[11], bestPar[12]};
        func_best->SetParameters(func_best_start);
        func_best->SetLineColor(4);
        func_best->SetLineStyle(9);
        func_best->SetLineWidth(3);
        func_best->Draw("same");
        legend->AddEntry(func_best, "Fitting", "L")->SetTextColor(4);
    }
    legend->Draw();
    c1->Update();
    c1->Print("fit_pipipi_besiii.pdf");
    c1->Print("fit_pipipi_besiii.jpg");
#pragma endregion
#pragma region 3.4.print
    double best_chisq = 0;
    for (Int_t i = 0; i < Ndata; i++)
    {
        double delta = (usedata.yv[i] - func_pipipi(usedata.xv[i], bestPar)) / usedata.ye[i];
        best_chisq += delta * delta;
    }
    cout << "result_best_chisq: " << best_chisq << endl;
#pragma endregion
    return 0;
}
