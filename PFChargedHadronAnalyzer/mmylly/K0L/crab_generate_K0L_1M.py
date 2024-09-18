# Import needed modules
from WMCore.Configuration import Configuration

# General settings
config = Configuration()
config.section_("General")
config.General.requestName = 'generate_K0L_1M'
config.General.transferOutputs = True

# JobType settings
config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'generate_K0L_1M.py'
config.JobType.outputFiles = ['step1_K0L_1M.root']
config.JobType.eventsPerLumi = 500
config.JobType.allowUndistributedCMSSW = True

# Data settings
config.section_("Data")
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
config.Data.totalUnits = 1000000
config.Data.outLFNDirBase = '/store/user/mmyllyma/CRAB3_TransferData'

config.Data.outputPrimaryDataset = 'SingleK0L'
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.outputDatasetTag = config.General.requestName



config.section_("Site")
config.Site.storageSite = 'T2_FI_HIP'
