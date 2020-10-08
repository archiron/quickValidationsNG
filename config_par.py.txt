#! /usr/bin/env python
#-*-coding: utf-8 -*-

import os,sys

#############################################################################
# global data
web_repo = ['/eos/project/c/cmsweb/www/egamma/validation/Electrons/Dev/', 'dev/']
#web_repo = ['/eos/project/c/cmsweb/www/egamma/validation/Electrons/Releases/', 'std'/]

# personalization 1
GeV_1 = [
['CMSSW_11_1_0_pre4', 'CMSSW_11_1_0_pre3'] ,
['quick_2021', ''] ,
['TTbar_14TeV', 'ZEE_14'] , 
'FullvsFull' , 
['RECO', 'RECO'] ,
['', ''] ,  # GT one couple rel/ref for each dataset
['DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_11_1_0_pre4-110X_mcRun3_2021_realistic_v8-v1__DQMIO.root',
 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_11_1_0_pre3-110X_mcRun3_2021_realistic_v8-v1__DQMIO.root',
 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_11_1_0_pre4-110X_mcRun3_2021_realistic_v8-v1__DQMIO.root',
 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_11_1_0_pre3-110X_mcRun3_2021_realistic_v8-v1__DQMIO.root',], # relref files one couple rel/ref for each dataset
[False, True], # DB flag
]

# personalization 2
GeV_2 = [
['CMSSW_11_1_0_pre4', 'CMSSW_11_1_0_pre3'] , # release/reference
['quick_PHASE2', ''] , # relref_extent
['ZEE_14'] , #datasets
'FullvsFull' , # choice
['RECO', 'RECO'] , # relrefValtype RECO vs RECO
['CMSSW_11_1_0_pre4-110X_mcRun4_realistic_v3_2026D49noPU-v1', 'CMSSW_11_1_0_pre3-110X_mcRun4_realistic_v3-v1',] , # GT one couple rel/ref for each dataset
['', ''], # relref files one couple rel/ref for each dataset
[False], # DB flag
]

#############################################################################


