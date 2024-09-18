# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3_pi_20k --datatier GEN-SIM-RECO,MINIAODSIM,DQMIO --runUnscheduled --conditions auto:run1_mc -s RAW2DIGI,L1Reco,RECO,RECOSIM,EI,PAT,VALIDATION:@standardValidationNoHLT+@miniAODValidation,DQM:@standardDQMFakeHLT+@miniAODDQM --eventcontent RECOSIM,MINIAODSIM,DQM -n 100 --filein file:step2.root --fileout file:step3.root
import FWCore.ParameterSet.Config as cms

#from Configuration.StandardSequences.Eras import eras
from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('ana',Run3)

# import of standard configurations
# process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
# process.load('Configuration.EventContent.EventContent_cff')
# process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
# process.load('Configuration.StandardSequences.MagneticField_cff')
# process.load('Configuration.StandardSequences.RawToDigi_cff')
# process.load('Configuration.StandardSequences.L1Reco_cff')
# process.load('Configuration.StandardSequences.Reconstruction_cff')
# process.load('Configuration.StandardSequences.RecoSim_cff')
# process.load('CommonTools.ParticleFlow.EITopPAG_cff')
# process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
# process.load('Configuration.StandardSequences.PATMC_cff')
# process.load('Configuration.StandardSequences.Validation_cff')
# process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2000000)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/0196f7c9-31b8-474c-9dee-5a7f4a7510dc.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/0788ebab-26eb-410e-97b0-868877d34e33.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/1542baa8-064c-4b32-bfb4-e0e40e8fae2f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/16a3abfd-74ff-42b2-90dd-1aa084608cd1.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/1da23793-f3b8-4296-9e79-144a34fc04ab.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/3789948d-7207-482d-b960-918b99e7ba5b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/389cfc20-348d-4167-9079-5cddc572fce4.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/42f1cbe4-4083-4ea3-9246-4c520a040444.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/578f9890-857c-40e2-9df9-8e1f44a8aee7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/67868896-3acf-4f30-8250-3fc771723b07.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/6a5f1415-4667-4f2e-b2d5-dc25020cf418.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/6d984b02-48d2-412e-8885-0b3adbe8b787.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/73fec87c-20d9-4b39-9979-ecd084bfd871.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/7542a8f3-ce4a-4b26-abf8-f9f010671f31.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/7f0d32ca-f9e5-4d6f-b65f-3b042f175d55.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/86f01179-051d-4ffc-917c-43bfd90bb178.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/8e0d1dfd-82f1-4dfa-961c-f6b615c117a5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/a6ee5282-ba96-4817-9539-e91bfea80157.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/aa173d85-3388-4d75-845c-70a065bf0bd3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/aee175e9-b743-452e-93f7-5095228dd8c9.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/b6c4be3c-acb6-4063-99aa-6bb69e8a10ee.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/bd4601b6-ed05-4a22-9454-d812077d32e3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/d3255075-1f91-41b8-a621-8a36fc5c196f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/d3872fdb-7f0a-4a84-bd6f-8881bb6e9f53.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/da7635e7-a521-405c-883e-5de372a09902.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/f617b577-253c-4328-b41f-ba08f468dd25.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/260000/f9bedc2a-1793-4de3-9824-dbf13986995f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/00443e74-868c-4296-ba12-60a2917d5f71.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/00a8234c-e159-4e2c-b07a-2e536cdd2262.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/00d81d69-d8d9-4484-97ca-6ca5e4a2d32b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0132c700-5f41-4906-ba55-5d164edffc9e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/020056fe-e540-4606-a08d-21cd705ce73a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0232cf71-4639-447f-806c-96d658ab10cd.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0400785c-8410-419a-9445-a1b3c8f169a3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/04a13bad-feb3-4178-9974-042f7b4aaa05.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/05a3d5e0-04e5-4f09-862a-41dd39e8dc01.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/05b50a75-8f1e-4355-af00-e54705e078ad.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/077ed42d-67f8-4f77-8ec4-6f2fe0465052.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/07a72061-6a81-426f-b0e6-d83a6ea98c85.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/07d5db03-5135-4458-91fd-1da8760ac97a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/07eb8430-ada9-4f9d-aad8-c6dd8ad04677.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0837d966-2521-48c6-82f1-26ad83437a48.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/088556e1-2ce8-4f24-b955-3c18ce2926d4.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/08bb55fe-0cc7-4575-83ee-21500b47ad34.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/08d1cf5e-c957-4ef9-ab5b-db0eb11ffd57.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/092e94d4-c821-415b-9721-62c6029bfb06.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0a2a418b-e3f5-4182-973a-e97aa9a534e9.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0a8817aa-b203-474f-8a49-11805d2ed729.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0bd58083-f75b-415f-bd28-ad970adfe596.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0c89427f-94c0-4744-b3f0-2f101569d752.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0c92c94b-1b84-4e96-93fc-bf5767e44e2b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0cbe114b-9aeb-4967-8269-11b9f50a1e33.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0d511784-4078-4666-aafb-763e1d79d62e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0f9e61e1-f588-4c23-bf35-15bda2d2c10b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/10a4782f-53db-41c4-8423-6046e58c300f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/10c725ef-5381-45ef-9777-22a01daf0c7d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1104c8b6-361f-41cf-b6b0-7f6dd54374b4.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1196084a-2cf7-4ed0-8cec-ae02dfd0ac53.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/11d7e16f-889f-49ef-9336-5595a81c4b29.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/11e1c5e2-f331-42d3-a22d-c7ddb65e368e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/12b12200-031a-4af2-b268-8faf04fa17ce.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/12bf1986-d811-476a-8c14-d742eabac95a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/12ecbab0-fb27-48d1-b0cf-d3879484a349.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/13115983-670d-41c4-b7b0-e8877cbcad86.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/13834576-0bca-4d87-b0fd-c13f21b754de.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/13a372b1-b6e5-4d67-9799-34a35e964f8b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/140241bc-e94a-4ef9-b501-e8aafa78b53d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1417eeb1-fd6b-417e-89eb-1f3981364dee.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/145d6657-e4fe-47df-a37f-c21a15bebbd1.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/14a5f95c-99d8-4561-bac4-963996e585b3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/14b27258-80dd-4c64-8bfd-85ba1a4cf0cd.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/14b27f89-d657-4bc9-9fda-063446834068.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/164b5f44-4b0a-4e65-a897-e2db87b6852d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/17c00260-2e45-4afc-ba50-15d99bb36fb5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/17caadba-8ae3-4fdd-9115-c23506b47346.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/17e8f90f-5b9d-45c0-a017-c7381e3e5345.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/18f27d6c-404c-4b0c-a6e9-95c97921ca8c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1921067c-15fd-4910-810f-8f097498669f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1965c8a3-b367-48d1-b200-58c3c1c753d8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/199a3e3b-e558-4cfe-a9c6-eac53c4d4938.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/19abcace-30b0-49ef-8ed3-2b4f58a6e868.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/19fb0423-1920-4fcd-9478-8ee5c23cbd4a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1a39f39d-b438-4f11-a8d6-77c4938c686f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1a68afcf-7674-4e97-8b05-0b2e728074de.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1b2e8b2f-e199-4a41-8ec0-5045bc212ed0.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1b5e3e15-fcce-417a-84a7-2fdfbbdd0026.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1b9626ff-5d14-4214-8c03-f409a63ee667.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1cb55e31-9665-4302-988d-5932abb640e1.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1cc2bd79-07e3-45b4-b78c-b18f413275a2.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1de7f3ba-2c6a-44a5-9a87-27e97a655872.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1e6fd9d0-4aea-4b90-815c-eef971eeb305.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/20158a92-60c2-4f0f-9102-21c5767f134f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/20cb7e69-45d6-4bdd-a861-443df097adec.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/21dfa1a8-993d-4120-a65f-9ccb7a5d528e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/22faee9c-aed1-4eba-9b42-31da36f8937c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/23aa48f8-2c5a-43d5-a012-5c17a7d70df2.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/23c0978a-9488-4cd9-9550-82cfabfceb0e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/23cbd738-048f-4f90-9905-802a713113cb.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/250baced-547f-42b3-83ea-9c8bd20622d8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/257a71ac-4a73-4506-9264-78c82e682301.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/261d67f1-b96a-4271-9baf-fbca8929a176.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/261d74bc-5124-4d3a-a72f-d0daf5200596.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/27eab5d0-d3b2-4e47-ab7c-cc6626b75f83.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2811e012-7537-4de3-86c4-09851ed9e06d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2833d574-a65e-44c6-9831-c35fcfb6f417.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/28d36881-4f09-4607-985a-7ea6a05e8c92.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/28f757fb-005b-4978-bd8d-4246ebe52652.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/29acfca1-05b0-470c-b0e9-4352869fb082.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/29ad5108-31c5-46db-9dde-60e33c41f126.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/29c4a0a9-d5c9-4e9c-a793-4fa9d5330843.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2aa523de-7c64-4b31-979c-bb11bd7ec489.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2b743339-2564-4415-8ac9-6f79d4eae446.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2c1a397e-9516-42d1-89eb-f6836a231c61.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2c501a9a-270b-4977-bd0b-58dc98e2a2ea.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2d8b46bf-5508-480e-8f91-caa0eaf4c5ee.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2ddcb778-379f-4f7d-b97e-8ee988399d26.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2df408e2-7154-4661-90b9-2a10938f23a2.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2e376a94-46d0-45c9-a5ee-26d037afb3b9.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2e69940f-c335-4d15-b5d9-ae1453aa9b96.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2e6f9485-1d20-44ff-85a5-a58b823ae286.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2ea8c2cc-1bc9-43da-afa5-be8da979bd44.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2ed0b9ed-fbd4-4153-89a4-5a870761f66e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2f19994e-519a-49d7-8ff0-6a0ab8436a0d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2f667659-9ff2-4776-9e30-5916b05ac8e7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/303a82e4-5bd1-4e3a-a0c5-f5e6e29b1869.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/308d3f7d-e746-4d18-8fd9-95017a598d03.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/31ab8fe7-7412-4070-9183-cfd72f318a35.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/31abad89-cac2-4b00-8329-814f75b51693.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3296d1ad-3f22-42ef-88e3-123580466c08.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/32df30f4-ad55-43f2-aa3b-737cd34fd6f1.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/32f94689-c6b3-4965-96cd-aed4cb723968.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/33387737-8b86-498b-b102-7f2d9fcd36de.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3382fc4f-b571-4b12-95d0-74b03a190df5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3489025b-f2e6-4bbb-99f5-92714f8ce2b2.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/350a4217-777b-4b40-bfe9-ca0cb3334d78.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/351f9d77-30ec-476e-8cdf-32d65dfd9aae.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/35ecbb2e-fc3a-4149-bea5-e8d873b90c65.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/368d4c1c-7b42-4db3-a31d-81ca36925e4f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/36db6e85-e6a7-456f-a9f2-a69bc9654787.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3716bd87-d087-4cf7-886b-c237adc8e198.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/376758b0-a731-4350-a2fb-046b66756341.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/379f4d43-6e7e-451d-bd89-261e30186953.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/38b553f4-3469-43fd-b326-f4dd9eaf00bc.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/390ed088-3a65-470c-827c-c0ee40c7c9ce.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/398b934a-b5d0-4fef-b4ea-5279c6250393.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/39cc70c2-a530-46fa-aa3b-e64878cbc071.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/39e49116-7c22-4c01-b78c-7914f6f11dcb.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/39f6c27e-730a-4fba-819a-f5a9a2509939.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3a152a9f-3c1c-4b4d-a67b-660d81c87eb3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3acfa9a1-7320-489e-9e02-142327bddc28.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3b4831c0-e35c-45db-9548-c74624df0ec4.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3bcd4a85-9057-49a9-ac78-40090491ab1c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3bcf0bca-bea9-47ab-8027-689c654bb3d7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3bd2d8b9-84e6-4d0d-92d7-aa60fa43b73c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3be84c65-7be6-4014-b7af-832350f6483c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3bec946a-7560-4ff0-8f45-c4724e01fb77.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3c00f21d-bb35-4bef-a3c0-d252dea01414.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3ca12038-9e99-4230-b717-28e144a87735.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3cda3720-017f-4778-b890-6fd854726b7e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3d1645c0-3e3d-436d-a37f-f8a2765c3923.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3d1c2bea-c4cb-4493-bdff-d044dfd95ea5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3e192972-3888-4d19-b3ff-0d98cb9ccd46.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3e33a20e-defe-4dcc-9592-7421e3f66800.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3e5ebefb-19e2-460a-ae68-575346e39501.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3ea7ff3c-3fcb-4228-8f4b-cce185998e28.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3f42c730-c03b-45d1-b3b1-21f9d1335da6.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3f607154-1267-4b94-8ddc-bcadd8446179.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3f7b8b2e-5c13-410e-8038-41fb5567b756.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4055d535-ab8d-4281-94bf-117129914dda.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/40c32f0c-ff40-4592-886e-20a3cd8b95d6.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/41aff3ea-dbbe-49d2-a405-3cf43f18316a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/42999b64-0e1e-440f-b8fa-1cec6f4dc241.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/43ad2bf2-a153-4dba-908b-a9d0da710dc9.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/43aebfeb-7bb7-436b-977d-0c5ad2ffc5c3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/43ea3460-194d-4263-a9cc-2444bd540914.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/448f28b8-7364-41d9-994d-e0189c659d0c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/449312fa-f3e3-4882-ae1f-ed6090509ff0.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4555ad4e-a665-42b0-b3a2-a2f0ea782c1d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/45b3c3dd-fafe-410e-a2a1-e7118090748d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/46321c40-e67e-4f8b-be5b-6d72586b7514.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/464a150a-7753-4b68-8e11-cbcdd0f9cb8e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/46a136d9-3c24-40b6-8c1a-6c50139aea0f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/46b8c2db-5259-43e5-a73c-ba472da5ef0e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/46e1c790-4396-4cf1-9ffd-f9b9008bdca8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/472b3840-0b7d-4757-940c-8cc4721837f1.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/478e4a20-287d-4a78-a876-327b202e195b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/487d3fc2-4705-44d0-b705-3bdbdbf6e5b8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/48b45c8c-69d1-405f-ba09-dc1a026d5447.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/48f4f20c-248f-47b1-9ae8-c6441637c5e0.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/49366434-bc1c-48e8-a5e5-bc62c6a45c50.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4975639b-9905-4d05-819d-422ec110436c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4aa26e13-50e4-412a-9019-35fbfd9c58ac.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4aa29ee3-880f-46b2-b935-938ae3fe858e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4abb597e-f79f-4500-b34e-36eb021c81e7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4b674b5c-9954-4f4f-a611-8076490a25f8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4b721ac8-c09e-46e3-ba9c-d14badc55c59.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4c51fb52-a58d-4db0-bca8-84d1da1b0c93.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4c79a475-71b2-42b9-92ef-4a1fbcac1594.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4c8d4e83-a661-4ba7-a327-7d6926b52758.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4d0ceaf8-630b-45eb-8fbd-cd74f912f2a9.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4d49c742-1be0-4326-8553-362b697ff889.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4dee9d98-5217-4121-a2e4-bc1de1846744.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4dfa8138-fd00-443d-92a6-bbc1e8944457.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4e5c28cd-9657-464d-be11-b8a216c2cea8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4e7c467d-7ef4-49ec-bb38-61e894eef6ab.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4ed44788-afac-490a-af4c-9a5e34288fb5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4ef0d37a-60cd-438d-987d-5f5304c41579.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4fb60ccc-4dc3-403d-a15a-ae0bb9802432.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4fcc32fd-3c25-4798-9824-f5129eaa3fc8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4fd2842e-fcc8-40c0-a76e-8fa6490386bd.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4fe6dcf2-5188-45d7-ad5d-b13513770f00.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/505a518b-f3e0-4abb-8d21-a247ea8bf222.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5178ee6c-9c47-4948-ba75-94a5bf166587.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/52031a80-d395-45d3-ad1a-c37b97aa28f2.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/53db38f4-9457-46f9-b2bf-2ff82f1b102c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/53dceaa2-81e7-44bd-8e6a-417b206c7ee5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/53e54fef-0f39-4954-af4c-7a13482843bb.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5473c376-ea02-458d-87fe-f7d46834245c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/54814121-6da1-4504-8e71-2c1623bb017f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/560690a3-798c-4922-9dbf-128e02ca133b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5625fe83-678c-47fd-870b-e0fd8091afa8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/56683c57-1d28-4c17-a4ee-329488148454.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/56a93649-3c0a-4cd4-b72d-afffec614d6f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/571b9635-8e16-486f-a50f-4f8a21c34757.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/571d85a9-b332-4466-93d2-f5f398d41cff.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/57785158-8cb9-432d-bb40-51e81aa4ab37.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/57a2d98b-be10-4df8-8042-006bb4718dc8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5834624c-cfdd-4a8d-8c0d-9f9f1767549c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/58561a6b-494d-4e18-aa62-2eb4d7d4d711.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/585e04db-f5ea-41ac-a9d5-6db726adb913.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5884faaf-8d9e-4dd0-b748-6940bec3969a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/58921a41-b66b-4cf0-a7ad-abbd4fd931ce.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/58ccbd53-3d4c-4635-bab0-0edc835cd2b1.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5a398017-768b-4150-933d-36cd3c8d591d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5ae3a53e-3190-4119-ba0f-cf89d75e3d51.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5b891dff-82a2-4c28-ad0b-16ae1e2113ac.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5d60af44-4a31-407e-89a2-14dccc919260.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5dbfbcfe-cef2-45e5-a731-80fe9742934a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5e21721a-f1d0-4574-95c4-e40adf18f45f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5e448ee6-2e8c-4116-ae64-a71412a1bf5a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5f0273df-169e-4cce-ba11-79fcce2c4a5b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5f76822d-4065-4f9c-81eb-a597f798c66f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5f858d7d-4f14-4b60-a817-077248e9599f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/600ca264-d6c3-47d6-af65-97a89da2f10f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6047d991-375e-4278-9a93-e154b7e6bb71.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/60d5e495-d4ae-4d97-8d1d-074dc345e095.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6107464b-a245-443f-9681-149994c2e21a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/617ac2b0-b172-40ae-a6e4-935c9fa04ec4.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/617d613a-98bc-40ad-8340-f5eef283b22e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/618051f3-f095-45b0-93af-f02da41277dd.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/61a06aed-7624-4217-92db-3fae0bd5b3d0.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/627da216-3760-4739-a622-6b07eb1121aa.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/627ed5b0-52fc-40ec-b5b9-4b45f7b0fa23.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/63258e49-9e44-4e9c-a7b4-70466a95e776.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/63976a6c-714b-4d5b-9b28-7426a059d3f8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6404cde1-444c-40fc-acb1-a34ebdfc3b25.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/65585411-a646-42c1-97b4-a40edd445ff7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/65644dd3-a4e9-42cf-8fb9-ee2939c93918.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/659e55fe-fb57-46ec-b1c5-b6d414b65d37.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/66b1cf95-7dc3-4321-b2a4-a3ffee598434.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/66f8dc2f-34c3-4744-a032-010ff8ebade1.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6778225a-5d94-4656-9143-8779a54276f2.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/67b9370a-b003-4f7a-b32e-605a8450965f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6805964b-7e34-4b0d-a0ec-5ef46cb7f218.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6813106d-5eaf-4b1a-992f-6f9b044bdd7c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6819510f-abd7-41dd-8040-f05332f01d97.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/68d60bea-e4db-48e9-a579-c718832c5694.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/695a93f8-ef38-4df5-80c0-1d66243ebaab.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/69a88b84-415e-4e79-9820-f619ee9ebf18.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/69cc413d-2c1c-4a20-b349-40d5cd1b1695.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/69f5caac-3c5e-40be-99b9-9166ec0bdc1a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6a2a70f1-0f09-435e-a944-7caa4b1bdbcb.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6a7dcf0a-be2e-4f42-9e32-e401a654847c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6a984557-00db-4d16-80d4-6e68465332a4.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6abcf807-22a1-4abb-a9cb-5a9c80d85cc3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6afc03ca-0add-41e2-860a-26c62ace9971.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6b858615-b443-44d9-af3b-a306895d183b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6be0955a-e7a5-42a8-8398-d0ff8d27e5c5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6c1fe198-b99b-42a2-b511-e5d78629b72a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6c726dae-a0ef-4643-8c3b-03d2da4c23d6.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6caecf0c-bdda-4826-8767-6341b4ad3bdd.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6d35f14e-5c42-414f-979b-db39a57ee565.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6d694658-8a7e-4c5f-839e-a7568e52eaf3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6da2c62f-3acc-46f9-b6c4-9af8139cbc2b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6db1058a-68b3-44d2-92ad-60d7aa66d646.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6dd3b1c4-97e6-48fc-82e2-83f7c47245bc.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6de58416-9f25-4b02-97bf-734bcfb5b47e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6deac259-8a83-4806-ab13-e90427aeb09d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6e2d9ad9-4dd1-4f7b-9c84-47ab0efe3dfa.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6e35cbed-4ae4-47b5-a35f-f9f8befb3236.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6e6fa5e4-b775-44a0-8021-a406bd66e289.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6e884456-6453-405e-ba07-7b0c63cb62be.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6ef5d000-fb07-416f-baf8-c6d2c1be5f3e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6f1baf87-2d33-4ef3-af0e-01b49f19213f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6fffe267-6402-4a17-a6cd-0443a59be6fa.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/70812849-1432-4472-80bf-30a9c4117b34.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/7092f84e-ebf5-4dd0-b386-8b8d53764aa3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/70a7f457-8961-48bd-b498-ea6b5a055ebf.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/70e0fc65-e0bf-4f43-9bfa-458af82c0241.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_200to500_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/7109d9c7-9169-4514-a37b-cff9f095fac0.root',
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
)

