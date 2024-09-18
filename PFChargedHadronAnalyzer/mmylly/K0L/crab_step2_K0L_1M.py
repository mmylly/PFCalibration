from WMCore.Configuration import Configuration

#General settings
config = Configuration()
config.section_("General")
config.General.requestName = 'step2_K0L_1M'
config.General.transferOutputs = True

#JobType settings
config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_K0L_1M.py'
config.JobType.outputFiles = ['step2_K0L_1M.root']
config.JobType.allowUndistributedCMSSW = True

config.JobType.maxMemoryMB = 2500


config.section_("Data")
config.Data.inputDataset = '/SingleK0L/mmyllyma-generate_K0L_1M-bc7f99e6da8174c019580527ac7fb82b/USER'
config.Data.inputDBS='phys03'
#config.Data.splitting = 'Automatic'


config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
NJOBS = 100  # Has to correspond to the number of files!!!
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outLFNDirBase = '/store/user/mmyllyma/CRAB3_TransferData'

config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.outputDatasetTag = config.General.requestName


config.section_("Site")
config.Site.storageSite = 'T2_FI_HIP'
config.Site.whitelist = ['T2_FI*', 'T2_CH*', 'T2_US*']
