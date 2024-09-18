//#include "RecoParticleFlow/Configuration/test/PFChargedHadronAnalyzer.h"
#include "PFCalibration/PFChargedHadronAnalyzer/plugins/PFChargedHadronAnalyzer.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowReco/interface/PFBlock.h"
#include "DataFormats/ParticleFlowReco/interface/PFBlockElementTrack.h"
#include "DataFormats/ParticleFlowReco/interface/PFBlockElementCluster.h"

#include "DataFormats/ParticleFlowReco/interface/PFCluster.h"
#include "DataFormats/ParticleFlowReco/interface/PFRecHit.h"
#include "DataFormats/ParticleFlowReco/interface/PFRecHitFraction.h"

#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h" 
#include "DataFormats/EcalRecHit/interface/EcalUncalibratedRecHit.h" 
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h" 
#include "DataFormats/HcalRecHit/interface/HcalRecHitDefs.h"

#include "FWCore/Framework/interface/ESHandle.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "SimDataFormats/CaloHit/interface/PCaloHit.h"

#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"


#include <TROOT.h>
#include <TVector3.h>
#include "DataFormats/Math/interface/deltaR.h"

//#include "PFChargedHadronAnalyzer.h"
using namespace std;
using namespace edm;
using namespace reco;

PFChargedHadronAnalyzer::PFChargedHadronAnalyzer(const edm::ParameterSet& iConfig) {
  
  nEv = std::vector<unsigned int>(5,static_cast<unsigned int>(0));

  inputTaggenParticles_ 
    = iConfig.getParameter<InputTag>("genParticles");
  tokengenParticles_ = consumes<reco::GenParticleCollection>(inputTaggenParticles_);

  inputTagPFCandidates_ 
    = iConfig.getParameter<InputTag>("PFCandidates");
  tokenPFCandidates_ = consumes<reco::PFCandidateCollection>(inputTagPFCandidates_);
 
  //std::cout << "Check point 1 " << std::endl;

  inputTagPFSimParticles_ 
    = iConfig.getParameter<InputTag>("PFSimParticles");
  tokenPFSimParticles_ = consumes<reco::PFSimParticleCollection>(inputTagPFSimParticles_);

  inputTagEcalPFClusters_ 
    = iConfig.getParameter<InputTag>("EcalPFClusters");
  tokenEcalPFClusters_ = consumes<reco::PFClusterCollection>(inputTagEcalPFClusters_);

  // Smallest track pt
  ptMin_ = iConfig.getParameter<double>("ptMin");

  // Smallest track p
  pMin_ = iConfig.getParameter<double>("pMin");

  // Smallest raw HCAL energy linked to the track
  hcalMin_ = iConfig.getParameter<double>("hcalMin");

  // Largest ECAL energy linked to the track to define a MIP
  ecalMax_ = iConfig.getParameter<double>("ecalMax");

  // Smallest number of pixel hits
  nPixMin_ = iConfig.getParameter<int>("nPixMin");

  // Smallest number of track hits in different eta ranges
  nHitMin_ = iConfig.getParameter< std::vector<int> > ("nHitMin");
  nEtaMin_ = iConfig.getParameter< std::vector<double> > ("nEtaMin");

  //Is minbias from simulation
  isMBMC_ = iConfig.getUntrackedParameter<bool>("isMinBiasMC",false);

  verbose_ = 
    iConfig.getUntrackedParameter<bool>("verbose",false);

  LogDebug("PFChargedHadronAnalyzer")
    <<" input collection : "<<inputTagPFCandidates_ ;
   

  // The root tuple
  outputfile_ = iConfig.getParameter<std::string>("rootOutputFile"); 
  tf1 = new TFile(outputfile_.c_str(), "RECREATE");  
  s = new TTree("s"," PFCalibration");

  //Gen particle
  s->Branch("genE",  &genE_,  "genE/F");
  s->Branch("genP",  &genP_,  "genP/F");
  s->Branch("genEta",&genEta_,"genEta/F");
  s->Branch("genPhi",&genPhi_,"genPhi/F");

  //PF particle
  s->Branch("pfE",  &pfE_,  "pfE/F");
  s->Branch("pfP",  &pfP_,  "pfP/F");
  s->Branch("pfEta",&pfEta_,"pfEta/F");
  s->Branch("pfPhi",&pfPhi_,"pfPhi/F");

  //TRK
  s->Branch("trkP", &trkP_, "trkP/F");

  //Resolutions
  s->Branch("trkReso",  &trkReso_,  "trkReso/F");
  s->Branch("caloReso", &caloReso_, "caloReso/F");

  s->Branch("w", &w_, "w/F");

  //Calo
  s->Branch("ecal",    &ecal_,    "ecal/F");
  s->Branch("hcal",    &hcal_,    "hcal/F");
  s->Branch("calo",    &calo_,    "calo/F");

  s->Branch("rawEcal", &rawEcal_, "rawEcal/F");
  s->Branch("rawHcal", &rawHcal_, "rawHcal/F");
  s->Branch("rawCalo", &rawCalo_, "rawCalo/F");

  s->Branch("run",&orun,"orun/l");
  s->Branch("evt",&oevt,"orun/l");
  s->Branch("lumiBlock",&olumiBlock,"orun/l");
  s->Branch("time",&otime,"orun/l");
}



