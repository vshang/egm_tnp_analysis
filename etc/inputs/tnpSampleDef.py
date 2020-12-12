from libPython.tnpClassUtils import tnpSample

hdfs2018Samples = '/hdfs/store/user/vshang/2020-12-07/2018/'

samples2018 = {
    'DY_NLO'               : tnpSample('DY_NLO', hdfs2018Samples + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/TnPTree_all.root', isMC = True, nEvts = -1 ), 
    'data_Run2018A'        : tnpSample('data_Run2018A', hdfs2018Samples + 'data/EGamma/crab_2018_Run2018A/TnPTree_all.root', lumi = 14.00 ), 
    'data_Run2018B'        : tnpSample('data_Run2018B', hdfs2018Samples + 'data/EGamma/crab_2018_Run2018B/TnPTree_all.root', lumi = 7.10 ), 
    'data_Run2018C'        : tnpSample('data_Run2018C', hdfs2018Samples + 'data/EGamma/crab_2018_Run2018C/TnPTree_all.root', lumi = 6.94 ), 
    'data_Run2018D'        : tnpSample('data_Run2018D', hdfs2018Samples + 'data/EGamma/crab_2018_Run2018D/TnPTree_all.root', lumi = 31.93 ), 
    }

