#! /usr/bin/env python
#-*-coding: utf-8 -*-

################################################################################
# validations.py : list of ROOT files to be used with as couples for egamma
# validation comparison                              
# 
# called with compareValidations.py script
#                                                                              
# Arnaud Chiron-Turlay LLR - arnaud.chiron@llr.in2p3.fr                        
#                                                                              
################################################################################

# definition '-' : not selected
#            '+' : selected
#            '*' : selected AND reference

# get the "sources" root file datas
validations_RECO = [
    ['15_0_0_pre1-2025', 'CMSSW_15_0_0_pre1-140X_mcRun3_2024_realistic_v26_STD_RecylcedGS_2024_noPU-v1', 'CMSSW_14_2_0_pre4-140X_mcRun3_2024_realistic_v26_STD_RecylcedGS_2024_noPU-v1'],
    ['15_0_0_pre2-2025', 'CMSSW_15_0_0_pre2-142X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1', 'CMSSW_15_0_0_pre1-142X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_noPU-v1'],
    ['15_0_0_pre3-2025', 'CMSSW_15_0_0_pre3-142X_mcRun3_2025_realistic_v5_STD_RecycledGS_2025_noPU-v1', 'CMSSW_15_0_0_pre2-142X_mcRun3_2025_realistic_v2_STD_RegeneratedGS_2025_noPU-v1'],
    ['15_0_0-2025', 'CMSSW_15_0_0-142X_mcRun3_2025_realistic_v7_STD_RegeneratedGS_2025_noPU-v1', 'CMSSW_15_0_0_pre3-142X_mcRun3_2025_realistic_v5_STD_RegeneratedGS_2025_noPU-v2'],
    ['15_1_0_pre1-2025', 'CMSSW_15_1_0_pre1-142X_mcRun3_2025_realistic_v7_STD_RegeneratedGS_2025_noPU-v1', 'CMSSW_15_0_0-142X_mcRun3_2025_realistic_v7_STD_RegeneratedGS_2025_noPU-v1'],
    ['15_1_0_pre2-2025', 'CMSSW_15_1_0_pre2-150X_mcRun3_2025_realistic_v1_STD_RegeneratedGS_2025_noPU-v1', 'CMSSW_15_1_0_pre1-142X_mcRun3_2025_realistic_v7_STD_RegeneratedGS_2025_noPU-v1'],
    ['15_1_0_pre3-2025', 'CMSSW_15_1_0_pre3-150X_mcRun3_2025_realistic_v2_STD_RegeneratedGS_2025_noPU-v1', 'CMSSW_15_1_0_pre2-150X_mcRun3_2025_realistic_v1_STD_RegeneratedGS_2025_noPU-v1'],
    ['15_1_0_pre4-2025', 'CMSSW_15_1_0_pre4-150X_mcRun3_2025_realistic_v2_STD_RecycledGS_2025_noPU-v1', 'CMSSW_15_1_0_pre3-150X_mcRun3_2025_realistic_v2_STD_RegeneratedGS_2025_noPU-v1'],
    ['15_1_0_pre5-2025', 'CMSSW_15_1_0_pre5-151X_mcRun3_2025_realistic_v3_STD_RecycledGS_2025_noPU-v1', 'CMSSW_15_1_0_pre4-151X_mcRun3_2025_realistic_v3_STD_RegeneratedGS_2025_noPU-v1'],
    ['15_1_0_pre6-2025', 'CMSSW_15_1_0_pre6-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1', 'CMSSW_15_1_0_pre5-151X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_noPU-v1'],
    ['15_1_0-2025', 'CMSSW_15_1_0-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v2', 'CMSSW_15_1_0_pre6-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v2'],
    ['16_0_0_pre1-2025', 'CMSSW_16_0_0_pre1-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1', 'CMSSW_15_1_0_pre6-151X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_noPU-v1'],
    ['16_0_0_pre2-2025', 'CMSSW_16_0_0_pre2-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1', 'CMSSW_16_0_0_pre1-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1'],
    ['16_0_0_pre3-2025', 'CMSSW_16_0_0_pre3-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1', 'CMSSW_16_0_0_pre2-151X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_noPU-v1'],
    ['16_0_0_pre4-2025', 'CMSSW_16_0_0_pre4-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v2', 'CMSSW_16_0_0_pre3-151X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_noPU-v1'],
]