PFChargedHadronAnalyzer::~PFChargedHadronAnalyzer() { 

  std::cout << "Total number of events ......... " << nEv[0] << std::endl;
  std::cout << "Events with one Sim Particle.... " << nEv[1] << std::endl;
  std::cout << "0  PF particle.................. " << nEv[2] << std::endl;
  std::cout << "1  PF particle.................. " << nEv[3] << std::endl;
  std::cout << ">1 PF particle.................. " << nEv[4] << std::endl;

  tf1->cd();
  s->Write();

  tf1->Write();
  tf1->Close();  
}



void 
PFChargedHadronAnalyzer::beginRun(const edm::Run& run, 
				  const edm::EventSetup & es) { }


void 
PFChargedHadronAnalyzer::analyze(const Event& iEvent, 
				 const EventSetup& iSetup) {
  
  LogDebug("PFChargedHadronAnalyzer")<<"START event: "<<iEvent.id().event()
			 <<" in run "<<iEvent.id().run()<<endl;
  

   edm::ESHandle<CaloGeometry> pCalo;
   iSetup.get<CaloGeometryRecord>().get( pCalo );
   theCaloGeom = pCalo.product();



  run  = iEvent.id().run();
  evt  = iEvent.id().event();
  lumiBlock = iEvent.id().luminosityBlock();
  time = iEvent.time();

  orun = (size_t)run;
  oevt = (size_t)evt;
  olumiBlock = (size_t)lumiBlock;
  otime = (size_t)((iEvent.time().value())>>32);

  //get genParticles
  Handle<GenParticleCollection> genParticles;
  iEvent.getByToken(tokengenParticles_, genParticles);

  // get PFCandidates
  Handle<PFCandidateCollection> pfCandidates;
  iEvent.getByToken(tokenPFCandidates_, pfCandidates);

  //get Ecal PFClusters
  Handle<reco::PFClusterCollection> pfClustersEcal;
  iEvent.getByToken(tokenEcalPFClusters_, pfClustersEcal);

  Handle<PFSimParticleCollection> trueParticles;
  //FIXME
  //bool isSimu = iEvent.getByLabel(inputTagPFSimParticles_,trueParticles);
  // bool isMBMC=true;
  bool isSimu = iEvent.getByToken(tokenPFSimParticles_, trueParticles);

  //simHits
  EcalSimHits.clear();
  ESSimHits.clear();
  HcalSimHits.clear();
  
  //recHits
  EcalRecHits.clear();
  ESRecHits.clear();
  HcalRecHits.clear();
  EcalRecHitsDr.clear();
  ESRecHitsDr.clear();
  HcalRecHitsDr.clear();

  if(isMBMC_) isSimu=false;
 

  if ( isSimu ) { 
    nEv[0]++;
    if ( (*trueParticles).size() != 1 ) return;
    nEv[1]++;

    // Initialize
    genE_ = 0.;
    genP_ = 0.;
    genEta_ = 0.;
    genPhi_ = 0.;

    pfE_ = 0.;
    pfP_ = 0.;
    pfEta_ = 0.;
    pfPhi_ = 0.;

    trkP_ = 0.;

    trkReso_ = 0.;
    caloReso_ = 0.;

    w_ = 0.;

    calo_    = 0.;
    ecal_    = 0.;
    hcal_    = 0.;
    rawCalo_ = 0.;
    rawEcal_ = 0.;
    rawHcal_ = 0.;

    genE_   = (*genParticles)[0].p4().E();
    genP_   = (*genParticles)[0].p4().P();
    genEta_ = (*genParticles)[0].p4().Eta();
    genPhi_ = (*genParticles)[0].p4().Phi();


    //Gen pi+
    for (unsigned int i=0; i<(*genParticles).size(); ++i) {
      /*
      cout << "GenId: " << (*genParticles)[i].pdgId() 
           << " Eta: "  << (*genParticles)[i].p4().Eta() 
           << " Phi: "  << (*genParticles)[i].p4().Phi()
           << " E: "    << (*genParticles)[i].p4().E() << endl;*/
    }

    //Loop over PF candidates

    int n_pf = 0;

    for( CI ci  = pfCandidates->begin(); ci!=pfCandidates->end(); ++ci)  {
      const reco::PFCandidate& pfc = *ci;


      if (pfc.particleId() == 1) {

        //cout << "Id: " << pfc.particleId() << " Eta: " << pfc.eta() << " Phi: " << pfc.phi()
        //     << " rawEcal: " << pfc.rawEcalEnergy() << " rawHcal: " << pfc.rawHcalEnergy()
        //     << " P: " << pfc.p() << " E: " << pfc.energy() << endl;

        //cout << "E candidate     " << pfc.energy() << endl;
        //cout << "corrected Ecal  " << pfc.ecalEnergy() << endl;
        //cout << "corrected Hcal  " << pfc.hcalEnergy() << endl;
        //cout << "corrected Calo  " << pfc.ecalEnergy() + pfc.hcalEnergy() << endl;
        //cout << "raw Ecal        " << pfc.rawEcalEnergy() << endl;
        //cout << "raw Hcal        " << pfc.rawHcalEnergy() << endl;
        //cout << "raw Calo        " << pfc.rawEcalEnergy() + pfc.rawHcalEnergy() << endl;

        ecal_    = pfc.ecalEnergy();
        hcal_    = pfc.hcalEnergy();
        calo_    = ecal_ + hcal_;

        rawEcal_ = pfc.rawEcalEnergy();
        rawHcal_ = pfc.rawHcalEnergy();
        rawCalo_ = rawEcal_ + rawHcal_;

        pfE_   = pfc.p4().E();
        pfP_   = pfc.p4().P();
        pfEta_ = pfc.p4().Eta();
        pfPhi_ = pfc.p4().Phi();

        trkP_  = pfc.trackRef()->p();

        double deta = genEta_ - pfEta_;
        double dphi = dPhi(genPhi_, pfPhi_);
        double dR   = std::sqrt(deta*deta+dphi*dphi);

        caloReso_ = neutralHadronEnergyResolution(pfc.trackRef()->p(), pfc.p4().Eta()) * pfc.trackRef()->p();

        trkReso_ = pfc.trackRef()->qoverpError() * pfc.trackRef()->p() * pfc.trackRef()->p();

        //cout << caloResolution << " " << trkResolution << endl;

        w_ = (caloReso_*caloReso_)/(caloReso_*caloReso_ + trkReso_*trkReso_);

        //cout << pfP_ << " " << calo_ << " " << trkP_ << " " << w << " " << w*trkP_ + (1-w)*calo_ <<endl;


        n_pf ++;

      }
    }

    if (n_pf == 0) nEv[2]++;
    else if (n_pf == 1) nEv[3]++;
    else nEv[4]++;
    if (n_pf != 1) return;


    s->Fill();
    return;
  }
}


