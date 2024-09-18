from WMCore.Configuration import Configuration

#General settings
config = Configuration()
config.section_("General")
config.General.requestName = 'step3_K0S_20k'
config.General.transferOutputs = True

#JobType settings
config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_K0S_20k.py'
config.JobType.outputFiles = ['step3_K0S_20k.root']
config.JobType.allowUndistributedCMSSW = True

config.JobType.maxMemoryMB = 2500


config.section_("Data")
config.Data.inputDataset = '/SingleK0S/mmyllyma-step2_K0S_20k-429973859737a67eb10c1a53af2256fc/USER'
config.Data.inputDBS='phys03'
config.Data.splitting = 'FileBased'

config.Data.unitsPerJob = 1
NJOBS = 20  # Has to correspond to the number of files!!!
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/mmyllyma/CRAB3_TransferData'

config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.outputDatasetTag = config.General.requestName


config.section_("Site")
config.Site.storageSite = 'T2_FI_HIP'
