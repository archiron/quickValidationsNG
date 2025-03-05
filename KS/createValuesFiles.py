#! /usr/bin/env python
#-*-coding: utf-8 -*-

################################################################################
# createAndCompare : create file for Kolmogorov-Smirnov maximum diff and generate
# pictures for releases comparison
# Only work for ZEE_14
#
# Arnaud Chiron-Turlay LLR - arnaud.chiron@llr.in2p3.fr                        
#                                                                              
################################################################################

from genericpath import exists
import os,sys,re
import time

sys.path.append('../../ChiLib_CMS_Validation')

# lines below are only for func_Extract
from sys import argv

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gErrorIgnoreLevel = ROOT.kFatal # ROOT.kBreak # 
ROOT.PyConfig.DisableRootLogon = True
ROOT.PyConfig.IgnoreCommandLineOptions = True

#from ROOT import gROOT
root_version = ROOT.gROOT.GetVersion()

import pandas as pd
import numpy as np

print('PYTHON     version : {}'.format(sys.version))
print("NUMPY      version : {}".format(np.__version__))
print("ROOT      version : {}".format(root_version))

print("\ncreateValuesFiles")

pathBase = os.getcwd()[:-3]
print('result path : {:s}'.format(pathBase))

pathChiLib = pathBase[:-19] + '/ChiLib_CMS_Validation'
print('Lib path : {:s}'.format(pathChiLib))

pathValues = os.getcwd() + '/Values/'
print('Values path : {:s}'.format(pathValues))

from controlFunctions import *
from graphicFunctions import Graphic
from functions import *
from networkFunctions import networkFunctions
from valEnv_default import env_default
from rootSources import *

gr = Graphic()
gr.initRoot()
tl = Tools()

sys.path.append(os.getcwd()) # path where you work
valEnv_d = env_default()
net = networkFunctions()

pathDATA = pathBase + '/DATA/'
print('path DATA {:s}'.format(pathDATA))

tp_list1 = ['ElectronMcSignalValidator', 'ElectronMcSignalValidatorMiniAOD']
it_list1 = ['/HistosConfigFiles/ElectronMcSignalHistos.txt', '/HistosConfigFiles/ElectronMcSignalHistosMiniAOD.txt']
tp_list2 = ['ElectronMcSignalValidator']
it_list2 = ['/HistosConfigFiles/ElectronMcSignalHistos.txt']

tic = time.time()

for elem in rootList:
    print('\ntableau : {:s}'.format(elem))
    pathTable = pathValues + elem
    print('chemin : {:s}'.format(pathTable))
    tl.checkCreateWebFolder(pathTable)

    tmp = elem.replace("rootSources", "")
    tmp2 = tmp.split('mcRun')
    dataset = tmp2[0][6:]
    choice = 'mcRun' + tmp2[1][0]
    relrefVT = tmp2[1][1:]
    recOnly = ''
    tp_list = tp_list1
    it_list = it_list1
    if (len(relrefVT) > 4):
        recOnly = 'RecoOnly'
        #print(relrefVT)
        #relrefVT = relrefVT.replace('RecoOnly', '')
        relrefVT = relrefVT[:-8]
        #print(relrefVT)
    print(dataset, choice, relrefVT, recOnly)
    if (relrefVT == 'PU'):
        tp_list = tp_list2 # liste des chemins dans les fichiers ROOT
        it_list = it_list2
    print('tp_list', tp_list)
    rootSources = locals()[str(elem)]
    #print(rootSources)
    for file in rootSources:
        print('fichier : {:s}'.format(file[1])) # fichier ROOT

        # get the branches for ElectronMcSignalHistos.txt
        i = 0
        for it in it_list:
            fileName = pathTable + '/' + file[1].split('.')[0] + '_' + str(i) + '.txt' # fichier text correspondant au fichier ROOT
            print('fichier : {:s}'.format(fileName))
            fichier = open(fileName, "w")
            branches = []
            print('ip', it)
            print('i', i)
            source = pathChiLib + it
            print('tp_list', tp_list)
            tp = tp_list[i]
            print('source %s' % source)
            print('tp : {:s}'.format(tp))
            branches = getBranches(tp, source)
            cleanBranches(branches) # remove some histo wich have a pbm with KS.
            N_histos = len(branches)
            print('N_histos : %d' % N_histos)
            f_root = ROOT.TFile(pathDATA + file[1])
            h_rel = gr.getHisto(f_root, tp)
            for ii in range(0, N_histos):#, N_histos-1 range(N_histos - 1, N_histos):  # 1 N_histos histo for debug
                #print('histo : {:s}'.format(branches[i])) # print histo name
                histo_rel = h_rel.Get(branches[ii])
                if (histo_rel):
                    print('%s OK' % branches[ii])
                    s_new = []
                    for entry in histo_rel:
                        s_new.append(entry)
                    s_new = np.asarray(s_new)
                    s_new = s_new[1:-1]
                    fichier.write('{:s} '.format(branches[ii]))
                    fichier.write(' '.join("{:10.04e}".format(x) for x in s_new))
                    fichier.write('\n')
                else:
                    print('%s KO' % branches[i])

            i +=1

        fichier.close()

toc = time.time()
print('Done in {:.4f} seconds'.format(toc-tic))

print("Fin !")