float PFChargedHadronAnalyzer::dR(float eta1, float eta2, float phi1, float phi2 ) {

  TVector3 v1(0,0,0),v2(0,0,0);
  
  v1.SetPtEtaPhi(1, eta1, phi1);
  v2.SetPtEtaPhi(1, eta2, phi2);

  return v1.DrEtaPhi( v2 );
  
}


void PFChargedHadronAnalyzer::SaveSimHit(const edm::Event& iEvent,  float eta_, float phi_) {

  //Access to simHits informations
  Handle<PCaloHitContainer> h_PCaloHitsEB;
  iEvent.getByLabel("g4SimHits","EcalHitsEB", h_PCaloHitsEB);

  Handle<PCaloHitContainer> h_PCaloHitsEE;
  iEvent.getByLabel("g4SimHits","EcalHitsEE", h_PCaloHitsEE);

  Handle<PCaloHitContainer> h_PCaloHitsES;
  iEvent.getByLabel("g4SimHits","EcalHitsES", h_PCaloHitsES);
  
  Handle<PCaloHitContainer> h_PCaloHitsH;
  iEvent.getByLabel("g4SimHits","HcalHits", h_PCaloHitsH);

  //iterator
  PCaloHitContainer::const_iterator genSH;

  //match hits... dR 0.2, should contains all simHits
  
  //ECAL
  if( fabs(eta_) <1.5 ) { //barrel
    
    for(genSH = h_PCaloHitsEB->begin(); genSH != h_PCaloHitsEB->end(); genSH++) {
      // float theta = genSH->thetaAtEntry();
      // float phi = genSH->phiAtEntry();
      // float eta = Eta( theta );
      // float dr = dR( eta, eta_, phi, phi_ );
      
      // if(dr > 0.2 ) continue;
      //cout<<" ecal hit : "<<genSH->energy()<<endl;
      EcalSimHits.push_back( genSH->energy() );
    }
  }
  else {
    
    for(genSH = h_PCaloHitsEE->begin(); genSH != h_PCaloHitsEE->end(); genSH++) {
      // float theta = genSH->thetaAtEntry();
      // float phi = genSH->phiAtEntry();
      // float eta = Eta( theta );
      // float dr = dR( eta, eta_, phi, phi_ );

      // if(dr > 0.2 ) continue;
      EcalSimHits.push_back( genSH->energy() );
    }    

    for(genSH = h_PCaloHitsES->begin(); genSH != h_PCaloHitsES->end(); genSH++) {
       // float theta = genSH->thetaAtEntry();
       // float phi = genSH->phiAtEntry();
       // float eta = Eta( theta );
       // float dr = dR( eta, eta_, phi, phi_ );

       // if(dr > 0.2 ) continue;
       ESSimHits.push_back( genSH->energy() );
    }    
  }
  
  //Hcal
  float sH=0; 
  for(genSH = h_PCaloHitsH->begin(); genSH != h_PCaloHitsH->end(); genSH++) {
    // float theta = genSH->thetaAtEntry();
    // float phi = genSH->phiAtEntry();
    // float eta = Eta( theta );
    // float dr = dR( eta, eta_, phi, phi_ );
       // if(dr > 0.2 ) continue;
    sH += genSH->energy();
    //cout<<" ecal hit : "<<genSH->energy()<<"    "<<genSH->energyEM()<<"   "<<genSH->energyHad()<<"   "<<sH<<endl;
       HcalSimHits.push_back( genSH->energy() );
    }

}


