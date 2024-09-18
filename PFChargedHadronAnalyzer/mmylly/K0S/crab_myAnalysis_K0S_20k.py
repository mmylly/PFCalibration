from WMCore.Configuration import Configuration

#General settings
config = Configuration()
config.section_("General")
config.General.requestName = 'myAnalysis_K0S_20k'
config.General.transferOutputs = True

#JobType settings
config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'myAnalysis_K0S_20k.py'
config.JobType.outputFiles = ['step99_K0S_20k_trees.root']
config.JobType.allowUndistributedCMSSW = True

config.JobType.maxMemoryMB = 2500


config.section_("Data")
config.Data.inputDataset = '/SingleK0S/mmyllyma-step3_K0S_20k-d50b77769ed38983f48189deb3e4f4d3/USER'
config.Data.inputDBS='phys03'
config.Data.splitting = 'FileBased'

config.Data.unitsPerJob = 1
NJOBS = 20  # Has to correspond to the number of files!!!
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/mmyllyma/CRAB3_TransferData'

#config.Data.publication = True
#config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
#config.Data.outputDatasetTag = config.General.requestName


config.section_("Site")
config.Site.storageSite = 'T2_FI_HIP'