####################

from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_mc', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '100X_upgrade2018_realistic_v10', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '100X_mc2017_realistic_v3', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2018_realistic', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '120X_mcRun3_2021_realistic_v5', '')

process.pfChargedHadronAnalyzer = cms.EDAnalyzer(
    "PFChargedHadronAnalyzer",
    genParticles = cms.InputTag("genParticles"),
    PFCandidates = cms.InputTag("particleFlow"),
    PFSimParticles = cms.InputTag("particleFlowSimParticle"),
    EcalPFClusters = cms.InputTag("particleFlowClusterECAL"),
    HcalPFClusters = cms.InputTag("particleFlowClusterHCAL"),
    ptMin = cms.double(1.),                     # Minimum pt
    pMin = cms.double(1.),                      # Minimum p
    nPixMin = cms.int32(2),                     # Nb of pixel hits
    nHitMin = cms.vint32(14,17,20,17,10),       # Nb of track hits
    nEtaMin = cms.vdouble(1.4,1.6,2.0,2.4,2.6), # in these eta ranges
    hcalMin = cms.double(0.5),                  # Minimum hcal energy
    ecalMax = cms.double(1E9),                  # Maximum ecal energy
    verbose = cms.untracked.bool(True),         # not used.
    rootOutputFile = cms.string("SinglePion_200to500_Run3Summer21.root"),# the root tree
#   IsMinBias = cms.untracked.bool(False)
)