float PFChargedHadronAnalyzer::Eta( float theta_ ) {
  if( sin(theta_/2.)==0 ) return 10000.*cos(theta_/2.);
  return -log(tan(theta_/2.0));
}


void PFChargedHadronAnalyzer::SaveRecHits(const edm::Event& iEvent, float eta_, float phi_) {

  //get rechits
  edm::Handle< EcalRecHitCollection > ebRecHits_h;
  edm::Handle< EcalRecHitCollection > eeRecHits_h;
  edm::Handle< EcalRecHitCollection > esRecHits_h;
 // Barrel
  iEvent.getByLabel( "ecalRecHit","EcalRecHitsEB", ebRecHits_h );
  // Endcaps
  iEvent.getByLabel( "ecalRecHit","EcalRecHitsEE", eeRecHits_h );
  // Preshower
  iEvent.getByLabel( "ecalRecHit","EcalRecHitsES", esRecHits_h );
  // Hcal
  edm::Handle< HBHERecHitCollection > hbheRecHits_h;
  iEvent.getByLabel( "hbhereco","", hbheRecHits_h );
  

  for( size_t ii =0; ii < ebRecHits_h->size(); ++ii )
    {
      EcalRecHitRef recHitRef( ebRecHits_h, ii );
      EBDetId id = recHitRef->id();

      const  GlobalPoint & rhPos = theCaloGeom->getPosition( id );
      float eta = rhPos.eta();
      float phi = rhPos.phi();
      float dr = dR( eta, eta_, phi, phi_ );
      if(dr > 0.1 ) continue;
      //cout<<"EB : "<<dr<<"  "<<recHitRef->energy()<<endl;
      EcalRecHits.push_back( recHitRef->energy() );
      EcalRecHitsDr.push_back( dr );
    }

  for( size_t ii =0; ii < eeRecHits_h->size(); ++ii )
    {
      EcalRecHitRef recHitRef( eeRecHits_h, ii );
      EEDetId id = recHitRef->id();

      const  GlobalPoint & rhPos = theCaloGeom->getPosition( id );
      float eta = rhPos.eta();
      float phi = rhPos.phi();
      float dr = dR( eta, eta_, phi, phi_ );
      if(dr > 0.1 ) continue;
      EcalRecHits.push_back( recHitRef->energy() );
      EcalRecHitsDr.push_back( dr );
    }


  for( size_t ii =0; ii < hbheRecHits_h->size(); ++ii )
    {
      HBHERecHitRef recHitRef( hbheRecHits_h, ii );
      HcalDetId id = recHitRef->id();

      const  GlobalPoint & rhPos = theCaloGeom->getPosition( id );
      float eta = rhPos.eta();
      float phi = rhPos.phi();
      float dr = dR( eta, eta_, phi, phi_ );
      if(dr > 0.15 ) continue;
      //cout<<"Hcal : "<<dr<<"  "<<recHitRef->energy()<<endl;
      HcalRecHits.push_back( recHitRef->energy() );
      HcalRecHitsDr.push_back( dr );
    }

  

}

float 
PFChargedHadronAnalyzer::phi( float x, float y ) {
  float phi_ =atan2(y, x);
  return (phi_>=0) ?  phi_ : phi_ + 2*3.141592;
}

float 
PFChargedHadronAnalyzer::dPhi( float phi1, float phi2 )
{
  float phi1_= phi( cos(phi1), sin(phi1) );
  float phi2_= phi( cos(phi2), sin(phi2) );
  float dphi_= phi1_-phi2_;
  if( dphi_> 3.141592 ) dphi_-=2*3.141592;
  if( dphi_<-3.141592 ) dphi_+=2*3.141592;
  return dphi_;
}


double PFChargedHadronAnalyzer::neutralHadronEnergyResolution(double clusterEnergyHCAL, double eta) {
  // Add a protection
  clusterEnergyHCAL = std::max(clusterEnergyHCAL, 1.);

  double resol = fabs(eta) < 1.48 ? sqrt(1.02 * 1.02 / clusterEnergyHCAL + 0.065 * 0.065)
                                  : sqrt(1.20 * 1.20 / clusterEnergyHCAL + 0.028 * 0.028);

  return resol;
}




DEFINE_FWK_MODULE(PFChargedHadronAnalyzer);
