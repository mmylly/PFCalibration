from WMCore.Configuration import Configuration

#General settings
config = Configuration()
config.section_("General")
config.General.requestName = 'step2_pi_100k'
config.General.transferOutputs = True

#JobType settings
config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_pi_100k.py'
config.JobType.outputFiles = ['step2_pi_100k.root']
config.JobType.allowUndistributedCMSSW = True

config.JobType.maxMemoryMB = 2500


config.section_("Data")
config.Data.inputDataset = '/SinglePi/mmyllyma-generate_pi_100k-49e13e6fd399c127b5b4930a2aa19018/USER'
config.Data.inputDBS='phys03'
config.Data.splitting = 'FileBased'

config.Data.unitsPerJob = 1
NJOBS = 100  # Has to correspond to the number of files!!!
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/mmyllyma/CRAB3_TransferData'

#config.Data.outputPrimaryDataset = 'SinglePi'
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.outputDatasetTag = config.General.requestName


config.section_("Site")
config.Site.storageSite = 'T2_FI_HIP'
