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
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/011144cf-49d4-44d6-86a4-c6d8c22def4a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/014c5d67-e23d-4502-ac25-413b6670feea.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/01a5273b-201a-4d09-ac39-8bbffb95f171.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/01adeb04-8941-42b2-bc4a-fd54a321a490.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/01e7d876-680a-44f8-8862-54cf44185ab3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0250d00f-38d3-4905-88dc-211f0c53f5d7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/02c4ed0f-793a-491b-aac3-cd5736ae7e56.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/02c71912-7d99-462c-a106-324ae1d8d2a9.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/02f03be6-e192-4811-bf41-f0b23c0e2f11.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/038373ee-b511-4896-b710-921bac23847f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/03d4868b-304e-46d3-9d5b-c829c87efede.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/03f424d4-7971-4f92-bd0e-9fd1b866203d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0437ebd7-36cd-4a0c-a037-c65ec741da65.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/048c8d71-9584-4c4a-b226-eb5f57132828.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/049c0f38-c8fd-4d0b-9efe-cd3d90181a24.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/050ff3e2-089c-41fe-90b6-056e43a9f7a8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/05bce23e-cb82-4c04-bc3f-2c5d339022d9.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/05bf6b17-f2f9-43ce-9e3c-5226736ece2a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/067db04b-26dd-4bd7-9517-46dcbdb418c5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/06ae11c9-2bfd-4100-a4d5-d9c99e48879d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0762258a-6076-4af4-9859-6d2bf5b8aa0a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/07a3012c-9c06-4c25-aeb5-bc81dad7612e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/07b6faf5-d9ff-4ad8-b327-53567061339e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/08edb82e-e3a1-448e-b0d8-2be7336c2d45.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/093d4332-4722-4a9b-a7e5-de10c099996c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/096af029-d126-416b-a542-0d9c305f69db.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/09827bef-1278-4e89-8447-103a893abfb4.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/09b2130d-3b89-438c-b8ea-06f849120981.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0b3ee3ba-9c36-422a-bcea-0ebdbf2fef77.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0b5d59c8-9f1a-449b-8ed9-fb7be83269f9.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0b61a0b1-0146-4606-a4ca-3c55d39158e7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0bfc0eb2-6212-4007-868a-a4da92035f51.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0d1639d4-7a9b-4316-ae48-70995e1ae2ce.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0d37b7f2-5385-4aaa-9351-209f7a0c1240.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0d448831-e978-476c-89b8-72262951656d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0d762b2b-3937-4c09-814c-8562681ae25e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0ddd0b04-aafa-454a-942c-f8ca57a65c9b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0e0231d0-d95f-474e-ab68-dac306fb896e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0e42d279-d31d-4d23-bb27-adf482ca4152.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0e4319c6-5d9f-4590-9cf8-4dff38bc2394.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0e4a275b-efe5-4132-a6d8-4a86ae6e569f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/0ed0d766-22d5-45e8-a1a3-f68b551f6d56.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/101175de-cdf4-4f69-983e-fb0168d4cadf.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1069660d-1f30-45ad-8c82-89c749b04857.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/10ac3f24-3ad9-422b-8047-96e2fcbf9b03.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/11dc79cc-95ee-4884-a470-8deca9262b48.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/126a822c-bed4-4cc9-80d7-8bb0123d8a6e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/12e57b3d-8eac-4713-8839-ea9a85997a42.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/12f6b12a-1e98-41e8-a876-f09e90032b3b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1348240e-2e86-4c08-a2f7-3de4c33bef5a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1373c599-15da-43fc-af97-5a3ef2b11b54.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/142bde81-0dc0-4ebb-894d-f2718a3daec0.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/154b37ca-92f7-45b0-b301-16e725f541be.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/154ce947-8c6f-48e7-bee0-a0fe26ee1016.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/15528e53-27fb-4acc-a31c-8b0964dd2020.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/15accebb-4786-4470-ae4f-ed9a0dfa42ed.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/15d53517-b951-4ddf-99a0-d28647bb0afa.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1608ce62-3a2b-4338-b630-fa136d1575e5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1661b650-d28b-46a8-8d99-35c80204eacf.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/16b2efaa-b9b3-4d19-8d77-a5ffc6695c42.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/16e72a46-8d70-4cb4-a5e3-73ca35556288.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1728ea83-f1dc-4da4-9cb5-8dff00844005.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/174ff9bd-5867-4ce4-9098-625f4c9b7755.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1756631b-ed09-41b3-9448-bf6a1d5b8210.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/17f478a4-c9df-4814-864a-35641518707e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/184203d4-6457-4107-a154-08e2d3cdae60.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/18d225ed-fd1c-4ee8-8733-74216cfe4764.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1959abf2-ccdf-4c8b-9656-c956723ab713.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/19636cff-fe24-416d-a1ff-bf005e678c00.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/19dc7480-614b-4794-9f06-51145d8510fc.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1a13f0e4-c990-412e-be35-b74efcb92930.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1a1a5a40-cee3-4315-83ae-67c7fa780347.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1ab818e9-7a93-480a-9485-33938574cee1.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1b7d9947-fadb-4939-af9b-bf209ef7658b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1cac74ac-607e-4d8f-acdd-ffdeb5f9e8dd.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1cb89673-b6a8-4798-a09e-d7fdd1555aeb.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1cc5daa8-a4f0-4f45-bf99-697876186304.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1d20a6b6-8c58-425c-82ac-e9a37e64a205.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1ec82d15-0c8e-47a5-a081-d46568de7937.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1ee59590-ba28-486f-accc-5ef14b93a2d9.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1eefe165-b430-4f9c-ae2e-02ae3720a3a6.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1fa24625-8c47-490c-9384-0bb33df7bf2e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/1fb40f13-7f82-4c6f-a1da-70868c7193f9.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/20d3260d-b48c-4503-8cc5-cd541c7f17c4.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2102a193-ca49-4948-8a64-8cee5c3c3772.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2176fcfd-1428-4e58-81f8-456a59b3b08a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/21a5edd2-e612-4ed9-abf4-b18d8e190a1e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/21d46337-e990-472b-933f-938af9433ab2.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/21ed6853-481b-4038-9456-bf221c32a4eb.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2313a924-7c7b-4817-8cdd-ce1ea030a813.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/231cfe4d-1fab-463a-b0fd-86135ae7d8d6.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2344724b-2e56-4b33-a1aa-6624d4bdb385.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/234ed9a7-cd82-4ea5-957b-5193f970e85f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/235b7453-2a1a-4a75-9cc0-bf6b3876c954.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2375c5f9-05eb-4f1d-9161-009a09f8e8c6.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/23940f63-045a-42bd-848f-deb6ac233f4f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/24998afd-4bb0-4cab-acc6-e0677f78726f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/24b19658-4bc9-4eea-824b-576180b9b9b9.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/24f5e4e9-e2a7-4a42-9595-f4364f0af9fd.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/25239c39-026a-4a86-804e-4d9d9c0025da.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/261f589f-2b94-4c88-a333-2833ab2c16c1.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/26429607-434a-4d7a-b9ce-c1b7d0c73fe7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/26c39d15-7c92-4729-870d-4380727805f8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/270a90d4-2147-4de9-8f2d-2d24445feda6.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/27c84283-ec33-45c8-8526-f887f3fce003.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/28e4a2f2-e2f7-4b3f-81d7-3fbb51907873.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/28e74ae1-8592-4518-ae36-68b4206c0317.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2a0130bf-bc44-4c1a-9e97-21d8f95cb88e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2aa05f91-c731-4c08-bdda-44fbbf694301.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2ae115f0-0249-481c-a542-ffef9eb2f8a3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2b5f3b5e-a579-42cb-93e5-4336becff8ce.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2d8fdc20-2c1b-48fd-97ea-3337b1545589.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2daeae57-a119-4387-8d0c-f27ee31de7c9.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2de358c7-dc4e-4b0f-84e5-c3d92177092a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2e1130bf-a1f5-4e59-8dda-3f68695c2edb.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2e4399f0-57a3-4367-a622-6f8cfb8314ed.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2e80040e-c6fe-41a8-916d-554930a34252.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2e8e82d7-9dd6-4ab3-82c7-a94f36ce81fe.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2eb39238-38f1-4ebb-be56-0ea3aad82092.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2f4d6af1-42cd-4cfe-bdcb-5662a4059d58.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2fa3ff06-4708-4693-9ee5-91664a80482f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2fe256a7-8b72-4510-9e65-c76f10302be5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/2ff31fcd-4157-4d49-9d17-a64988dc97ae.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3014b4ba-b41d-4244-a34e-19ab8d95ec95.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/30ae9a62-45d4-4f43-9029-8c69c9d5e4ab.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/31215b25-0a40-4f54-815c-9c227aa4ead8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3132565c-6df0-424f-85b3-7e9d67da8fe8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/313aa098-dfb9-45d7-812b-8979405e149a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/32910f5f-9bb9-4e82-a6e7-f6a73623601c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/333985d1-fd68-4da2-b8d6-9153075633c5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/33a46940-ec95-4b5f-82ec-95ef1831733c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/34662b50-c797-43eb-aed2-bf2c691f400c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/34cabb23-2ef3-4176-a26c-80889154e294.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/35043e94-062f-4e43-9ff6-feeaa157c325.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/357a90de-4203-41e2-b85f-9484fb4f7384.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/35abf3da-2a61-45b5-b081-ea8434351b3c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/36d40d90-c31a-4cb4-9cbe-66a63c9b111e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/37a28b68-edce-44db-a1a7-a2572f5f2df1.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/37e3bf61-81d1-4a54-be78-86b3abd77a12.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/38296d2d-cfff-4baf-a863-03a771ab6877.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/382e76e0-c41c-4491-93db-29ef5dccc74e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/39200fe5-7b75-4e45-b079-d05988c5fab4.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/395a6246-6cbe-49e7-80a2-58c2ce8c4567.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3a2141c7-b30d-459c-977d-085719784151.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3a4073d9-0a28-4827-9c64-0111c44d1e65.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3afe475f-2d7b-4aab-b1ff-5563fbd06093.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3b412347-e3d1-4dbb-9603-9513308ccd7a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3b6222c0-5973-4bea-b228-a5dc01f45827.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3bb30f76-c60b-4190-8132-f7a6d2542d7b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3bc12afe-1476-4c27-9279-8ba1c11f1ecc.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3c6aa2aa-d752-4185-8d58-5fa4b03c9a2e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3de78514-3b37-44e7-b16a-c55d7d043a9a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3de98989-62e6-4f9d-9f29-747eeaf7fce6.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3e1b1eea-35b6-4496-be64-f4f007c40f73.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3e5e406c-55f2-4e47-bd2e-0df595aa23b7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3e76581c-86a9-40a2-b4f8-95669976b828.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3e7b4527-ae41-4ef4-82fb-d2429c0310e7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/3ee4f456-23df-444a-904e-a6a44831dda8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/401f62d5-4338-4b4c-a309-0b2d5b2b31d3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/403d2ba5-6d98-43dc-8c41-885b5a62787c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/404df857-e29d-4f70-8cbc-4325c3e1edba.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/40f87f9f-da0b-4212-a5c3-5febdd5adb21.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/40f9fe45-2aa5-407b-a19a-71f67d028a64.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/41cb0b3c-c2df-48d3-a1c1-87d8d8bfab8e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/41eee6dd-dd45-4317-bbc8-3ec96dbff150.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4264bb69-974b-4f4a-a676-87a9435c9f59.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4271ef9a-4507-4d2d-bde6-42133ef65082.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/427cbcb2-a090-4c79-9eea-57dc78d9fbab.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/42cce528-c21d-483a-a874-b0705fba7c66.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/42dfecdf-25f8-473b-869c-c82c6fbfcb97.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4358357e-d8ae-4916-ba7a-ae77d9dabfa7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/43e87733-fd4f-4af2-9935-8dbd8d709bcd.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4447d56d-a3ab-4487-b9bb-96b6f6907677.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/44c89304-a3fe-43b2-a071-7065b9789dc4.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/44f4e45d-71d9-4bcc-bc87-36390b2ef478.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/451b1688-7ddc-4138-9497-823662e4fa8d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/455f8084-2624-4f80-a791-f1fadd0d38a1.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/460f27c3-edda-4c80-8b0c-e22147893ce0.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/463ff8a0-5f0b-44a1-811c-3c5b0e6639f6.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/46866386-c202-4475-a0f1-3547d962961f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/468bfba5-2fe6-4a7b-a9d1-1adaef0a4775.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/469f2dd8-c89b-4d84-82a9-5e2407143a6d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/471b0aa0-2021-41a6-ac51-dcc01e98d379.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/474baf9b-75ac-4f74-9361-d40884c148e9.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/474fdc71-91cc-4b4b-944a-57178261d8d1.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/47aab1f3-a4cb-4230-9044-1223022eaedb.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/48bc6817-aec8-49c4-8582-6b7eed6a4fd8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/48ceb9a7-9f77-4a89-9c0c-f3b69b2c1179.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4923d0ef-f3fa-4aa7-a552-dc14b7727a45.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4957d5bd-e057-4bf3-afcd-6286f7f3d789.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4986b1e8-80c7-44d8-9f90-f3f1f76cb67a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/49f3d23a-e221-42a3-add2-adf09dd79e5e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4a615d02-39cd-48af-9858-ad16982e8a6a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4a8f5ee4-f4df-4c67-b814-6b2530101948.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4bd4d445-36f4-4e8e-be0d-fee5b6626e45.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4be273fb-5190-4b0f-a3f0-07e89acf8008.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4cb9fc1d-764f-4f96-9361-d9ac078d3e98.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4cce4ff1-ce90-4c8b-a7a2-aaf722ac37ae.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4d4031cd-884a-4427-a24a-f6c390139e64.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4d49a91e-fd1d-4d64-8947-6869f0d1ef77.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4d741d90-17bd-420f-878b-82b5583e4585.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4de70666-2982-4f4d-8fb4-f309aa91c651.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4dee01a7-b34e-4c80-952c-62bedc544bae.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4e9fa4c2-cfcf-4e20-9efe-fcad4649f3e4.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4ea4d743-23b6-4d70-9a49-ddab9557a43f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4eaa523a-75ed-4ad0-9435-eb2f9c2b9068.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/4ee88151-7ca0-4844-8508-c91e4672b3f5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/50211c58-4935-48ee-9add-390cd3301ce1.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/50abe72c-691e-4dec-82ee-4b7f4e0a2743.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5295571b-efb9-4e44-9722-73db41c539a5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5311b371-e931-42f0-9468-92261344208b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5403741f-d165-4b60-a5f8-2fd1f27bbd7c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/55930d97-1be3-4c81-9db8-244a01bf03ad.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/55a8d728-70f9-4feb-817d-8c8f45baf5f3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/55d7b351-1fb8-4845-8fe1-383516a74e15.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/55e3999c-ceab-464b-a106-9cab5c6d909a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/55e6bad5-3220-4465-985f-d0b1b6917c79.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/55f660fc-d641-4c93-9953-eb45ff0598c5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5606b062-bddc-4e1a-8a6a-391dff0dd7f8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/560db27d-af6f-40d4-8e19-dbf0dedb4c9a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/560f6748-be77-4ed3-8bd8-3eee42cbfb7f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/562e92eb-8de9-4e45-b616-cc14c277b8b7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/57090aad-35ab-4393-88b9-ed8c2f40564c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/57237228-59e2-4463-93a5-ed6dc2d19566.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/577ad737-f14b-4d2d-97c3-e3d9b285bcc5.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/59439d00-b9ac-474b-abb0-75b4eb72ed02.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/59a497cd-5bd1-48c6-b117-5653fc21a82b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/59fee583-ddac-4ef8-a017-0f5093310476.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5a1d5bbc-3d44-4519-940f-935fcf21ad65.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5abea4f0-5af0-4a53-b17c-0e6e808bf4bd.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5b9ef0db-c840-4250-bd1e-3d0ae36d334b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5e230b80-91c7-4cee-89eb-02aa0774c0c7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5f848c76-d320-4a19-9439-fbadb58d9a4e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/5fe42c99-79a1-475a-a674-332442112a53.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/601c03ac-2b57-47be-89c7-1a78e2f8cd2e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6123a16f-4d6f-4fdb-af76-070f30f22884.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/61742281-d001-4388-9850-63ae4fe2c00d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/61bf6387-d00b-4c9d-ba5e-c0fa0c7d8505.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/622116f9-dcd2-4583-a974-4a9b54391ab0.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/623197c4-e593-4934-8084-914445c32900.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/62ba8a91-7389-4bc0-aabe-ae3c16a0984b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6324728c-9246-4c6d-81d7-bafc8c2fa2d4.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/634007e3-8d99-455c-81de-e76076721a40.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/63a2177e-df76-4749-b430-faadec4d53d6.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/63f2db9b-34e4-4db9-9ed1-4c0fb0a7a0a7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6459b10e-d6f3-4d56-8f21-2e92b9f8b8bb.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/64d2e43a-f67c-409d-bed8-3a7f0cda1d7e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/65451d7d-8ebb-47aa-9125-eb50621daa6c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/65efaccd-1e5a-4a20-90cf-de85b2321571.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/66b0db17-a269-4c2d-af58-e24935c6953b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/671bb40c-0e43-4571-9cc8-fd74457d1d68.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/69d1408d-6de2-4573-835f-eb4d7cc90c0d.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6a1e54ce-1221-41da-a005-ae4ffb474384.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6a8795e5-8a97-468a-8025-31026f3f6992.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6af374a7-0dc4-44cf-8849-be14a89070a8.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6b00eba2-167f-4355-9c15-0b5f8645d01c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6b3a3905-c97d-4c17-9d5f-56aff4ac48ff.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6c495de5-150e-4f45-8d07-584838311325.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6c535406-01d4-4f8a-885c-f6aae97724d2.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6c706e63-439b-49d3-bad6-cff1c99b7edc.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6c8bc094-5bae-4311-868d-b6426e666b6a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6cd33fbb-3018-4e2a-a951-62b4a787f9ce.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6cde7025-6b23-4712-83b1-b88984e7efbb.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6cebdf49-79f9-4ce6-b70d-1a3bbc53e158.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6d18a537-0f7b-487e-8037-f85a4de3da76.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6e551058-5124-4fff-aff3-b8b3dab7b1ed.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6e8e4302-9fe6-423d-92e9-3d9c543e2922.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/6f8838e2-7923-46fa-a9df-c9c3815e3f4b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/702a73ee-ad8e-4f8e-9f34-133c16ec2016.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/708fca7c-74c6-4660-a09d-5f51b267110f.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/70ac8db4-457a-416f-9c6b-efacae0ac0e3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/70eee26c-4f02-4f54-b92d-fdba1b2338b7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/71cdbce5-43f4-418d-9987-5ac33a2ae083.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/71d33c1f-0ffa-4914-ac53-1a3b9d3fafd6.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/71fea27b-fbfc-415c-aa86-47b621025785.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/72bf2217-9d1d-443a-8e41-20610de00225.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/72d83591-d71b-4c23-a82a-e82d12f23d6c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/73333a67-178d-4f25-bdc3-b7e1fa14b43a.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/73741e38-59e1-42eb-a632-adff7e9e5fb3.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/73a24761-f214-480b-bf9b-1b923c5e0f0e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/73e9612b-1a2a-4dc1-9284-19451284df33.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/7431b9d1-02b8-497e-b3ef-7cae5d1544bc.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/74929b92-d0fe-4b37-8935-86a537226c33.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/749d2073-389c-4b9c-9982-278e993f7322.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/76053919-e76b-49fc-a580-93a7f66422cd.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/769785dc-ad18-4a49-aa14-8e326027d261.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/76fc6364-312f-4583-8c97-b4ddb738dcd7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/77720d9e-54c1-4cfc-bb35-9fbff1c8cee7.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/779bb173-154a-4921-ad63-f42d21493abf.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/78c64bba-3452-4cc6-945a-90d028cc517c.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/793d21da-c55e-47d3-96ab-82d546458415.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/79571c20-21f5-4b9e-8266-d6c45ef86d83.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/79bccae8-ed4d-428e-92a3-78f343732152.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/7ab781d2-f365-4ddd-a9aa-38be84119728.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/7ade46fa-20f9-45d1-bc9f-2d7a520b3e3e.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/7adeb260-c76b-49c7-93f6-5a1d6c0a4d98.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/7b00c5d9-448e-4aee-a4a0-0e627ea798dd.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/7b203a97-345a-4f78-b897-9001c24d025b.root',
'/store/mc/Run3Summer21DR/Single_Pion_gun_E_2to200_14TeV_pythia8/GEN-SIM-RECO/NoPURAWRECO_120X_mcRun3_2021_realistic_v6-v2/270000/7b745144-627d-446f-83a9-fa7ab3ff304a.root',
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
    rootOutputFile = cms.string("SinglePion_2to200_Run3Summer21.root"),# the root tree
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
