#! /usr/bin/env python
#-*-coding: utf-8 -*-

###########################################################################
# compareValidations : create file for Kolmogorov-Smirnov maximum diff and 
# create pictures for releases comparison
# V1
#
# Arnaud Chiron-Turlay LLR - arnaud.chiron@llr.in2p3.fr                    
#                                                                          
###########################################################################

import os
import sys
import time
from collections import Counter
from itertools import chain

sys.path.append('../../ChiLib_CMS_Validation')

# lines below are only for func_Extract
from sys import argv

import ROOT
import pandas as pd
import numpy as np
import matplotlib

ROOT.gROOT.SetBatch(True)
ROOT.gErrorIgnoreLevel = ROOT.kFatal # ROOT.kBreak # 
ROOT.PyConfig.DisableRootLogon = True
ROOT.PyConfig.IgnoreCommandLineOptions = True

#from ROOT import gROOT
root_version = ROOT.gROOT.GetVersion()

print('PANDAS     version : {}'.format(pd.__version__))
print('PYTHON     version : {}'.format(sys.version))
print("NUMPY      version : {}".format(np.__version__))
print('MATPLOTLIB version : {}'.format(matplotlib.__version__))
print("ROOT      version : {}".format(root_version))

# import matplotlib.dates as md
matplotlib.use('agg')

print("\ncompareValidations V1")

pathBase = os.getcwd()[:-3]
print('result path : {:s}'.format(pathBase))

pathChiLib = pathBase[:-19] + '/ChiLib_CMS_Validation'
print('Lib path : {:s}'.format(pathChiLib))

tp_1 = 'ElectronMcSignalValidator'

from controlFunctions import getListFiles, getBranches, cleanBranches
from graphicFunctions import Graphic
from graphicAutoEncoderFunctions import createCompLossesPicture5
from DecisionBox import DecisionBox
from functions import *
from networkFunctions import networkFunctions
#from valEnv_default import env_default
from pprint import pprint

from validations import validations_RECO, validations_PU, validations_miniAOD

gr = Graphic()
gr.initRoot()
tl = Tools()

picture_ext = 'pngs' # gifs / pngs for picture format
web_repo = ['/eos/project/c/cmsweb/www/egamma/validation/Electrons/Releases/', 'std']
datasets = ['ZEE_14']
choiceT = 'FullvsFull' # Must be FullvsFull
relrefVT_RECO = ['RECO', 'RECO', ''] # RECO, RECO
relrefVT_PU = ['PU', 'PU', '']
relrefVT_miniAOD = ['RECO', 'miniAOD', '']
referenceExtent = ''
releaseExtent = ''

## Traitement RECO ##
tl.checkPictureExt(picture_ext)

sys.path.append(os.getcwd()) # path where you work
DB = DecisionBox()
net = networkFunctions()

pathDATA = pathBase + '/DATA/'
print('path DATA {:s}'.format(pathDATA))
rootFilesList_0 = getListFiles(pathDATA) # get the list of the root files in the folderName folder
if (len(rootFilesList_0) == 0 ):
    print('there is no ROOT files')
    exit()
else:
    print('there is {:d} ROOT files'.format(len(rootFilesList_0)))
rootFilesList_0.sort()
greatBallsOfFire = {} # array with all histos diff values for all cases

