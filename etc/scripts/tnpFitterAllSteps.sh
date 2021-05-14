#!/bin/bash

script=$1
flags=(
    #"passEleTriggers2016" 
    "passEleTriggers2017" 
    #"passEleTriggers2018"
    
)

for flag in ${flags[@]}; do
    echo $flag
    python tnpEGM_fitter.py  $script --flag $flag --createBins
    python tnpEGM_fitter.py  $script --flag $flag --createHists
    python tnpEGM_fitter.py  $script --flag $flag --doFit
    python tnpEGM_fitter.py  $script --flag $flag --doFit --mcSig --altSig
    python tnpEGM_fitter.py  $script --flag $flag --doFit --altSig
    python tnpEGM_fitter.py  $script --flag $flag --doFit --altBkg
    python tnpEGM_fitter.py  $script --flag $flag --sumUp
done


