#! /usr/bin/env python
#-*-coding: utf-8 -*-

################################################################################
# filesSources.py : list of ROOT files to be used with zeeExtract tools
# for egamma validation comparison                              
# 
# MUST be launched with the cmsenv cmd after a cmsrel cmd !!
#                                                                              
# Arnaud Chiron-Turlay LLR - arnaud.chiron@llr.in2p3.fr                        
#                                                                              
################################################################################

# definition '-' : not selected
#            '+' : selected
#            '*' : selected AND reference

# get the "sources" root file datas
rootList = [
    'rootSourcesRelValSingleEFlatPt2To100mcRun4RECO',
    'rootSourcesRelValSingleEFlatPt2To100mcRun4PU',
    'rootSourcesRelValTTbar_14TeVmcRun4RECO',
    'rootSourcesRelValTTbar_14TeVmcRun3RECO',
    'rootSourcesRelValTTbar_14TeVmcRun4PU',
    'rootSourcesRelValTTbar_14TeVmcRun3PU',
    'rootSourcesRelValZEE_14mcRun4RECO',
    'rootSourcesRelValZEE_14mcRun3RECO',
    'rootSourcesRelValZEE_14mcRun4PU',
    'rootSourcesRelValZEE_14mcRun3PU',
    'rootSourcesRelValZpToEE_m6000_14TeVmcRun3RECO',
    'rootSourcesRelValZpToEE_m6000_14TeVmcRun3PU',
    'rootSourcesRelValTTbar_14TeVmcRun3PURecoOnly',
    'rootSourcesRelValTTbar_14TeVmcRun4PURecoOnly',
    'rootSourcesRelValZpToEE_m6000_14TeVmcRun3PURecoOnly',
    'rootSourcesRelValZEE_14mcRun3PURecoOnly',
    'rootSourcesRelValZEE_14mcRun4PURecoOnly',
]

