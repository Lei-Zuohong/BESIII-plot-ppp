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

using namespace std;
#pragma endregion
#pragma region 2.0.phasespace_function
double Momentum(double x, double m1, double m2)
{
    double part1 = x * x - (m1 + m2) * (m1 + m2);
    double part2 = x * x - (m1 - m2) * (m1 - m2);
    double output = 0;
    if (part1 > 0)
    {
        output = sqrt(part1 * part2) / (2 * x);
    }
    else
    {
        output = 0;
    }
    return output;
}

double Phasespaceint(double *m, double *mass)
{
    double mu = m[0];
    double m0 = mass[0];
    double m1 = mass[1];
    double m2 = mass[2];
    double m3 = mass[3];
    double E12 = (m3 * m3 + mu - m0 * m0) / (2 * m3);
    double part1 = Momentum(E12, m1, m2);
    double part2 = Momentum(m3, sqrt(mu), m0);
    double output = part1 * part2 / (m3 * E12);
    return output;
}

double Phasespace(double x)
{
    double mpiz = 0.13498;
    double momega = 0.78265;
    TF1 *pdf = new TF1("pdf", Phasespaceint, 0, 5, 4);
    pdf->SetParameter(0, mpiz);
    pdf->SetParameter(1, momega);
    pdf->SetParameter(2, mpiz);
    pdf->SetParameter(3, x);
    double x1 = mpiz + momega;
    double x2 = x - mpiz;
    double pi = 3.1415926;
    double output = pdf->Integral(x1, x2) / pi / pi / pi / 2.5;
    return output;
}
#pragma endregion
#pragma region 2.1.input_data
const int Ndata = 19;
double xv[Ndata] = {2., 2.05, 2.1, 2.125, 2.15, 2.175, 2.2, 2.2324, 2.3094, 2.3864,
                    2.396, 2.6444, 2.6464, 2.9, 2.95, 2.981, 3., 3.02, 3.08};
double xe[Ndata] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
double yv[Ndata] = {396.45361363, 343.78185221, 315.01832213, 373.64206324, 415.09194772,
                    294.97070169, 247.90466141, 264.66898385, 206.77077837, 130.4083881,
                    134.96843607, 64.80962381, 69.72858224, 35.73219311, 32.32693706,
                    31.56566033, 32.44858999, 18.98827785, 9.01159806};
double ye[Ndata] = {12.10522737, 20.47001322, 9.40073534, 3.59730693, 24.58936805, 9.401119,
                    7.1815981, 8.69930914, 5.7206749, 4.06115812, 2.46097189, 2.2803079,
                    2.46051272, 1.08910151, 2.52605349, 2.25033934, 2.67369352, 1.50150048,
                    0.37122428};
double edge_left = 1.9;
double edge_right = 3.2;
double intergral = 0.00001;
const int Nphase = int((edge_right - edge_left) / intergral);
double *phasespace = new double[Nphase];
#pragma endregion

double Get_phasespace(double x)
{
    int dx = int((x - edge_left) / intergral);
    double output = phasespace[dx];
    return output;
}

double Func_etapipi(double *var, double *par)
{
    // parameter
    double x = var[0];
    double mr = par[0];
    double wr = par[1];
    double phi = par[2];
    double brc = par[3];
    double c = par[4];
    double b = par[5];
    complex<double> img(0.0, 1.0);
    complex<double> real(1.0, 0.0);
    complex<double> phase(cos(phi), sin(phi));

    double phspx = Get_phasespace(x);
    double phspm = Get_phasespace(mr);

    double part1 = sqrt(12 * 3.1415926 * wr * brc);
    complex<double> part2 = x * x - mr * mr + img * mr * wr;
    complex<double> partr = (mr / x) * (part1 / part2) * phase * sqrt(phspx / phspm);
    double partn = c * pow(x, b) * sqrt(phspx);
    double value = pow(abs(partr + partn), 2.0);
    return value;
}

double Func_etapipi_continue(double *var, double *par)
{
    // parameter
    double x = var[0];
    double mr = par[0];
    double wr = par[1];
    double phi = par[2];
    double brc = par[3];
    double c = par[4];
    double b = par[5];
    complex<double> img(0.0, 1.0);
    complex<double> real(1.0, 0.0);
    complex<double> phase(cos(phi), sin(phi));

    double phspx = Get_phasespace(x);
    double phspm = Get_phasespace(mr);

    double part1 = sqrt(12 * 3.1415926 * wr * brc);
    complex<double> part2 = x * x - mr * mr + img * mr * wr;
    complex<double> partr = (mr / x) * (part1 / part2) * phase * sqrt(phspx / phspm);
    double partn = c * pow(x, b) * sqrt(phspx);
    double value = pow(partn, 2.0);
    return value;
}

