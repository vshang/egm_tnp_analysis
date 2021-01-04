from libPython.tnpClassUtils import tnpSample

hdfs2016Samples = '/hdfs/store/user/vshang/TnP_EleTriggers_2020-12-23/2016/'
hdfs2017Samples = '/hdfs/store/user/vshang/TnP_EleTriggers_2020-12-23/2017/'
hdfs2018Samples = '/hdfs/store/user/vshang/TnP_EleTriggers_2020-12-23/2018/'

samples2016 = {
    'DY_LO'               : tnpSample('DY_LO', hdfs2016Samples + 'mc/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/TnPTree_all.root', isMC = True, nEvts = -1 ), 
    'DY_NLO'               : tnpSample('DY_NLO', hdfs2016Samples + 'mc/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/TnPTree_all.root', isMC = True, nEvts = -1 ), 
    'data_Run2016B'        : tnpSample('data_Run2016B', hdfs2016Samples + 'data/SingleElectron/crab_2016_Run2016B/TnPTree_all.root', lumi = 5.75 ), 
    'data_Run2016C'        : tnpSample('data_Run2016C', hdfs2016Samples + 'data/SingleElectron/crab_2016_Run2016C/TnPTree_all.root', lumi = 2.57 ), 
    'data_Run2016D'        : tnpSample('data_Run2016D', hdfs2016Samples + 'data/SingleElectron/crab_2016_Run2016D/TnPTree_all.root', lumi = 4.24 ), 
    'data_Run2016E'        : tnpSample('data_Run2016E', hdfs2016Samples + 'data/SingleElectron/crab_2016_Run2016E/TnPTree_all.root', lumi = 4.03 ), 
    'data_Run2016F'        : tnpSample('data_Run2016F', hdfs2016Samples + 'data/SingleElectron/crab_2016_Run2016F/TnPTree_all.root', lumi = 3.10 ), 
    'data_Run2016G'        : tnpSample('data_Run2016G', hdfs2016Samples + 'data/SingleElectron/crab_2016_Run2016G/TnPTree_all.root', lumi = 7.58 ), 
    'data_Run2016H'        : tnpSample('data_Run2016H', hdfs2016Samples + 'data/SingleElectron/crab_2016_Run2016H/TnPTree_all.root', lumi = 8.65 ), 
    }

samples2017 = {
    'DY_LO'               : tnpSample('DY_LO', hdfs2017Samples + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/TnPTree_all.root', isMC = True, nEvts = -1 ), 
    'DY_NLO'               : tnpSample('DY_NLO', hdfs2017Samples + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/TnPTree_all.root', isMC = True, nEvts = -1 ), 
    'data_Run2017B'        : tnpSample('data_Run2017B', hdfs2017Samples + 'data/SingleElectron/crab_2017_Run2017B/TnPTree_all.root', lumi = 4.79 ), 
    'data_Run2017C'        : tnpSample('data_Run2017C', hdfs2017Samples + 'data/SingleElectron/crab_2017_Run2017C/TnPTree_all.root', lumi = 9.63 ), 
    'data_Run2017D'        : tnpSample('data_Run2017D', hdfs2017Samples + 'data/SingleElectron/crab_2017_Run2017D/TnPTree_all.root', lumi = 4.25 ), 
    'data_Run2017E'        : tnpSample('data_Run2017E', hdfs2017Samples + 'data/SingleElectron/crab_2017_Run2017E/TnPTree_all.root', lumi = 9.31 ), 
    'data_Run2017F'        : tnpSample('data_Run2017F', hdfs2017Samples + 'data/SingleElectron/crab_2017_Run2017F/TnPTree_all.root', lumi = 13.54 ), 
    }

samples2018 = {
    'DY_LO'               : tnpSample('DY_LO', hdfs2018Samples + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/TnPTree_all.root', isMC = True, nEvts = -1 ), 
    'DY_NLO'               : tnpSample('DY_NLO', hdfs2018Samples + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/TnPTree_all.root', isMC = True, nEvts = -1 ), 
    'data_Run2018A'        : tnpSample('data_Run2018A', hdfs2018Samples + 'data/EGamma/crab_2018_Run2018A/TnPTree_all.root', lumi = 14.03 ), 
    'data_Run2018B'        : tnpSample('data_Run2018B', hdfs2018Samples + 'data/EGamma/crab_2018_Run2018B/TnPTree_all.root', lumi = 7.07 ), 
    'data_Run2018C'        : tnpSample('data_Run2018C', hdfs2018Samples + 'data/EGamma/crab_2018_Run2018C/TnPTree_all.root', lumi = 6.90 ), 
    'data_Run2018D'        : tnpSample('data_Run2018D', hdfs2018Samples + 'data/EGamma/crab_2018_Run2018D/TnPTree_all.root', lumi = 31.84 ), 
    }

