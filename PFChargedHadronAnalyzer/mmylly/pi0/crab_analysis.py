from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import getUsernameFromSiteDB



config = Configuration()
config.section_("General")
config.General.requestName = 'myAnalysis'
config.General.workArea = 'test_ana'



config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'myAnalysis.py'
config.JobType.outputFiles = ['step99_trees.root']
config.JobType.maxMemoryMB = 2500



config.section_("Data")
config.Data.inputDataset = '/SinglePi/akormu-PGun_step3_10_RECOSIMoutput-a72183928a18347e3ce9f021a71eec87/USER'
config.Data.inputDBS='phys03'

#config.Data.userInputFiles = open('file:step3_file_list.txt').readlines()
#config.Data.ignoreLocality = True

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10
NJOBS = 10
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outLFNDirBase = '/store/user/%s/CRAB3_TransferData' % (getUsernameFromSiteDB())
config.Data.outputPrimaryDataset = 'SinglePi'
config.Data.publication = False
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/' # Parameter Data.publishDbsUrl has been renamed to Data.publishDBS
config.Data.outputDatasetTag = TestAna # <== Check!!!



config.section_("Site")
config.Site.storageSite = 'T2_FI_HIP'
#config.Site.whitelist = ['T2_FI_HIP']

