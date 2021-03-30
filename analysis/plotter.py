import ROOT
import time
import numpy as np
import sys


# Load histograms
filename = sys.argv[-1]
inFile = ROOT.TFile.Open(filename)
print("loaded files")

# useful functions   
def saveFig(hist, histColors, legendNames, hist_name, outdir):
    can = ROOT.TCanvas( "c_"+hist_name, "canvas", 800, 800 )

    pad1 = ROOT.TPad( "pad1", "pad1", 0, 0.3, 1, 1.0 )
    pad1.Draw()

    pad1.cd()
    pad1.SetLogy()

    h_stack = ROOT.THStack( "h_stack", hist_name )
    legend = ROOT.TLegend( 0.7, 0.7, 0.89, 0.89 )

    counter = 0
    for h, c, l in zip(hist, histColors, legendNames):
        h.SetFillColor(c)
        h_stack.Add(h)
        legend.AddEntry(h, l)
        
        """h.SetLineColor(c)
        h.SetLineWidth(2)
        if counter == 0:
            h.Draw()
        else:
            h.Draw("same")"""
        counter += 1
    
    h_stack.Draw()
    legend.Draw()


    can.SaveAs(outdir+hist_name+".pdf")
    can.SaveAs(outdir+hist_name+".png")

# main loop
processTypes = ["fakes",
                "flips",
                "rareSM",
                "GluGlu",
                "signal"
                ]
processColors = [ROOT.kRed,
                 ROOT.kBlue,
                 ROOT.kOrange+7,
                 ROOT.kPink+7,
                 ROOT.kGreen+2
                ]

nJet_trilep = []
nJet_SSdilep = []
nJet_OSdilep = []
nJet_onelepFO = []
nJet_dilepFO = []

nBJet_trilep = []
nBJet_SSdilep = []
nBJet_OSdilep = []
nBJet_onelepFO = []
nBJet_dilepFO = []

MET_trilep = []
MET_SSdilep = []
MET_OSdilep = []
MET_onelepFO = []
MET_dilepFO = []

minMT_trilep = []
minMT_SSdilep = []
minMT_OSdilep = []
minMT_onelepFO = []
minMT_dilepFO = []

for p in processTypes:

    h_nJet_trilep   = ROOT.TH1F("h_nJet_trilep", "nJet", 7, -0.5, 6.5)
    h_nJet_SSdilep  = ROOT.TH1D("h_nJet_SSdilep",  "nJets", 7, -0.5, 6.5)
    h_nJet_OSdilep  = ROOT.TH1D("h_nJet_OSdilep",  "nJets", 7, -0.5, 6.5)
    h_nJet_onelepFO = ROOT.TH1D("h_nJet_onelepFO", "nJets", 7, -0.5, 6.5)
    h_nJet_dilepFO  = ROOT.TH1D("h_nJet_dilepFO",  "nJets", 7, -0.5, 6.5)
    
    h_nBJet_trilep   = ROOT.TH1D("h_nBJet_trilep",   "nb-tagged Jets", 4, -0.5, 3.5)
    h_nBJet_SSdilep  = ROOT.TH1D("h_nBJet_SSdilep",  "nb-tagged Jets", 4, -0.5, 3.5)
    h_nBJet_OSdilep  = ROOT.TH1D("h_nBJet_OSdilep",  "nb-tagged Jets", 4, -0.5, 3.5)
    h_nBJet_onelepFO = ROOT.TH1D("h_nBJet_onelepFO", "nb-tagged Jets", 4, -0.5, 3.5)
    h_nBJet_dilepFO  = ROOT.TH1D("h_nBJet_dilepFO",  "nb-tagged Jets", 4, -0.5, 3.5)
    
    h_MET_trilep   = ROOT.TH1D("h_MET_trilep",   "MET", 50, 0, 500)
    h_MET_SSdilep  = ROOT.TH1D("h_MET_SSdilep",  "MET", 50, 0, 500)
    h_MET_OSdilep  = ROOT.TH1D("h_MET_OSdilep",  "MET", 50, 0, 500)
    h_MET_onelepFO = ROOT.TH1D("h_MET_onelepFO", "MET", 50, 0, 500)
    h_MET_dilepFO  = ROOT.TH1D("h_MET_dilepFO",  "MET", 50, 0, 500)
    
    h_minMT_trilep   = ROOT.TH1D("h_minMT_trilep",   "minMT", 50, 0, 500)
    h_minMT_SSdilep  = ROOT.TH1D("h_minMT_SSdilep",  "minMT", 50, 0, 500)
    h_minMT_OSdilep  = ROOT.TH1D("h_minMT_OSdilep",  "minMT", 50, 0, 500)
    h_minMT_onelepFO = ROOT.TH1D("h_minMT_onelepFO", "minMT", 50, 0, 500)
    h_minMT_dilepFO  = ROOT.TH1D("h_minMT_dilepFO",  "minMT", 50, 0, 500)


    h_nJet_trilep   = inFile.Get("h_nJet_trilep"+"_"+p)
    h_nJet_SSdilep  = inFile.Get("h_nJet_SSdilep"+"_"+p)
    h_nJet_OSdilep  = inFile.Get("h_nJet_OSdilep"+"_"+p)
    h_nJet_onelepFO = inFile.Get("h_nJet_onelepFO"+"_"+p)
    h_nJet_dilepFO  = inFile.Get("h_nJet_dilepFO"+"_"+p)
    
    h_nBJet_trilep   = inFile.Get("h_nBJet_trilep"+"_"+p)
    h_nBJet_SSdilep  = inFile.Get("h_nBJet_SSdilep"+"_"+p)
    h_nBJet_OSdilep  = inFile.Get("h_nBJet_OSdilep"+"_"+p)
    h_nBJet_onelepFO = inFile.Get("h_nBJet_onelepFO"+"_"+p)
    h_nBJet_dilepFO  = inFile.Get("h_nBJet_dilepFO"+"_"+p)
    
    h_MET_trilep   = inFile.Get("h_MET_trilep"+"_"+p)
    h_MET_SSdilep  = inFile.Get("h_MET_SSdilep"+"_"+p)
    h_MET_OSdilep  = inFile.Get("h_MET_OSdilep"+"_"+p)
    h_MET_onelepFO = inFile.Get("h_MET_onelepFO"+"_"+p)
    h_MET_dilepFO  = inFile.Get("h_MET_dilepFO"+"_"+p)
    
    h_minMT_trilep   = inFile.Get("h_minMT_trilep"+"_"+p)
    h_minMT_SSdilep  = inFile.Get("h_minMT_SSdilep"+"_"+p)
    h_minMT_OSdilep  = inFile.Get("h_minMT_OSdilep"+"_"+p)
    h_minMT_onelepFO = inFile.Get("h_minMT_onelepFO"+"_"+p)
    h_minMT_dilepFO  = inFile.Get("h_minMT_dilepFO"+"_"+p)


    nJet_trilep.append(h_nJet_trilep)
    nJet_SSdilep.append(h_nJet_SSdilep)
    nJet_OSdilep.append(h_nJet_OSdilep)
    nJet_onelepFO.append(h_nJet_onelepFO)
    nJet_dilepFO.append(h_nJet_dilepFO)

    nBJet_trilep.append(h_nBJet_trilep)
    nBJet_SSdilep.append(h_nBJet_SSdilep)
    nBJet_OSdilep.append(h_nBJet_OSdilep)
    nBJet_onelepFO.append(h_nBJet_onelepFO)
    nBJet_dilepFO.append(h_nBJet_dilepFO)

    MET_trilep.append(h_MET_trilep)
    MET_SSdilep.append(h_MET_SSdilep)
    MET_OSdilep.append(h_MET_OSdilep)
    MET_onelepFO.append(h_MET_onelepFO)
    MET_dilepFO.append(h_MET_dilepFO)

    minMT_trilep.append(h_minMT_trilep)
    minMT_SSdilep.append(h_minMT_SSdilep)
    minMT_OSdilep.append(h_minMT_OSdilep)
    minMT_onelepFO.append(h_minMT_onelepFO)
    minMT_dilepFO.append(h_minMT_dilepFO)

