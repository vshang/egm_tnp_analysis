#############################################################
########## General settings
#############################################################
# flag to be Tested
flags = {
    'passEleTriggers2017' : '( ( (passHltEl327WPTightGsfL1DoubleEG == 1) && (passHltEGL1SingleEG == 1) ) ||  (passHltPhoton200 == 1) || (passHltEle115CaloIdVTGsfTrkIdT == 1) )'
    #'passEleTriggers2017' : '( (passHltEl327WPTightGsfL1DoubleEG == 1) && (passHltEGL1SingleEG == 1) )'
    }
baseOutDir = 'results/eleTriggersv3/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpEleTrig'

samplesDef = {
    'data'   : tnpSamples.samples2017['data_Run2017B'].clone(),
    'mcNom'  : tnpSamples.samples2017['DY1_LO'].clone(),
    'mcAlt'  : tnpSamples.samples2017['DY_NLO'].clone(),
    'tagSel' : None, #tnpSamples.samples2017['DY_NLO'].clone(),
}
## can add data sample easily
# samplesDef['mcNom'].add_sample( tnpSamples.samples2017['DY_LO_HT200to400'] )
# samplesDef['mcNom'].add_sample( tnpSamples.samples2017['DY_LO_HT400to600'] )
# samplesDef['mcNom'].add_sample( tnpSamples.samples2017['DY_LO_HT600to800'] )
# samplesDef['mcNom'].add_sample( tnpSamples.samples2017['DY_LO_HT800to1200'] )
# samplesDef['mcNom'].add_sample( tnpSamples.samples2017['DY_LO_HT1200to2500'] )
# samplesDef['mcNom'].add_sample( tnpSamples.samples2017['DY_LO_HT2500toInf'] )
samplesDef['mcNom'].add_sample( tnpSamples.samples2017['DY2_LO'] )
samplesDef['mcNom'].add_sample( tnpSamples.samples2017['DY3_LO'] )
samplesDef['mcNom'].add_sample( tnpSamples.samples2017['DY4_LO'] )
samplesDef['data'].add_sample( tnpSamples.samples2017['data_Run2017C'] )
samplesDef['data'].add_sample( tnpSamples.samples2017['data_Run2017D'] )
samplesDef['data'].add_sample( tnpSamples.samples2017['data_Run2017E'] )
samplesDef['data'].add_sample( tnpSamples.samples2017['data_Run2017F'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()

## set MC weight, simple way (use tree weight) 
weightName = 'totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [35,50,70,100,150,200,500] },
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.1 && el_q*tag_Ele_q < 0'

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
# additionalCuts = { 
#     0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#     1 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#     2 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#     3 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#     4 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#     5 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#     6 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#     7 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#     8 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#     9 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
# }

#### or remove any additional cut (default)
additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.5,0.1,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, 0, 1]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, 0, 1]","peakF[90.0]",
    ]

tnpParAltSigFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.5,0.1,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",
    ]
        
