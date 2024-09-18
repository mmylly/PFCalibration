from WMCore.Configuration import Configuration
#from CRABClient.UserUtilities import getUsernameFromSiteDB
config = Configuration()

config.section_("General")
config.General.requestName = 'step2_pi0_20k'
config.General.workArea = ''
config.General.transferOutputs = True
config.General.transferLogs = True


config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_pi0_20k.py'
config.JobType.outputFiles = ['step2_pi0_20k.root']
config.JobType.allowUndistributedCMSSW = True
#config.JobType.eventsPerLumi = 2000

config.JobType.maxMemoryMB = 2500  # Max amount of memory a job is allowed to use
#config.JobType.numCores = 2  # Note that increasing this will most probably force you to increase memroy as well!

config.section_("Data")
#config.Data.inputDataset = '/SinglePi/akormu-TestSinglePi_10-cd18d6428c3fb7c717758244f5fd08c3/USER'
#config.Data.inputDataset = '/afs/cern.ch/work/m/mmyllyma/singleParticleResponse/CMSSW_10_4_0/src/PFCalibration/PFChargedHadronAnalyzer/mmylly/step1_pi0_20k.root'
#config.Data.inputDBS='phys03'
#config.Data.inputDBS='global'
#config.Data.splitting = 'EventBased'

config.Data.primaryDataset = 'step1_pi0_20k'
config.Data.userInputFiles = open('step1_pi0_20k_list.txt').readlines()
#config.Data.userInputFiles = [step1_pi0_20k_1.root, step1_pi0_20k_2.root, step1_pi0_20k_3.root, step1_pi0_20k_4.root, step1_pi0_20k_5.root, step1_pi0_20k_6.root, step1_pi0_20k_7.root, step1_pi0_20k_8.root, step1_pi0_20k_9.root, step1_pi0_20k_10.root]
config.Data.ignoreLocality = True
config.Data.splitting = 'FileBased'

config.Data.unitsPerJob = 1
NJOBS = 10  # Has to correspond to the number of files!!!
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.outLFNDirBase = '/store/user/%s/CRAB3_TransferData' % (getUsernameFromSiteDB())

config.Data.outputPrimaryDataset = 'SinglePi'
config.Data.publication = True
config.Data.publishDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/' # Parameter Data.publishDbsUrl has been renamed to Data.publishDBS
config.Data.outputDatasetTag = 'SinlePi_step2_10' # <== Check!!!


config.section_("Site")
config.Site.storageSite = 'T2_FI_HIP'
config.Site.whitelist = ['T2_FI_HIP']

