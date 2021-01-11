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

using namespace std;
#pragma endregion
#pragma region 2.1.input_data
const int Ndata = 40;
double xv[Ndata] = {1.050000, 1.075000, 1.100000, 1.125000, 1.150000,
                    1.175000, 1.200000, 1.225000, 1.250000, 1.275000,
                    1.300000, 1.325000, 1.350000, 1.375000, 1.400000,
                    1.425000, 1.450000, 1.475000, 1.500000, 1.525000,
                    1.550000, 1.575000, 1.600000, 1.625000, 1.650000,
                    1.675000, 1.700000, 1.725000, 1.750000, 1.775000,
                    1.800000, 1.825000, 1.850000, 1.870000, 1.890000,
                    1.900000, 1.925000, 1.950000, 1.975000, 2.000000};
double xe[Ndata] = {0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0, 0.0, 0.0, 0.0,
                    0.0, 0.0, 0.0, 0.0, 0.0};
double yv[Ndata] = {1270.000000, 3300.000000, 4270.000000, 4640.000000, 5240.000000,
                    5420.000000, 5130.000000, 5800.000000, 6000.000000, 5550.000000,
                    4920.000000, 4910.000000, 5020.000000, 4810.000000, 4180.000000,
                    4060.000000, 4100.000000, 4300.000000, 4440.000000, 4520.000000,
                    4630.000000, 4710.000000, 5810.000000, 5060.000000, 4650.000000,
                    3420.000000, 2610.000000, 2150.000000, 1800.000000, 1620.000000,
                    1050.000000, 1280.000000, 1280.000000, 920.000000, 680.000000,
                    1040.000000, 660.000000, 510.000000, 690.000000, 840.000000};
double ye[Ndata] = {545.893763, 477.074418, 466.904701, 412.310563, 424.499706,
                    361.247837, 362.353419, 374.833296, 382.099463, 376.430604,
                    340.587727, 311.126984, 325.576412, 304.138127, 300.000000,
                    292.061637, 308.058436, 283.196045, 275.862284, 312.409987,
                    312.409987, 318.904374, 374.833296, 356.089876, 328.024389,
                    266.270539, 259.422435, 210.237960, 196.977156, 174.642492,
                    186.815417, 152.315462, 180.277564, 136.014705, 123.693169,
                    158.113883, 114.017543, 131.529464, 143.178211, 164.924225};
#pragma endregion

double Func_pipipi(double *var, double *par)
{
    double e = var[0];
    double output = bes_func::snd_line_shape(e,
                                             1.019461, 0.004249, par[0], 3.14 * 163 / 180,
                                             0.78265, 0.00849, par[1], 0.0,
                                             par[2], par[3], par[4], 3.14,
                                             par[5], par[6], par[7], 0.0,
                                             par[8], par[9]);
    return output;
}

double func_pipipi(double x, double *par)
{
    double e = x;
    double mr_omega1450 = par[0];
    double wr_omega1450 = par[1];
    double b1b2_omega1450 = par[2];
    double mr_omega1680 = par[3];
    double wr_omega1680 = par[4];
    double b1b2_omega1680 = par[5];
    double back = par[6];
    double phase_omega1450 = par[7];
    double phase_omega1680 = par[8];
    double phase_back = par[9];
    double output = bes_func::snd_line_shape(e,
                                             mr_omega1450, wr_omega1450, b1b2_omega1450,
                                             mr_omega1680, wr_omega1680, b1b2_omega1680,
                                             back,
                                             phase_omega1450,
                                             phase_omega1680,
                                             phase_back);
    return output;
}

void fcn(Int_t &npar, Double_t *gin, Double_t &f, Double_t *par, Int_t iflag)
{
    Double_t chisq = 0;
    Double_t delta;
    for (Int_t i = 0; i < Ndata; i++)
    {
        delta = (yv[i] - func_pipipi(xv[i], par)) / ye[i];
        chisq += delta * delta;
    }
    f = chisq;
}

