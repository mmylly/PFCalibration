# Import needed modules
from WMCore.Configuration import Configuration

#particleID=111
#energy=2

# General settings
config = Configuration()
config.section_("General")
config.General.requestName = 'generate_pi0_20k'
config.General.workArea = ''
config.General.transferOutputs = True
config.General.transferLogs = True

# JobType settings
config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'generate_pi0_20k.py'
#config.JobType.pyCfgParams = ['particleID','energy'] # Parameters to pass to the particle gun
config.JobType.outputFiles = ['step1_pi0_20k.root']
config.JobType.eventsPerLumi = 500
config.JobType.allowUndistributedCMSSW = True

# Data settings
config.section_("Data")
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1
NJOBS = 10
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = False
config.Data.outLFNDirBase = '/store/user/mmyllyma/CRAB3_TransferData'
config.Data.outputPrimaryDataset = 'generate_pi0_20k'
#config.Data.publication = True
#config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.outputDatasetTag = config.General.requestName # <== Check!!!

config.section_("Site")
config.Site.storageSite = 'T2_FI_HIP'