# RelValSingleEFlatPt2To100-mcRun4-RECO-noPU
rootSourcesRelValSingleEFlatPt2To100mcRun4RECO = [
    ['*', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_14_1_0_pre7-141X_mcRun4_realistic_v1_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_14_2_0_pre1-141X_mcRun4_realistic_v1_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_14_2_0_pre2-141X_mcRun4_realistic_v1_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_14_2_0_pre3-141X_mcRun4_realistic_v3_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_14_2_0_pre4-141X_mcRun4_realistic_v3_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_15_0_0_pre1-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_15_0_0_pre2-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_15_0_0_pre3-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_15_0_0_pre2-141X_mcRun4_realistic_v3_STD_RegeneratedGS_Run4D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_15_1_0_pre2-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_15_1_0_pre3-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v1__DQMIO.root'],
]

# RelValSingleEFlatPt2To100-mcRun4-PU
rootSourcesRelValSingleEFlatPt2To100mcRun4PU = [
    ['*', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_14_1_0_pre7-141X_mcRun4_realistic_v1_STD_2026D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_14_2_0_pre1-PU_141X_mcRun4_realistic_v1_STD_2026D110_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_14_2_0_pre2-PU_141X_mcRun4_realistic_v1_STD_2026D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_14_2_0_pre3-PU_141X_mcRun4_realistic_v3_STD_2026D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_14_2_0_pre4-PU_141X_mcRun4_realistic_v3_STD_2026D110_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_15_0_0_pre1-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_15_0_0_pre2-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_15_0_0_pre3-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_15_0_0_pre3-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v2__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_15_1_0_pre1-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_15_1_0_pre2-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValSingleEFlatPt2To100__CMSSW_15_1_0_pre3-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1__DQMIO.root'],
]

# RelValTTbar_14TeV-mcRun4-noPU
rootSourcesRelValTTbar_14TeVmcRun4RECO = [
    ['*', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0_pre7-141X_mcRun4_realistic_v1_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre1-141X_mcRun4_realistic_v1_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre2-141X_mcRun4_realistic_v1_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre3-141X_mcRun4_realistic_v3_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre4-141X_mcRun4_realistic_v3_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre1-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre2-141X_mcRun4_realistic_v3_STD_RegeneratedGS_Run4D110_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre3-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre3-141X_mcRun4_realistic_v3_STD_RegeneratedGS_Run4D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre1-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre2-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre3-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v1__DQMIO.root'],
]

# RelValTTbar_14TeV-mcRun3-noPU
rootSourcesRelValTTbar_14TeVmcRun3RECO = [
    ['*', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0-140X_mcRun3_2024_realistic_v21_STD_RegeneratedGS_2024_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre1-140X_mcRun3_2024_realistic_v21_STD_RegeneratedGS_2024_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre2-140X_mcRun3_2024_realistic_v25_STD_RegeneratedGS_2024_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre3-140X_mcRun3_2024_realistic_v26_STD_RegeneratedGS_2024_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre4-140X_mcRun3_2024_realistic_v26_STD_RecylcedGS_2024_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre1-142X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre2-142X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre2-142X_mcRun3_2025_realistic_v2_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre3-142X_mcRun3_2025_realistic_v5_STD_RegeneratedGS_2025_noPU-v2__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre3-142X_mcRun3_2025_realistic_v5_STD_RecycledGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0-142X_mcRun3_2025_realistic_v7_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre1-142X_mcRun3_2025_realistic_v7_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre2-150X_mcRun3_2025_realistic_v1_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre3-150X_mcRun3_2025_realistic_v2_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
]

# RelValTTbar_14TeV-mcRun4-PU
rootSourcesRelValTTbar_14TeVmcRun4PU = [
    ['*', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0_pre7-141X_mcRun4_realistic_v1_STD_2026D110_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre1-PU_141X_mcRun4_realistic_v1_STD_2026D110_PU-v2__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre2-PU_141X_mcRun4_realistic_v1_STD_2026D110_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre3-PU_141X_mcRun4_realistic_v3_STD_2026D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre4-PU_141X_mcRun4_realistic_v3_STD_2026D110_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre1-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre2-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre3-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre3-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre1-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre2-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre3-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1__DQMIO.root'],
]

# RelValTTbar_14TeV-mcRun3-PU
rootSourcesRelValTTbar_14TeVmcRun3PU = [
    ['*', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0-PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre1-PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre2-PU_140X_mcRun3_2024_realistic_v25_STD_2024_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre3-PU_140X_mcRun3_2024_realistic_v26_STD_2024_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre4-PU_142X_mcRun3_2025_realistic_v1_STD_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre1-PU_140X_mcRun3_2024_realistic_v26_STD_2024_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre2-PU_142X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre3-PU_142X_mcRun3_2025_realistic_v5_STD_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre3-PU_142X_mcRun3_2025_realistic_v5_STD_2025_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0-PU_142X_mcRun3_2025_realistic_v7_STD_2025_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre1-PU_142X_mcRun3_2025_realistic_v7_STD_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre2-PU_150X_mcRun3_2025_realistic_v1_STD_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre3-PU_150X_mcRun3_2025_realistic_v2_STD_2025_PU-v2__DQMIO.root'],
]

# RelValZEE_14-mcRun3-noPU
rootSourcesRelValZEE_14mcRun3RECO = [
    ['*', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_1_0-140X_mcRun3_2024_realistic_v21_STD_RegeneratedGS_2024_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre1-140X_mcRun3_2024_realistic_v21_STD_RegeneratedGS_2024_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre2-140X_mcRun3_2024_realistic_v25_STD_RegeneratedGS_2024_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre3-140X_mcRun3_2024_realistic_v26_STD_RegeneratedGS_2024_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre4-140X_mcRun3_2024_realistic_v26_STD_RecylcedGS_2024_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre1-142X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre2-142X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre2-142X_mcRun3_2025_realistic_v2_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre3-142X_mcRun3_2025_realistic_v5_STD_RecycledGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre3-142X_mcRun3_2025_realistic_v5_STD_RegeneratedGS_2025_noPU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0-142X_mcRun3_2025_realistic_v7_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre1-142X_mcRun3_2025_realistic_v7_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre2-150X_mcRun3_2025_realistic_v1_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre3-150X_mcRun3_2025_realistic_v2_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
]

# RelValZEE_14-mcRun3-PU
rootSourcesRelValZEE_14mcRun3PU = [
    ['*', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_1_0-PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre1-PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre2-PU_140X_mcRun3_2024_realistic_v25_STD_2024_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre3-PU_140X_mcRun3_2024_realistic_v26_STD_2024_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre4-PU_142X_mcRun3_2025_realistic_v1_STD_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre1-PU_140X_mcRun3_2024_realistic_v26_STD_2024_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre2-PU_142X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre3-PU_142X_mcRun3_2025_realistic_v5_STD_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre3-PU_142X_mcRun3_2025_realistic_v5_STD_2025_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0-PU_142X_mcRun3_2025_realistic_v7_STD_2025_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre1-PU_142X_mcRun3_2025_realistic_v7_STD_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre2-PU_150X_mcRun3_2025_realistic_v1_STD_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre3-PU_150X_mcRun3_2025_realistic_v2_STD_2025_PU-v2__DQMIO.root'],
]

# RelValZEE_14-mcRun4-noPU
rootSourcesRelValZEE_14mcRun4RECO = [
    ['*', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_1_0_pre7-141X_mcRun4_realistic_v1_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre1-141X_mcRun4_realistic_v1_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre2-141X_mcRun4_realistic_v1_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre3-141X_mcRun4_realistic_v3_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre4-141X_mcRun4_realistic_v3_STD_RegeneratedGS_2026D110_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre1-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre2-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre2-141X_mcRun4_realistic_v3_STD_RegeneratedGS_Run4D110_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre3-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre3-141X_mcRun4_realistic_v3_STD_RegeneratedGS_Run4D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre1-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre2-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre3-141X_mcRun4_realistic_v3_STD_RecycledGS_Run4D110_noPU-v1__DQMIO.root'],
]

# RelValZEE_14-mcRun4-PU
rootSourcesRelValZEE_14mcRun4PU = [
    ['*', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_1_0_pre7-141X_mcRun4_realistic_v1_STD_2026D110_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre1-PU_141X_mcRun4_realistic_v1_STD_2026D110_PU-v2__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre2-PU_141X_mcRun4_realistic_v1_STD_2026D110_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre3-PU_141X_mcRun4_realistic_v3_STD_2026D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre4-PU_141X_mcRun4_realistic_v3_STD_2026D110_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre1-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre2-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre3-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre3-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre1-PU_141X_mcRun4_realistic_v3_STD_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre2-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre3-PU_150X_mcRun4_realistic_v1_STD_Run4D110_PU-v1__DQMIO.root'],
]

# RelValZpToEE_m6000_14TeV-mcRun3-noPU
rootSourcesRelValZpToEE_m6000_14TeVmcRun3RECO = [
    ['*', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_1_0-140X_mcRun3_2024_realistic_v21_STD_RegeneratedGS_2024_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_2_0_pre1-140X_mcRun3_2024_realistic_v21_STD_RegeneratedGS_2024_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_2_0_pre2-140X_mcRun3_2024_realistic_v25_STD_RegeneratedGS_2024_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_2_0_pre3-140X_mcRun3_2024_realistic_v26_STD_RegeneratedGS_2024_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_2_0_pre4-140X_mcRun3_2024_realistic_v26_STD_RecylcedGS_2024_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_0_0_pre1-142X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_0_0_pre2-142X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_0_0_pre2-142X_mcRun3_2025_realistic_v2_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_0_0_pre3-142X_mcRun3_2025_realistic_v5_STD_RegeneratedGS_2025_noPU-v2__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_0_0_pre3-142X_mcRun3_2025_realistic_v5_STD_RecycledGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_0_0-142X_mcRun3_2025_realistic_v7_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_1_0_pre1-142X_mcRun3_2025_realistic_v7_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_1_0_pre2-150X_mcRun3_2025_realistic_v1_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_1_0_pre3-150X_mcRun3_2025_realistic_v2_STD_RegeneratedGS_2025_noPU-v1__DQMIO.root'],
]

# RelValZpToEE_m6000_14TeV-mcRun3-PU
rootSourcesRelValZpToEE_m6000_14TeVmcRun3PU = [
    ['*', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_1_0-PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_2_0_pre1-PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_2_0_pre2-PU_140X_mcRun3_2024_realistic_v25_STD_2024_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_2_0_pre3-PU_140X_mcRun3_2024_realistic_v26_STD_2024_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_2_0_pre4-PU_142X_mcRun3_2025_realistic_v1_STD_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_0_0_pre1-PU_140X_mcRun3_2024_realistic_v26_STD_2024_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_0_0_pre2-PU_142X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_0_0_pre3-PU_142X_mcRun3_2025_realistic_v5_STD_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_0_0_pre3-PU_142X_mcRun3_2025_realistic_v5_STD_2025_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_0_0-PU_142X_mcRun3_2025_realistic_v7_STD_2025_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_1_0_pre1-PU_142X_mcRun3_2025_realistic_v7_STD_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_1_0_pre2-PU_150X_mcRun3_2025_realistic_v1_STD_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_1_0_pre3-PU_150X_mcRun3_2025_realistic_v2_STD_2025_PU-v2__DQMIO.root'],
]

# RelValTTbar_14TeV-mcRun3-PU-RecoOnly
rootSourcesRelValTTbar_14TeVmcRun3PURecoOnly = [
    ['*', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0-140X_mcRun3_2024_realistic_v21_STD_RecoOnly_2024_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0_pre1-140X_mcRun3_2024_realistic_v1_STD_2024_PU_RecoOnly-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0_pre3-140X_mcRun3_2024_realistic_v7_STD_2024_PU_RecoOnly-v2__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0_pre4-140X_mcRun3_2024_realistic_v8_STD_2024_PU_RecoOnly-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0_pre5-140X_mcRun3_2024_realistic_v11_STD_2024_PU_RecoOnly-v1__DQMIO.root'],
    ['+', 'DQM_V0002_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0_pre6-140X_mcRun3_2024_realistic_v15_STD_2024_PU_RecoOnly-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0_pre7-140X_mcRun3_2024_realistic_v15_STD_RecoOnly_2024_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre1-PU_140X_mcRun3_2024_realistic_v21_STD_RecoOnly_2024_PU-v2__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre2-140X_mcRun3_2024_realistic_v21_STD_RecoOnly_2024_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre3-PU_140X_mcRun3_2024_realistic_v25_STD_RecoOnly_2024_PU-v2__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre4-140X_mcRun3_2024_realistic_v26_STD_RecoOnly_2024_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre1-PU_142X_mcRun3_2025_realistic_v1_STD_RecoOnly_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre2-PU_142X_mcRun3_2025_realistic_v4_STD_RecoOnly_2025_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre3-PU_142X_mcRun3_2025_realistic_v4_STD_RecoOnly_2025_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0-PU_142X_mcRun3_2025_realistic_v5_STD_RecoOnly_2025_PU-v3__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre1-PU_142X_mcRun3_2025_realistic_v5_STD_RecoOnly_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre2-142X_mcRun3_2025_realistic_v7_STD_RecoOnly_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre3-150X_mcRun3_2025_realistic_v1_STD_RecoOnly_2025_PU-v1__DQMIO.root'],
]

# RelValTTbar_14TeV-mcRun4-PU-RecoOnly
rootSourcesRelValTTbar_14TeVmcRun4PURecoOnly = [
    ['*', 'DQM_V0002_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0_pre7-141X_mcRun4_realistic_v1_STD_RecoOnly_2026D110_PU-v4__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre1-141X_mcRun4_realistic_v1_STD_RecoOnly_2026D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre3-PU_141X_mcRun4_realistic_v3_STD_RecoOnly_2026D110_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_2_0_pre4-PU_141X_mcRun4_realistic_v3_STD_RecoOnly_2026D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre1-PU_141X_mcRun4_realistic_v3_STD_RecoOnly_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre2-141X_mcRun4_realistic_v3_STD_RecoOnly_Run4D110_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_0_0_pre3-PU_141X_mcRun4_realistic_v3_STD_RecoOnly_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre1-PU_141X_mcRun4_realistic_v3_STD_RecoOnly_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre2-PU_150X_mcRun4_realistic_v1_STD_RecoOnly_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_15_1_0_pre3-PU_150X_mcRun4_realistic_v1_STD_RecoOnly_Run4D110_PU-v2__DQMIO.root'],
]

# RelValZpToEE_m6000_14TeV-mcRun3-PU-RecoOnly
rootSourcesRelValZpToEE_m6000_14TeVmcRun3PURecoOnly = [
    ['*', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_0_0-140X_mcRun3_2024_realistic_v3_RecoOnly_2024_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_0_0_pre3-140X_mcRun3_2024_realistic_v1_RecoOnly_2024_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_1_0_pre1-140X_mcRun3_2024_realistic_v1_STD_2024_PU_RecoOnly-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_1_0_pre3-140X_mcRun3_2024_realistic_v7_STD_2024_PU_RecoOnly-v2__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_1_0_pre4-140X_mcRun3_2024_realistic_v8_STD_2024_PU_RecoOnly-v1__DQMIO.root'],
    ['+', 'DQM_V0002_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_14_1_0_pre6-140X_mcRun3_2024_realistic_v15_STD_2024_PU_RecoOnly-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZpToEE_m6000_14TeV__CMSSW_15_0_0_pre1-PU_142X_mcRun3_2025_realistic_v1_STD_RecoOnly_2025_PU-v1__DQMIO.root'],
]

# RelValZEE_14-mcRun3-PU-RecoOnly
rootSourcesRelValZEE_14mcRun3PURecoOnly = [
    ['*', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_1_0-140X_mcRun3_2024_realistic_v21_STD_RecoOnly_2024_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_1_0_pre1-140X_mcRun3_2024_realistic_v1_STD_2024_PU_RecoOnly-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_1_0_pre3-140X_mcRun3_2024_realistic_v7_STD_2024_PU_RecoOnly-v2__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_1_0_pre4-140X_mcRun3_2024_realistic_v8_STD_2024_PU_RecoOnly-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_1_0_pre5-140X_mcRun3_2024_realistic_v11_STD_2024_PU_RecoOnly-v1__DQMIO.root'],
    ['+', 'DQM_V0002_R000000001__RelValZEE_14__CMSSW_14_1_0_pre6-140X_mcRun3_2024_realistic_v15_STD_2024_PU_RecoOnly-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_1_0_pre7-140X_mcRun3_2024_realistic_v15_STD_RecoOnly_2024_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre1-PU_140X_mcRun3_2024_realistic_v21_STD_RecoOnly_2024_PU-v2__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre2-140X_mcRun3_2024_realistic_v21_STD_RecoOnly_2024_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre3-PU_140X_mcRun3_2024_realistic_v25_STD_RecoOnly_2024_PU-v2__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre4-140X_mcRun3_2024_realistic_v26_STD_RecoOnly_2024_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre1-PU_142X_mcRun3_2025_realistic_v1_STD_RecoOnly_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre2-PU_142X_mcRun3_2025_realistic_v4_STD_RecoOnly_2025_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre3-PU_142X_mcRun3_2025_realistic_v4_STD_RecoOnly_2025_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0-PU_142X_mcRun3_2025_realistic_v5_STD_RecoOnly_2025_PU-v3__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre1-PU_142X_mcRun3_2025_realistic_v5_STD_RecoOnly_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre2-142X_mcRun3_2025_realistic_v7_STD_RecoOnly_2025_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre3-150X_mcRun3_2025_realistic_v1_STD_RecoOnly_2025_PU-v1__DQMIO.root'],
]

# RelValZEE_14-mcRun4-PU-RecoOnly
rootSourcesRelValZEE_14mcRun4PURecoOnly = [
    ['*', 'DQM_V0002_R000000001__RelValZEE_14__CMSSW_14_1_0_pre7-141X_mcRun4_realistic_v1_STD_RecoOnly_2026D110_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre1-141X_mcRun4_realistic_v1_STD_RecoOnly_2026D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre3-PU_141X_mcRun4_realistic_v3_STD_RecoOnly_2026D110_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre4-141X_mcRun4_realistic_v3_STD_RecoOnly_2026D110_PU-v1__DQMIO.root'],
    ['-', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_2_0_pre4-PU_141X_mcRun4_realistic_v3_STD_RecoOnly_2026D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre1-PU_141X_mcRun4_realistic_v3_STD_RecoOnly_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre2-141X_mcRun4_realistic_v3_STD_RecoOnly_Run4D110_PU-v2__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_0_0_pre3-PU_141X_mcRun4_realistic_v3_STD_RecoOnly_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre1-PU_141X_mcRun4_realistic_v3_STD_RecoOnly_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre2-PU_150X_mcRun4_realistic_v1_STD_RecoOnly_Run4D110_PU-v1__DQMIO.root'],
    ['+', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_15_1_0_pre3-PU_150X_mcRun4_realistic_v1_STD_RecoOnly_Run4D110_PU-v2__DQMIO.root'],
]

'''
'''