validations_PU = [
    ['15_0_0_pre1-2025', 'CMSSW_15_0_0_pre1-PU_140X_mcRun3_2024_realistic_v26_STD_2024_PU-v1', 'CMSSW_14_2_0_pre4-PU_140X_mcRun3_2024_realistic_v26_STD_2024_PU-v1'],
    ['15_0_0_pre2-2025', 'CMSSW_15_0_0_pre2-PU_142X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_PU-v1', 'CMSSW_15_0_0_pre1-PU_142X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_PU-v3'],
    ['15_0_0_pre3-2025', 'CMSSW_15_0_0_pre3-PU_142X_mcRun3_2025_realistic_v5_STD_2025_PU-v1', 'CMSSW_15_0_0_pre2-PU_142X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_PU-v1'],
    ['15_0_0-2025', 'CMSSW_15_0_0-PU_142X_mcRun3_2025_realistic_v7_STD_2025_PU-v2', 'CMSSW_15_0_0_pre3-PU_142X_mcRun3_2025_realistic_v5_STD_2025_PU-v2'],
    ['15_1_0_pre1-2025', 'CMSSW_15_1_0_pre1-PU_142X_mcRun3_2025_realistic_v7_STD_2025_PU-v1', 'CMSSW_15_0_0-PU_142X_mcRun3_2025_realistic_v7_STD_2025_PU-v2'],
    ['15_1_0_pre2-2025', 'CMSSW_15_1_0_pre2-PU_150X_mcRun3_2025_realistic_v1_STD_2025_PU-v1', 'CMSSW_15_1_0_pre1-PU_142X_mcRun3_2025_realistic_v7_STD_2025_PU-v1'],
    ['15_1_0_pre3-2025', 'CMSSW_15_1_0_pre3-PU_150X_mcRun3_2025_realistic_v2_STD_2025_PU-v2', 'CMSSW_15_1_0_pre2-PU_150X_mcRun3_2025_realistic_v1_STD_2025_PU-v1'],
    ['15_1_0_pre4-2025', 'CMSSW_15_1_0_pre4-PU_151X_mcRun3_2025_realistic_v3_STD_2025_PU-v1', 'CMSSW_15_1_0_pre3-PU_150X_mcRun3_2025_realistic_v2_STD_2025_PU-v2'],
    ['15_1_0_pre5-2025', 'CMSSW_15_1_0_pre5-PU_151X_mcRun3_2025_realistic_v4_STD_2025_PU-v2', 'CMSSW_15_1_0_pre4-PU_151X_mcRun3_2025_realistic_v3_STD_2025_PU-v1'],
    ['15_1_0_pre6-2025', 'CMSSW_15_1_0_pre6-PU_151X_mcRun3_2025_realistic_v4_STD_2025_PU-v1', 'CMSSW_15_1_0_pre5-PU_151X_mcRun3_2025_realistic_v4_STD_2025_PU-v2'],
    ['15_1_0-2025', 'CMSSW_15_1_0-PU_151X_mcRun3_2025_realistic_v4_STD_2025_PU-v1', 'CMSSW_15_1_0_pre6-PU_151X_mcRun3_2025_realistic_v4_STD_2025_PU-v1'],
    ['16_0_0_pre1-2025', 'CMSSW_16_0_0_pre1-PU_151X_mcRun3_2025_realistic_v4_STD_2025_PU-v1', 'CMSSW_15_1_0_pre6-PU_151X_mcRun3_2025_realistic_v4_STD_2025_PU-v1'],
    ['16_0_0_pre2-2025', 'CMSSW_16_0_0_pre2-PU_151X_mcRun3_2025_realistic_v4_STD_2025_PU-v1', 'CMSSW_16_0_0_pre1-PU_151X_mcRun3_2025_realistic_v4_STD_2025_PU-v1'],
    ['16_0_0_pre3-2025', 'CMSSW_16_0_0_pre3-PU_151X_mcRun3_2025_realistic_v4_STD_2025_PU-v1', 'CMSSW_16_0_0_pre2-PU_151X_mcRun3_2025_realistic_v4_STD_2025_PU-v1'],
    ['16_0_0_pre4-2025', 'CMSSW_16_0_0_pre4-PU_151X_mcRun3_2025_realistic_v4_STD_2025_PU-v2', 'CMSSW_16_0_0_pre3-PU_151X_mcRun3_2025_realistic_v4_STD_2025_PU-v1'],
]

