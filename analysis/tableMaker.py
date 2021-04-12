import ROOT
import time
import numpy as np
import sys
import pandas as pd
#from pdflatex import PDFLaTeX

# Load histograms
filename = sys.argv[-1]
#backgroundFile = sys.argv[-2]
#signalFile = sys.argv[-1]
#bFile = ROOT.TFile.Open(backgroundFile)
#sFile = ROOT.TFile.Open(signalFile)
print("loaded files")

# useful functions 
def makeTableHeader(selectionHeaders, processes):
    #cBreak = " & "
    #line = ""
    line = []
    counter = 0
    for s in selectionHeaders:
        line.append(s)
        #if counter == 0:
        #    line = line + s
        #else:
        #    line = line + cBreak + s
        #counter += 1
    for p in processes:
        proc = p.replace("_", " ")
        #line = line + cBreak + proc
        line.append(proc)
        line.append("error")
    #line = line + cBreak + "total background \\\\"
    line.append("total background")
    line.append("error")
    return line
    
def makeTableRow(hist, nJets, nBs, nLeps, processes):
    cBreak = " & "
    nLeps = nLeps.replace("_"," ")
    nLeps = nLeps.replace("lep","l")
    nLeps = nLeps.replace("tri","3+")
    nLeps = nLeps.replace("di","2")
    nLeps = nLeps.replace("one","1")
    nJets = nJets.replace("j","")
    nJets = nJets.replace("ge","+")
    nBs = nBs.replace("b","")
    nBs = nBs.replace("ge","+")
    #line = str(nLeps)+cBreak+str(nJets)+cBreak+str(nBs)
    line = []
    line.append(nLeps)
    line.append(nJets)
    line.append(nBs)
    totBack = 0
    totError = 0
    for h,p in zip(hist,processes):
        numBins = h.GetNbinsX()
        totYield = 0
        error = 0
        for b in range(numBins):
            if "signal" in p:
                totYield = totYield+(0.01*h.GetBinContent(b))
            else:
                totYield = totYield+h.GetBinContent(b)
                totBack = totBack + totYield
            if h.GetBinContent(b) != 0:
                if "signal" in p:
                    error = 0.01*h.GetBinError(b)
                else:
                    error = h.GetBinError(b)
                    totError = totError + pow(h.GetBinError(b),2)
        #line = line + cBreak + str(round(totYield,2)) + " $\pm$ " + str(round(error,2))
        line.append(round(totYield,2))
        line.append(round(error,2))
    #line = line + cBreak + str(round(totBack,2)) + " \\\\"
    line.append(round(totBack,2))
    totError = np.sqrt(totError)
    line.append(round(totError,2))
    return line

def makeTable(lines, outdir):
    outFile = open(outdir+"tables/yieldsTable.txt","w")
    for l in lines:
        outFile.write(l)
        outFile.write("\n")
    outFile.close()
    return None

def addHistos(hist, histNames, legendNames, histName, nBins, xmin, xmax):   
    listOfAddedHistos = []
    for s in legendNames:
        h_combined = ROOT.TH1F("h_combined"+s+histName, histName, nBins, xmin, xmax)
        for h, n in zip(hist, histNames):
            if s in n:
                h_combined.Add(h)
        listOfAddedHistos.append(h_combined)
    return listOfAddedHistos

def getObjFromFile(fname, hname):
    f = ROOT.TFile(fname)
    assert not f.IsZombie()
    f.cd()
    htmp = f.Get(hname)
    if not htmp:  return htmp
    ROOT.gDirectory.cd('PyROOT:/')
    res = htmp.Clone()
    f.Close()
    return res

# main loop
#outdir = "/home/users/ksalyer/public_html/dump/FCNC_tables/"
outdir = "/home/users/ksalyer/FCNCAnalysis/analysis/plots/"

processTypes = ["fakes",
                "flips",
                "other",
                "signal_hut",
                "signal_hct"
                ]

"""processTypes = ["signal_hut",
                "signal_hct",
                "rareSM",
                "wjets",
                "DY",
                "ttX",
                "multiboson",
                "ttjets"
                ]"""

leptonSelections = ["trilep",
                    "SS_SF_dilep",
                    "SS_OF_dilep",
                    "OS_SF_dilep",
                    "OS_OF_dilep",
                    #"onelepFO",
                    #"dilepFO"
                   ]

jetSelections = ["2j",
                 "3j",
                 "ge4j"
                 ]

bJetSelections = ["0b",
                  "1b",
                  "ge2b"
                  ]

plottedVariables = [#["nJet", 7, -0.5, 6.5],
                    "nBJet", 
                    #["nGoodLeps", 6, -0.5, 5.5],
                    #["leadLepPt", 50, 0, 500],
                    #["leadLepEta", 20, -5, 5],
                    #["leadLepMass", 50, 0, 500],
                    #["leadLepMiniIso", 50, 0, 5],
                    #["leadLepPtRel", 50, 0, 10],
                    #["leadLepPtRatio", 50, 0, 5],
                    #["leadJetPt", 50, 0, 500],
                    #["leadBPt", 50, 0, 500],
                    #["leadBMass", 50, 0, 500],
                    #["jetHT", 50, 0, 500],
                    #["MET", 50, 0, 500],
                    #["minMT", 50, 0, 500],
                    #["MT_b_MET", 50, 0, 500]
                   ]

headers = ["nLeptons",
           "nJets",
           "nBtags"
           ]
header = makeTableHeader(headers,processTypes)
#tableLines = [header]
#df = pd.DataFrame(columns=header)
#print(df)
allLines = []

for v in plottedVariables:
    #print(nbins, xmin, xmax)
    for l in leptonSelections:
        for j in jetSelections:
            for b in bJetSelections:
                histosForTable = []
                for p in processTypes:
                    histoName = "h_"+v+"_"+l+"_"+j+"_"+b+"_"+p
                    #print(type(v),type(l),type(j),type(b),type(p))
                    hist = getObjFromFile(filename,histoName)
                    histosForTable.append(hist)
                line = ""
                line = makeTableRow(histosForTable, j, b, l, processTypes)
                #print(df)
                allLines.append(line)
                #print(df)
                #tableLines.append(line)
    #makeTable(tableLines, outdir)
    df = pd.DataFrame(allLines, columns=header)
    outFile = open(outdir+"tables/yieldsTable.tex","w")
    outFile.write("\documentclass[7pt,oneside]{report} \n")
    outFile.write("\usepackage{graphicx,xspace,amssymb,amsmath,colordvi,colortbl,verbatim,multicol} \n")
    #outFile.write("\usepackage{multirow, rotating} \n")
    #outFile.write("\usepackage[active,tightpage]{preview} \n")
    outFile.write("\\renewcommand{\\arraystretch}{1.1} \n")
    outFile.write("\\begin{document} \n")
    #outFile.write("\begin{preview} \n")
    outFile.write(df.to_latex())
    #outFile.write("\end{preview} \n")
    outFile.write("\end{document} \n")
    #outFile.write("\end{document}")
    #outFile.write("\n")
    outFile.close()
    #print(df.to_latex())