tic = time.time()
for valGeV in validations_RECO: # loop over GUI configurations
    print('\n########### ' + valGeV[0] + ' #############')
    relrefVT = relrefVT_RECO
    print(valGeV)
    release = valGeV[1].split("-")[0]
    reference = valGeV[2].split("-")[0]
    print('release : {:s} - reference : {:s}'.format(release, reference))
    shortRelease = release[6:] # CMSSW_ removed
    shortReference = reference[6:] # CMSSW_ removed

    # get config files
    (it1, it2, tp_1, tp_2) = tl.testForDataSetsFile2(pathChiLib + '/HistosConfigFiles/', relrefVT)
    tl.p_valPaths(it1, it2, tp_1, tp_2, os.getcwd(), pathChiLib)
    print('it1 : {:s}'.format(it1))
    print('it2 : {:s}'.format(it2))
    print('tp_1 : {:s} - tp_2 : {:s}'.format(tp_1, tp_2))
    if (tp_2 == 'ElectronMcSignalValidatorMiniAOD'):
        tp_1 = tp_2
    
    # print variables
    if ((relrefVT[0] == 'RECO') and (relrefVT[1] == 'RECO')):
        choice = 'RECO'
    elif ((relrefVT[0] == 'RECO') and (relrefVT[1] == 'miniAOD')):
        choice = 'RECO'
    elif ((relrefVT[0] == 'PU') and (relrefVT[1] == 'PU')):
        choice = 'PU'
    print('choice = {:s}'.format(choice))

    if ( referenceExtent != '' ):
        webFolder = shortReference + "_" + referenceExtent
    else:
        webFolder = shortReference
    if ( releaseExtent != '' ):
        webFolder = shortRelease + "_" + releaseExtent + "_vs_" + webFolder
    else:
        webFolder = shortRelease + "_vs_" + webFolder
    shortWebFolder = webFolder
    webFolder = pathBase + '/KS/GLOBOS/' + webFolder + '/'
    print('webFolder : {:s}'.format(webFolder))

    tl.checkCreateWebFolder(webFolder)

    N = len(datasets)
    print('For %s there is %d datasets : %s' % (valGeV, N, datasets))

    # get the branches for ElectronMcSignalHistos.txt
    branches = []
    source = it1
    print('source %s' % source)
    branches = getBranches(tp_1, source)
    cleanBranches(branches) # remove some histo wich have a pbm with KS.

    N_histos = len(branches)
    print('N_histos : %d' % N_histos)
        
    rootSources = [valGeV[1], valGeV[2]] # for comparison
    print(rootSources)
    os.chdir(webFolder) # going into finalFolder

    for dts in datasets:
        print('\n{:s}[{:s}]'.format(valGeV[0], dts))

        rootFilesList = []
        for ind in range(0,2):
            for elem in rootFilesList_0:
                elem2 = rootSources[ind]
                if ( (elem2 in elem) and (dts in elem) ):
                    rootFilesList.append(elem)
        #print(rootFilesList)

        rels = []
        tmp_branches = []

        print('for branch enumeration, we use the files :')
        for item in rootFilesList:
            tmp_branch = []
            nbHistos = 0
            print('\n%s' % item)
            b = (item.split('__')[2]).split('-')
            #sortedRels2.append([b[0], b[0][6:], item])
            f_root = ROOT.TFile(pathDATA + item)
            h_rel = gr.getHisto(f_root, tp_1)
            for i in range(0, N_histos): # 1 N_histos histo for debug
                histo_rel = h_rel.Get(branches[i])
                s_tmp = []
                if ( histo_rel ):
                    s_tmp = histo_rel.values()
                    #print('[{:03d}] : {:s} & {:d} for size'.format(i, branches[i], len(s_tmp)))

                    if (s_tmp.min() < 0.):
                        print('pbm whith histo %s, min < 0' % branches[i])
                    elif (np.floor(s_tmp.sum()) == 0.):
                        print('pbm whith histo %s, sum = 0' % branches[i])
                    else:
                        nbHistos += 1
                        tmp_branch.append(branches[i])
                else:
                    print('pbm with {:s}'.format(branches[i]))
                    s_tmp = []
            tmp_branches.append(tmp_branch)

        newBr2 = [val for sous_liste in tmp_branches for val in sous_liste]
        compteur = Counter(newBr2)
        d_occurrences = dict(compteur)
        c_min = min(d_occurrences.values())
        c_max = max(d_occurrences.values())
        print('[min, max] : [{:d}, {:d}]'.format(c_min, c_max))
        newBranches2 = [cle for cle, nb in d_occurrences.items() if nb == c_max]
        #pprint(newBranches2)

        if (len(branches) != len(newBranches2)):
            print('len std branches : {:d}'.format(len(branches)))
            print('len new branches : {:d}'.format(len(newBranches2)))
            branches = newBranches2
            N_histos = len(branches)

        print('N_histos : %d' % N_histos)
        N_histos = 15 # TEMPORAIRE

        # get the root file datas
        f_KSref = ROOT.TFile(pathDATA + rootFilesList[1])
        h_KSref = gr.getHisto(f_KSref, tp_1)
        f_rel = ROOT.TFile(pathDATA + rootFilesList[0])
        h_rel = gr.getHisto(f_rel, tp_1)

        toto = {} # array with all histos diff.

        for i in range(0, N_histos):#, N_histos-1 range(N_histos - 1, N_histos):  # 1 N_histos histo for debug
            print('[{:03d}] - histo : {:s}'.format(i, branches[i])) # print histo name
            r_rels2 = []
            
            # by comparing 1 curve with the others.
            histo_KSref = h_KSref.Get(branches[i])
            s_KSref = histo_KSref.values()
            histo_rel = h_rel.Get(branches[i])
            s_rel = histo_rel.values()
            if (len(s_KSref) != len(s_rel)):
                print('pbm whith histo {:s}, lengths are not the same [{:d}, {:d}]'.format(branches[i], len(s_KSref), len(s_rel)))
                continue
            else:
                print('s_KSref and s_rel have {:d} elements'.format(len(s_KSref)))

            if (s_rel.min() < 0.):
                print('pbm whith histo %s, min < 0' % branches[i])
                continue
            if (np.floor(s_rel.sum()) == 0.):
                print('pbm whith histo %s, sum = 0' % branches[i])
                continue
            toto[branches[i]] = s_KSref - s_rel

        print()
        greatBallsOfFire[valGeV[0]] = toto
        
    #pprint('greatBallsOfFire')
    #pprint(greatBallsOfFire)

    greatK = list(greatBallsOfFire.keys())
    pprint(greatK)
    greatHistos = []
    greatDiffValues = {}
    for val in greatK:
        greatHistos.append(list(greatBallsOfFire[val].keys()))
    flat_greatHistos = list(set(list(chain.from_iterable(greatHistos))))

    for vul in flat_greatHistos: # pour chaque histo
        #print('vul ==> {:s}'.format(vul))
        val1 = []
        for val in greatK:
            val1.append(greatBallsOfFire[val][vul])
        #pprint(val1)
        nb1 = len(val1)
        #print('nb1 : {:d}'.format(nb1))
        diffValues = []
        for nb2 in range(0,nb1-1):
            s1 = val1[nb2]
            s2 = val1[nb2+1]
            diffMax0 = DB.diffMAXKS3c(s1, s2)
            diffValues.append(diffMax0)
        greatDiffValues[vul] = diffValues

    lab = greatK[1:]
    print('lab')
    print(lab)
    for vul in flat_greatHistos: # pour chaque histo
        diffValues2 = greatDiffValues[vul]
        #print('diffValues')
        #print(diffValues2)
        pictureName = webFolder + '/newDiff_comparison_' + vul + '_1.png'
        title = r"$\bf{total}$" + ' : diff values vs releases.'
        createCompLossesPicture5(lab, diffValues2, pictureName, title, 'Releases', 'max diff')
        #greatDiffValues.append(diffValues)
    
    #pprint(greatDiffValues)
    nb3 = len(greatDiffValues)
    print('nb3 ==> {:d}'.format(nb3))
    nb4 = 0
    sumDiffValues = np.asarray(greatDiffValues[flat_greatHistos[0]])
    #print('0', sumDiffValues)
    for nb4 in range(1,nb3):
        sumDiffValues += np.asarray(greatDiffValues[flat_greatHistos[nb4]])
    #print('sum', sumDiffValues)
    sumDiffValues /= N_histos
    print('mean', sumDiffValues)
    pictureName = webFolder + '/newSumDiff_comparison_1.png'
    title = r"$\bf{total}$" + ' : diff values vs releases.'
    createCompLossesPicture5(lab, sumDiffValues, pictureName, title, 'Releases', 'max diff')

    toc = time.time()
    print('Done in {:.4f} seconds\n'.format(toc-tic))

print("Fin !")