validations_miniAOD = [
    ['15_0_0_pre1-2025', 'CMSSW_15_0_0_pre1-140X_mcRun3_2024_realistic_v26_STD_RecylcedGS_2024_noPU-v1', 'CMSSW_15_0_0_pre1-140X_mcRun3_2024_realistic_v26_STD_RecylcedGS_2024_noPU-v1'],
    ['15_0_0_pre2-2025', 'CMSSW_15_0_0_pre2-142X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1', 'CMSSW_15_0_0_pre2-142X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1'],
    ['15_0_0_pre3-2025', 'CMSSW_15_0_0_pre3-142X_mcRun3_2025_realistic_v5_STD_RecycledGS_2025_noPU-v1', 'CMSSW_15_0_0_pre3-142X_mcRun3_2025_realistic_v5_STD_RecycledGS_2025_noPU-v1'],
    ['15_0_0-2025', 'CMSSW_15_0_0-PU_142X_mcRun3_2025_realistic_v7_STD_2025_PU-v2', 'CMSSW_15_0_0_pre3-PU_142X_mcRun3_2025_realistic_v5_STD_2025_PU-v2'],
    ['15_1_0_pre1-2025', 'CMSSW_15_1_0_pre1-142X_mcRun3_2025_realistic_v7_STD_RegeneratedGS_2025_noPU-v1', 'CMSSW_15_1_0_pre1-142X_mcRun3_2025_realistic_v7_STD_RegeneratedGS_2025_noPU-v1'],
    ['15_1_0_pre2-2025', 'CMSSW_15_1_0_pre2-150X_mcRun3_2025_realistic_v1_STD_RegeneratedGS_2025_noPU-v1', 'CMSSW_15_1_0_pre2-150X_mcRun3_2025_realistic_v1_STD_RegeneratedGS_2025_noPU-v1'],
    ['15_1_0_pre3-2025', 'CMSSW_15_1_0_pre3-150X_mcRun3_2025_realistic_v2_STD_RegeneratedGS_2025_noPU-v1', 'CMSSW_15_1_0_pre3-150X_mcRun3_2025_realistic_v2_STD_RegeneratedGS_2025_noPU-v1'],
    ['15_1_0_pre4-2025', 'CMSSW_15_1_0_pre4-150X_mcRun3_2025_realistic_v2_STD_RecycledGS_2025_noPU-v1', 'CMSSW_15_1_0_pre4-150X_mcRun3_2025_realistic_v2_STD_RecycledGS_2025_noPU-v1'],
    ['15_1_0_pre5-2025', 'CMSSW_15_1_0_pre5-151X_mcRun3_2025_realistic_v3_STD_RecycledGS_2025_noPU-v1', 'CMSSW_15_1_0_pre5-151X_mcRun3_2025_realistic_v3_STD_RecycledGS_2025_noPU-v1'],
    ['15_1_0_pre6-2025', 'CMSSW_15_1_0_pre6-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1', 'CMSSW_15_1_0_pre6-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1'],
    ['15_1_0-2025', 'CMSSW_15_1_0-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v2', 'CMSSW_15_1_0-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v2'],
    ['16_0_0_pre1-2025', 'CMSSW_16_0_0_pre1-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1', 'CMSSW_16_0_0_pre1-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1'],
    ['16_0_0_pre2-2025', 'CMSSW_16_0_0_pre2-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1', 'CMSSW_16_0_0_pre2-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1'],
    ['16_0_0_pre3-2025', 'CMSSW_16_0_0_pre3-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1', 'CMSSW_16_0_0_pre3-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v1'],
    ['16_0_0_pre4-2025', 'CMSSW_16_0_0_pre4-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v2', 'CMSSW_16_0_0_pre4-151X_mcRun3_2025_realistic_v4_STD_RecycledGS_2025_noPU-v2'],
]