print("defined histograms")


#write histograms
outdir = "/home/users/ksalyer/public_html/dump/FCNC_plots/"
#outdir = "/home/users/ksalyer/FCNCAnalysis/analysis/plots/"

saveFig(nJet_trilep, processColors, processTypes, "h_nJet_trilep", outdir)
saveFig(nJet_SSdilep, processColors, processTypes, "h_nJet_SSdilep", outdir)
saveFig(nJet_OSdilep, processColors, processTypes, "h_nJet_OSdilep", outdir)
saveFig(nJet_onelepFO, processColors, processTypes, "h_nJet_onelepFO", outdir)
saveFig(nJet_dilepFO, processColors, processTypes, "h_nJet_dilepFO", outdir)

saveFig(nBJet_trilep, processColors, processTypes, "h_nBJet_trilep", outdir)
saveFig(nBJet_SSdilep, processColors, processTypes, "h_nBJet_SSdilep", outdir)
saveFig(nBJet_OSdilep, processColors, processTypes, "h_nBJet_OSdilep", outdir)
saveFig(nBJet_onelepFO, processColors, processTypes, "h_nBJet_onelepFO", outdir)
saveFig(nBJet_dilepFO, processColors, processTypes, "h_nBJet_dilepFO", outdir)

saveFig(MET_trilep, processColors, processTypes, "h_MET_trilep", outdir)
saveFig(MET_SSdilep, processColors, processTypes, "h_MET_SSdilep", outdir)
saveFig(MET_OSdilep, processColors, processTypes, "h_MET_OSdilep", outdir)
saveFig(MET_onelepFO, processColors, processTypes, "h_MET_onelepFO", outdir)
saveFig(MET_dilepFO, processColors, processTypes, "h_MET_dilepFO", outdir)

saveFig(minMT_trilep, processColors, processTypes, "h_minMT_trilep", outdir)
saveFig(minMT_SSdilep, processColors, processTypes, "h_minMT_SSdilep", outdir)
saveFig(minMT_OSdilep, processColors, processTypes, "h_minMT_OSdilep", outdir)
saveFig(minMT_onelepFO, processColors, processTypes, "h_minMT_onelepFO", outdir)
saveFig(minMT_dilepFO, processColors, processTypes, "h_minMT_dilepFO", outdir)

print("saved histograms")