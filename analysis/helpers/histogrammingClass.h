#include <TH1F.h>
#include <TFile.h>

class categoryHistogram{
    private:
        TH1F* h_nJet;
        TH1F* h_nBJet;
        TH1F* h_nGoodLeps;
        TH1F* h_leadLepPt;
        TH1F* h_leadLepEta;
        TH1F* h_leadLepMass;
        TH1F* h_leadLepMiniIso;
        TH1F* h_leadLepPtRel;
        TH1F* h_leadLepPtRatio;
        TH1F* h_leadJetPt;
        TH1F* h_leadBPt;
        TH1F* h_leadBMass;
        TH1F* h_jetHT;
        TH1F* h_MET;
        TH1F* h_minMT;
        TH1F* h_MT_b_MET;

    public:
        /*int nJet;
        int nBJet;
        int nLep;
        int nFO;
        bool isSS;
        bool isSF;*/

        //constructor will create all histograms for each region category
        categoryHistogram(string numLep, string numJet, string numB, string sampleName){
            h_nJet = new TH1F( ("h_nJet_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "nJets", 7, -0.5, 6.5 );
            h_nBJet = new TH1F( ("h_nBJet_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "nBjets", 4, -0.5, 3.5 );
            h_nGoodLeps = new TH1F( ("h_nGoodLeps_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "nGoodLeps", 6, -0.5, 5.5 );
            h_leadLepPt = new TH1F( ("h_leadLepPt_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "leadLepPt", 50, 0, 500 );
            h_leadLepEta = new TH1F( ("h_leadLepEta_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "leadLepEta", 20, -5, 5 );
            h_leadLepMass = new TH1F( ("h_leadLepMass_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "leadLepMass", 500, 0, 1 );
            h_leadLepMiniIso = new TH1F( ("h_leadLepMiniIso_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "leadLepMiniIso", 10, 0, 0.5 );
            h_leadLepPtRel = new TH1F( ("h_leadLepPtRel_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "leadLepPtRel", 50, 0, 10 );
            h_leadLepPtRatio = new TH1F( ("h_leadLepPtRatio_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "leadLepPtRatio", 50, 0, 5 );
            h_leadJetPt = new TH1F( ("h_leadJetPt_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "leadJetPt", 50, 0, 500 );
            h_leadBPt = new TH1F( ("h_leadBPt_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "leadBPt", 50, 0, 500 );
            h_leadBMass = new TH1F( ("h_leadBMass_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "leadBMass", 50, 0, 500 );
            h_jetHT = new TH1F( ("h_jetHT_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "jetHT", 100, 0, 1000 );
            h_MET = new TH1F( ("h_MET_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "MET", 50, 0, 500 );
            h_minMT = new TH1F( ("h_minMT_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "minMT", 50, 0, 500 );
            h_MT_b_MET = new TH1F( ("h_MT_b_MET_"+numLep+"_"+numJet+"_"+numB+"_"+sampleName).c_str(), "MT_b_MET", 50, 0, 500 );
        } 

        //methods to fill and save histograms
        void fillHistogram(vector<float> variables, float weight){
            h_nJet->Fill(variables[0], weight);
            h_nBJet->Fill(variables[1], weight);
            h_nGoodLeps->Fill(variables[2], weight);
            h_leadLepPt->Fill(variables[3], weight);
            h_leadLepEta->Fill(variables[4], weight);
            h_leadLepMass->Fill(variables[5], weight);
            h_leadLepMiniIso->Fill(variables[6], weight);
            h_leadLepPtRel->Fill(variables[7], weight);
            h_leadLepPtRatio->Fill(variables[8], weight);
            h_leadJetPt->Fill(variables[9], weight);
            h_leadBPt->Fill(variables[10], weight);
            h_leadBMass->Fill(variables[11], weight);
            h_jetHT->Fill(variables[12], weight);
            h_MET->Fill(variables[13], weight);
            h_minMT->Fill(variables[14], weight);
            h_MT_b_MET->Fill(variables[15], weight);
        }

        void writeHistogram(TFile* &outfile){
            if (outfile->IsOpen()){
                h_nJet->Write();
                h_nBJet->Write();
                h_nGoodLeps->Write();
                h_leadLepPt->Write();
                h_leadLepEta->Write();
                h_leadLepMass->Write();
                h_leadLepMiniIso->Write();
                h_leadLepPtRel->Write();
                h_leadLepPtRatio->Write();
                h_leadJetPt->Write();
                h_leadBPt->Write();
                h_leadBMass->Write();
                h_jetHT->Write();
                h_MET->Write();
                h_minMT->Write();
                h_MT_b_MET->Write();
            }
        }

};