double func_etapipi(double x, double *par)
{
    // parameter
    double mr = par[0];
    double wr = par[1];
    double phi = par[2];
    double brc = par[3];
    double c = par[4];
    double b = par[5];
    complex<double> img(0.0, 1.0);
    complex<double> real(1.0, 0.0);
    complex<double> phase(cos(phi), sin(phi));

    double phspx = Get_phasespace(x);
    double phspm = Get_phasespace(mr);

    double part1 = sqrt(12 * 3.1415926 * wr * brc);
    complex<double> part2 = x * x - mr * mr + img * mr * wr;
    complex<double> partr = (mr / x) * (part1 / part2) * phase * sqrt(phspx / phspm);
    double partn = c * pow(x, b) * sqrt(phspx);
    double value = pow(abs(partr + partn), 2.0);
    return value;
}

void fcn(Int_t &npar, Double_t *gin, Double_t &f, Double_t *par, Int_t iflag)
{
    Double_t chisq = 0;
    Double_t delta;
    for (Int_t i = 0; i < Ndata; i++)
    {
        delta = (yv[i] - func_etapipi(xv[i], par)) / ye[i];
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
#pragma region 3.0.calculate_phasespace
    cout << "1. Start calculating phase space" << endl;
    for (int i = 0; i < Nphase; i++)
    {
        phasespace[i] = Phasespace(edge_left + intergral * i);
    }
#pragma endregion
#pragma region 3.1.fit
    const int npar = 6;
    TMinuit *my_fit = new TMinuit(npar + 1);
    my_fit->SetFCN(fcn);
    // 初始化需要的参数
    double fit_index[10];
    Int_t fit_error = 0;
    fit_index[0] = 1;
    // 1. SET ERR
    my_fit->mnexcm("SET ERR", fit_index, 1, fit_error);
    // 设定初始值、边界、步长
    my_fit->mnparm(0, "mr     ", 2.22130e+00, 0.001, 2.0, 2.4, fit_error);
    my_fit->mnparm(1, "wr     ", 5.04612e-02, 0.0001, 0.005, 0.5, fit_error);
    my_fit->mnparm(2, "phi    ", 2.32921e+00, 0.0001, 2, 2.5, fit_error);
    my_fit->mnparm(3, "brc    ", 8.61643e-02, 0.0001, 0.01, 1, fit_error);
    my_fit->mnparm(4, "c      ", 1.90508e+04, 0.01, 0.0, 100000.0, fit_error);
    my_fit->mnparm(5, "b      ", -5.36684e+00, 0.001, -100.0, 0.0, fit_error);
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
        TF1 *func_test = new TF1("func_test", Func_etapipi, 1.9, 3.2, 6);
        double func_test_start[6] = {2.22130e+00,
                                     5.04571e-02,
                                     2.32924e+00,
                                     8.61664e-02,
                                     1.90508e+04,
                                     -5.36684e+00};
        func_test->SetParameters(func_test_start);
        func_test->SetLineColor(4);
        func_test->SetLineStyle(9);
        func_test->SetLineWidth(3);
        func_test->Draw("same");
    }
    if (option_draw_best_function == 1)
    {
        TF1 *func_best = new TF1("func_best", Func_etapipi, 1.9, 3.2, 6);
        double func_best_start[6] = {bestPar[0], bestPar[1], bestPar[2], bestPar[3], bestPar[4], bestPar[5]};
        func_best->SetParameters(func_best_start);
        func_best->SetLineColor(4);
        func_best->SetLineStyle(9);
        func_best->SetLineWidth(3);
        func_best->Draw("same");
        legend->AddEntry(func_best, "Fitting", "L")->SetTextColor(4);
    }
    if (option_draw_continue_function == 1)
    {
        TF1 *func_conti = new TF1("func_conti", Func_etapipi_continue, 1.9, 3.2, 6);
        double func_conti_start[6] = {bestPar[0], bestPar[1], bestPar[2], bestPar[3], bestPar[4], bestPar[5]};
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
        double delta = (yv[i] - func_etapipi(xv[i], bestPar)) / ye[i];
        best_chisq += delta * delta;
    }
    cout << "result_best_chisq: " << best_chisq << endl;
#pragma endregion
    return 0;
}