int fitomegapipi_v1()
{
#pragma region 3.set_option
    int option_fit_migrad = 1;
    int option_fit_hesse = 1;
    int option_fit_minos = 0;
    int option_fit_mnprin = 1;
    int option_draw_origin = 1;
    int option_draw_test_function = 0;
    int option_draw_best_function = 1;
    int option_draw_continue_function = 1;
#pragma endregion
#pragma region 3.1.fit
    const int npar = 10;
    TMinuit *my_fit = new TMinuit(npar + 1);
    my_fit->SetFCN(fcn);
    // 初始化需要的参数
    double fit_index[10];
    Int_t fit_error = 0;
    fit_index[0] = 1;
    // 1. SET ERR
    my_fit->mnexcm("SET ERR", fit_index, 1, fit_error);
    // 设定初始值、边界、步长
    my_fit->mnparm(0, "mr_omega1450         ", 1.45000, 0.0010, 1.0000, 2.000, fit_error);
    my_fit->mnparm(1, "wr_omega1450         ", 0.88000, 0.0010, 0.0100, 1.000, fit_error);
    my_fit->mnparm(2, "b1b2_omega1450       ", 73.0000, 0.1000, 0.0000, 10000, fit_error);
    my_fit->mnparm(3, "mr_omega1680         ", 1.68000, 0.0010, 1.0000, 2.000, fit_error);
    my_fit->mnparm(4, "wr_omega1680         ", 0.31000, 0.0010, 0.0100, 1.000, fit_error);
    my_fit->mnparm(5, "b1b2_omega1680       ", 156.000, 0.1000, 0.0000, 10000, fit_error);
    my_fit->mnparm(6, "back                 ", 0.01000, 0.0010, 0.0000, 10000, fit_error);
    my_fit->mnparm(7, "phase_omega1450      ", 0.00000, 0.0010, -4.000, 4.000, fit_error);
    my_fit->mnparm(8, "phase_omega1680      ", 0.00000, 0.0010, -4.000, 4.000, fit_error);
    my_fit->mnparm(9, "phase_back           ", 0.00000, 0.0010, -4.000, 4.000, fit_error);
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
        TGraph *Ddata = new TGraphAsymmErrors(Ndata, xv, yv, xe, xe, ye, ye);
        TLegend *legend = new TLegend(0.65, 0.7, 0.94, 0.94);
        FormatData(Ddata, 1, 20);
        NameAxes(Ddata, "#sqrt{s} (GeV)", "#sigma(e^{+}e^{-} #rightarrow #omega #pi^{0}#pi^{0}) (pb)");
        Ddata->SetMarkerStyle(21);
        Ddata->SetMarkerSize(1.3);
        Ddata->SetMarkerColor(2);
        Ddata->SetLineColor(2);
        Ddata->SetLineWidth(2);
        Ddata->Draw("AP");
        legend->AddEntry(Ddata, "R-scan data", "PEL")->SetTextColor(2);
    }
    if (option_draw_test_function == 1)
    {
        TF1 *func_test = new TF1("func_test", Func_pipipi, 1.0, 3.2, 10);
        double func_test_start[10] = {1.450, 0.88, 73,
                                      1.680, 0.31, 156,
                                      0.0,
                                      0.0,
                                      0.0,
                                      0.0};
        func_test->SetParameters(func_test_start);
        func_test->SetLineColor(4);
        func_test->SetLineStyle(9);
        func_test->SetLineWidth(3);
        func_test->Draw("same");
    }
    if (option_draw_best_function == 1)
    {
        TF1 *func_best = new TF1("func_best", Func_pipipi, 1.0, 3.2, 10);
        double func_best_start[6] = {bestPar[0], bestPar[1], bestPar[2], bestPar[3], bestPar[4],
                                     bestPar[5], bestPar[6], bestPar[7], bestPar[8], bestPar[9]};
        func_best->SetParameters(func_best_start);
        func_best->SetLineColor(4);
        func_best->SetLineStyle(9);
        func_best->SetLineWidth(3);
        func_best->Draw("same");
        legend->AddEntry(func_best, "Fitting", "L")->SetTextColor(4);
    }
    if (option_draw_continue_function == 1)
    {
        TF1 *func_conti = new TF1("func_conti", Func_pipipi, 1.0, 3.2, 10);
        double func_conti_start[6] = {bestPar[0], bestPar[1], bestPar[2], bestPar[3], bestPar[4],
                                      bestPar[5], bestPar[6], bestPar[7], bestPar[8], bestPar[9]};
        func_conti->SetParameters(func_conti_start);
        func_conti->SetLineColor(8);
        func_conti->SetLineStyle(2);
        func_conti->SetLineWidth(3);
        func_conti->Draw("same");
        legend->AddEntry(func_conti, "Continous", "L")->SetTextColor(8);
    }
    legend->Draw();
    c1->Update();
    c1->Print("fitomega.pdf");
    c1->Print("fitomega.jpg");
#pragma endregion
#pragma region 3.4.print
    double best_chisq = 0;
    for (Int_t i = 0; i < Ndata; i++)
    {
        double delta = (yv[i] - func_pipipi(xv[i], bestPar)) / ye[i];
        best_chisq += delta * delta;
    }
    cout << "result_best_chisq: " << best_chisq << endl;
#pragma endregion
    return 0;
}