process.load("RecoParticleFlow.PFProducer.particleFlowSimParticle_cff")

from FastSimulation.Event.ParticleFilter_cfi import  ParticleFilterBlock
process.particleFlowSimParticle.ParticleFilter = ParticleFilterBlock.ParticleFilter.copy()
process.particleFlowSimParticle.ParticleFilter.chargedPtMin = cms.double(0.0)
process.particleFlowSimParticle.ParticleFilter.EMin = cms.double(0.0)
#process.load("FastSimulation.Event.ParticleFilter_cfi")
#process.particleFlowSimParticle.ParticleFilter = cms.PSet(
#        # Allow *ALL* protons with energy > protonEMin
#        protonEMin = cms.double(5000.0),
#        # Particles must have abs(eta) < etaMax (if close enough to 0,0,0)
#        etaMax = cms.double(5.3),
#        # Charged particles with pT < pTMin (GeV/c) are not simulated
#        chargedPtMin = cms.double(0.0),
#        # Particles must have energy greater than EMin [GeV]
#        EMin = cms.double(0.0)
#)

process.genReReco = cms.Sequence(
    process.particleFlowSimParticle
)

# Path and EndPath definitions

process.EDA = cms.EndPath(process.pfChargedHadronAnalyzer)
process.gRR = cms.EndPath(process.genReReco)

process.schedule = cms.Schedule(process.gRR,process.EDA)
#process.schedule = cms.Schedule(process.EDA)
