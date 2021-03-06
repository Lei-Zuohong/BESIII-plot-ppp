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
}

int plot_pipipi_fitbelow()
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
    bes_data::pipipi_snd.cut(1.1, 2.05);
    bes_data::pipipi_babar.cut(1.1, 2.05);
    bes_data::pipipi_beslow.cut(1.1, 2.05);
    if (1 == 1)
    {
        TGraph *Ddata_snd = new TGraphAsymmErrors(bes_data::pipipi_snd.ndata,
                                                  bes_data::pipipi_snd.xv,
                                                  bes_data::pipipi_snd.yv,
                                                  bes_data::pipipi_snd.xe,
                                                  bes_data::pipipi_snd.xe,
                                                  bes_data::pipipi_snd.ye,
                                                  bes_data::pipipi_snd.ye);
        NameAxes(Ddata_snd, "#sqrt{s} (GeV)", "#sigma(e^{+}e^{-} #rightarrow #pi^{+}#pi^{-}#pi^{0}) (pb)");
        FormatData(Ddata_snd, 1, 20);
        Ddata_snd->SetMarkerStyle(21);
        Ddata_snd->SetMarkerSize(1.3);
        Ddata_snd->SetMarkerColor(3);
        Ddata_snd->SetLineColor(3);
        Ddata_snd->SetLineWidth(2);
        Ddata_snd->Draw("AP");
        legend->AddEntry(Ddata_snd, "SND", "PEL")->SetTextColor(3);
    }
    if (1 == 0)
    {
        TGraph *Ddata_babar = new TGraphAsymmErrors(bes_data::pipipi_babar.ndata,
                                                    bes_data::pipipi_babar.xv,
                                                    bes_data::pipipi_babar.yv,
                                                    bes_data::pipipi_babar.xe,
                                                    bes_data::pipipi_babar.xe,
                                                    bes_data::pipipi_babar.ye,
                                                    bes_data::pipipi_babar.ye);
        FormatData(Ddata_babar, 1, 20);
        Ddata_babar->SetMarkerStyle(21);
        Ddata_babar->SetMarkerSize(1.3);
        Ddata_babar->SetMarkerColor(4);
        Ddata_babar->SetLineColor(4);
        Ddata_babar->SetLineWidth(2);
        Ddata_babar->Draw("Psame");
        legend->AddEntry(Ddata_babar, "BABAR", "PEL")->SetTextColor(4);
    }
    if (1 == 0)
    {
        TGraph *Ddata_beslow = new TGraphAsymmErrors(bes_data::pipipi_beslow.ndata,
                                                     bes_data::pipipi_beslow.xv,
                                                     bes_data::pipipi_beslow.yv,
                                                     bes_data::pipipi_beslow.xe,
                                                     bes_data::pipipi_beslow.xe,
                                                     bes_data::pipipi_beslow.ye,
                                                     bes_data::pipipi_beslow.ye);
        FormatData(Ddata_beslow, 1, 20);
        Ddata_beslow->SetMarkerStyle(21);
        Ddata_beslow->SetMarkerSize(1.3);
        Ddata_beslow->SetMarkerColor(6);
        Ddata_beslow->SetLineColor(6);
        Ddata_beslow->SetLineWidth(2);
        Ddata_beslow->Draw("Psame");
        legend->AddEntry(Ddata_beslow, "BESIII ISR", "PEL")->SetTextColor(6);
    }
    if (1 == 1)
    {
        TF1 *func_test = new TF1("func_test", Func_pipipi, 1.1, 3.0, 10);
        double func_test_start[9] = {2.10160e+03,
                                     1.46048e+00, 9.99059e-01, 1.12192e+02,
                                     1.62766e+00, 2.36609e-01, 7.66721e+02,
                                     2.83825e+01, 3.96547e+00};
        func_test->SetParameters(func_test_start);
        func_test->SetLineColor(2);
        func_test->SetLineStyle(9);
        func_test->SetLineWidth(3);
        func_test->Draw("same");
        legend->AddEntry(func_test, "Fitting", "L")->SetTextColor(2);
    }
    if (1 == 1)
    {
        TF1 *func_omega1420 = new TF1("func_omega1420", Func_pipipi, 1.1, 3.0, 10);
        double func_omega1420_start[9] = {0.0,
                                          1.46048e+00, 9.99059e-01, 1.12192e+02,
                                          1.62766e+00, 2.36609e-01, 0.0,
                                          0.0, 0.0};
        func_omega1420->SetParameters(func_omega1420_start);
        func_omega1420->SetLineColor(4);
        func_omega1420->SetLineStyle(9);
        func_omega1420->SetLineWidth(3);
        func_omega1420->Draw("same");
        legend->AddEntry(func_omega1420, "Omega1420", "L")->SetTextColor(4);
    }
    if (1 == 1)
    {
        TF1 *func_omega1650 = new TF1("func_omega1650", Func_pipipi, 1.1, 3.0, 10);
        double func_omega1650_start[9] = {0.0,
                                          1.46048e+00, 9.99059e-01, 0.0,
                                          1.62766e+00, 2.36609e-01, 7.66721e+02,
                                          0.0, 0.0};
        func_omega1650->SetParameters(func_omega1650_start);
        func_omega1650->SetLineColor(5);
        func_omega1650->SetLineStyle(9);
        func_omega1650->SetLineWidth(3);
        func_omega1650->Draw("same");
        legend->AddEntry(func_omega1650, "Omega1650", "L")->SetTextColor(5);
    }
    if (1 == 1)
    {
        TF1 *func_phi = new TF1("func_phi", Func_pipipi, 1.1, 2.0, 10);
        double func_phi_start[9] = {2.10160e+03,
                                    1.46048e+00, 9.99059e-01, 0.0,
                                    1.62766e+00, 2.36609e-01, 0.0,
                                    0.0, 0.0};
        func_phi->SetParameters(func_phi_start);
        func_phi->SetLineColor(6);
        func_phi->SetLineStyle(9);
        func_phi->SetLineWidth(3);
        func_phi->Draw("same");
        legend->AddEntry(func_phi, "Phi", "L")->SetTextColor(6);
    }
    if (1 == 1)
    {
        TF1 *func_back = new TF1("func_back", Func_pipipi, 1.1, 3.0, 10);
        double func_back_start[9] = {0.0,
                                     1.46048e+00, 9.99059e-01, 0.0,
                                     1.62766e+00, 2.36609e-01, 0.0,
                                     2.83825e+01, 3.96547e+00};
        func_back->SetParameters(func_back_start);
        func_back->SetLineColor(7);
        func_back->SetLineStyle(9);
        func_back->SetLineWidth(3);
        func_back->Draw("same");
        legend->AddEntry(func_back, "Background", "L")->SetTextColor(7);
    }
    if (1 == 1)
    {
        TF1 *func_withoutphi = new TF1("func_withoutphi", Func_pipipi, 1.1, 3.0, 10);
        double func_withoutphi_start[9] = {0.0,
                                           1.46048e+00, 9.99059e-01, 1.12192e+02,
                                           1.62766e+00, 2.36609e-01, 7.66721e+02,
                                           2.83825e+01, 3.96547e+00};
        func_withoutphi->SetParameters(func_withoutphi_start);
        func_withoutphi->SetLineColor(8);
        func_withoutphi->SetLineStyle(9);
        func_withoutphi->SetLineWidth(3);
        func_withoutphi->Draw("same");
        legend->AddEntry(func_withoutphi, "Without phi", "L")->SetTextColor(8);
    }
    legend->Draw("same");
    c1->Update();
    //c1->Print("plot_pipipi_fitbelow.pdf");
    //c1->Print("plot_pipipi_fitbelow.jpg");
    return 0;
}
