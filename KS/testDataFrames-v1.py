#! /usr/bin/env python
#-*-coding: utf-8 -*-

################################################################################
# createAndCompare : create file for Kolmogorov-Smirnov maximum diff and generate
# pictures for releases comparison
# V2
#
# Arnaud Chiron-Turlay LLR - arnaud.chiron@llr.in2p3.fr                        
#                                                                              
################################################################################

from genericpath import exists
import os,sys,re
import importlib
import importlib.machinery
import importlib.util
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

import uproot as up
import pandas as pd
import numpy as np
import matplotlib

print('PANDAS     version : {}'.format(pd.__version__))
print('PYTHON     version : {}'.format(sys.version))
print("NUMPY      version : {}".format(np.__version__))
print('MATPLOTLIB version : {}'.format(matplotlib.__version__))
print("ROOT      version : {}".format(root_version))

# import matplotlib.dates as md
matplotlib.use('agg')
#from matplotlib import pyplot as plt

print("\ncreateAndCompare")

extFile = sys.argv[1]
CompleteExtFile = os.getcwd()+'/'+ extFile
# Import module
loader = importlib.machinery.SourceFileLoader( extFile, CompleteExtFile )
spec = importlib.util.spec_from_loader( extFile, loader )
cf2 = importlib.util.module_from_spec( spec )
loader.exec_module( cf2 )

pathBase = os.getcwd()[:-3]
print('result path : {:s}'.format(pathBase))

pathChiLib = pathBase[:-19] + '/ChiLib_CMS_Validation'
print('Lib path : {:s}'.format(pathChiLib))

tp_1 = 'ElectronMcSignalValidator'

from controlFunctions import *
from graphicFunctions import Graphic
from DecisionBox import DecisionBox
from rootSources import *
from functions import *
from networkFunctions import networkFunctions
from valEnv_default import env_default

gr = Graphic()
gr.initRoot()
tl = Tools()

Validation_reference = cf2.Validation_reference
web_repo = cf2.web_repo
tl.p_cf2(cf2)
picture_ext = cf2.picture_ext
tl.checkPictureExt(picture_ext)

sys.path.append(os.getcwd()) # path where you work
valEnv_d = env_default()
DB = DecisionBox()
net = networkFunctions()

pathDATA = pathBase + '/DATA/'
print('path DATA {:s}'.format(pathDATA))

mods = dir(cf2)
listGeV = []
for elem in mods:
    if re.search('GeV_', elem):
        listGeV.append(elem)
print(listGeV)

tic = time.time()
for valGeV in listGeV: # loop over GUI configurations
    validation = getattr(cf2, valGeV)
    release = validation[0][0]
    reference = validation[0][1]
    shortRelease = release[6:] # CMSSW_ removed
    shortReference = reference[6:] # CMSSW_ removed
    releaseExtent = validation[1][0]
    referenceExtent = validation[1][1]
    choiceT = validation[3] # Must be FullvsFull
    relrefVT = validation[4] # RECO, RECO

    # get config files
    print('{:s}'.format(valGeV))
    (it1, it2, tp_1, tp_2) = tl.testForDataSetsFile2(pathChiLib + '/HistosConfigFiles/', relrefVT)
    tl.p_valPaths(it1, it2, tp_1, tp_2, os.getcwd(), pathChiLib)
    print('it1 : {:s}'.format(it1))
    print('it2 : {:s}'.format(it2))
    print('tp_1 : {:s}'.format(tp_1))
    print('tp_2 : {:s}'.format(tp_2))
    if (tp_2 == 'ElectronMcSignalValidatorMiniAOD'):
        tp_1 = tp_2
    
    # print variables
    #tl.p_RelRef(validation, release, reference, shortRelease, shortReference, releaseExtent, referenceExtent, choiceT, web_repo, validation[7], relrefVT, valEnv_d.KS_Path())
    if ((relrefVT[0] == 'RECO') and (relrefVT[1] == 'RECO')):
        choice = 'RECO'
    elif ((relrefVT[0] == 'RECO') and (relrefVT[1] == 'miniAOD')):
        choice = 'RECO'
    elif ((relrefVT[0] == 'PU') and (relrefVT[1] == 'PU')):
        choice = 'PU'
    print('choice = {:s}'.format(choice))

    #if ((relrefVT[0] == 'RECO') and (relrefVT[1] == 'RECO')):
    if ( referenceExtent != '' ):
        webFolder = choiceT + '_' + reference + "_" + referenceExtent
    else:
        webFolder = choiceT + '_' + reference
    if ( releaseExtent != '' ):
        webFolder = shortRelease + "_" + releaseExtent + "_DQM_" + web_repo[1] + '/' + webFolder
    else:
        webFolder = shortRelease + "_DQM_" + web_repo[1] + '/' + webFolder
    shortWebFolder = webFolder
    webFolder = web_repo[0] + webFolder + '/'
    print('webFolder : {:s}'.format(webFolder))

    tl.checkCreateWebFolder(webFolder)

    datasets = validation[2]
    N = len(datasets)
    print('For %s there is %d datasets : %s' % (valGeV, N, datasets))
    globalTag = validation[5]
    #print(globalTag)

    # get the branches for ElectronMcSignalHistos.txt
    branches = []
    source = it1 # pathChiLib + "/HistosConfigFiles/ElectronMcSignalHistos.txt"
    print('source %s' % source)
    branches = getBranches(tp_1, source)
    cleanBranches(branches) # remove some histo wich have a pbm with KS.

    N_histos = len(branches)
    print('N_histos : %d' % N_histos)

    #dts = 'ZEE_14'
    for dts in datasets:
        print('\n{:s}[{:s}]'.format(valGeV, dts))
        
        leNom = 'rootSourcesRelVal' + dts
        if (releaseExtent == 'PHASE2'):
            leNom += 'mcRun4'
        else:
            leNom += 'mcRun3'
        leNom += relrefVT[0]
        if ('Only' in referenceExtent):
            leNom += 'RecoOnly'

        print('leNom calculé : {:s}'.format(leNom))
    
        rootSources = locals()[leNom]
        print(rootSources)
        #Stop()

        rels = []
        tmp_branches = []
        nb_ttl_histos = []
        rels2 = []
        tmp_branches2 = []
        nb_ttl_histos2 = []

        os.chdir(webFolder) # going into finalFolder

        # create folder 
        dataSetFolder = str(relrefVT[0] + '-' + relrefVT[1] + '_' + dts)
        if (relrefVT[2] != ''):
            dataSetFolder = str(relrefVT[2] + '-') + dataSetFolder
        tl.createDatasetFolder(dataSetFolder, picture_ext) # gifs / pngs
        os.chdir(dataSetFolder) # going to dataSetFolder

        # create first picture other the partial release list
        tmpSource1 = []
        for elem in rootSources:
            #print(elem)
            if (elem[0] == '+') :
                tmpSource1.append(1)
            else:
                tmpSource1.append(0)
        rootFilesList = []

        # create first picture other the total release list
        tmpSource2 = []
        for elem in rootSources:
            print(elem)
            tmpSource2.append(elem[1])
            if (elem[0] == '*'):
                # extract release from source reference
                input_ref_file = elem[1]
                release = elem[1].split('__')[2].split('-')[0]
                print('extracted release : {:s}'.format(release))
        rootFilesList2 = []
        for elem in tmpSource2:
            print('elem : {:s}'.format(elem))
            name = pathDATA + '/' + elem
            if exists(name):
                rootFilesList2.append(elem)
            else:
                print("{:s} n'existe pas".format(name))
        print(rootFilesList2)
        rootFilesList2=rootFilesList2[0:2]

        print('we use the files :')
        for item in rootFilesList2:
            tmp_branch = []
            nbHistos = 0
            print('\n%s' % item)
            b = (item.split('__')[2]).split('-')
            rels2.append([b[0], b[0][6:], item])
            f_root = ROOT.TFile(pathDATA + item)
            h_rel = gr.getHisto(f_root, tp_1)
            for i in range(0, 2): # 1 N_histos histo for debug
                histo_rel = h_rel.Get(branches[i])
                print('[{:03d}] : {:s}'.format(i, branches[i]))
                if (histo_rel):
                    d = gr.getHistoConfEntry(histo_rel)
                    ibin=0
                    for entry in range(0,histo_rel.GetXaxis().GetNbins()): #histo_rel:
                        #print('{:f}'.format(entry))
                        print('[{:03d}] : {:f}'.format(ibin, histo_rel.GetBinContent(ibin)))
                        ibin+=1
                    '''s_tmp = gr.fill_Snew2(d, histo_rel)
                    if (s_tmp.min() < 0.):
                        print('pbm whith histo %s, min < 0' % branches[i])
                    elif (np.floor(s_tmp.sum()) == 0.):
                        print('pbm whith histo %s, sum = 0' % branches[i])
                    else:
                        nbHistos += 1
                        tmp_branch.append(branches[i])'''
                else:
                    print('%s KO' % branches[i])

        print('N_histos : %d' % N_histos)

        # get the "reference" root file datas
        f_KSref = ROOT.TFile(pathDATA + input_ref_file)
        print('we use the {:s} file as KS reference'.format(input_ref_file))
        file_KS = up.open(pathDATA + input_ref_file)

        h_KSref = gr.getHisto(f_KSref, tp_1)
        print(h_KSref)

        print('###### new loop #######')
        for ij in range(0, 2):#, N_histos-1 range(N_histos - 1, N_histos):  # 1 N_histos histo for debug
            print('[{:03d}] : {:s}'.format(ij, branches[ij]))

            # create the datas for the p-Value graph
            # by comparing 1 curve with the others.
            histo_KSref = h_KSref.Get(branches[ij])
            s_KSref = []
            for jbin in range(0,histo_KSref.GetXaxis().GetNbins()):#histo_KSref:
                s_KSref.append(histo_KSref.GetBinContent(jbin))
            s_KSref = np.asarray(s_KSref)
            #s_KSref = s_KSref[1:-1]
            print('s_KSref has {:d} elements'.format(len(s_KSref)))
            hist = file_KS["DQMData/Run 1/EgammaV/Run summary/ElectronMcSignalValidator/" + branches[ij]]
            s_KSref2 = gr.histogram_to_dataframe2(hist)
            tl.p_histoValues(s_KSref2)

            # Afficher sous forme de tableau
            print(f"{'Bin':>5} | {'Xmin':>10} | {'Xmax':>10} | {'Content':>10} | {'Error':>10}")
            print("-" * 55)

            #nbins = histo_KSref.GetXaxis().GetNbins()
            nbins = histo_KSref.GetNbinsX()
            print('nbins: {:03d}'.format(nbins))

            for i in range(1, nbins + 1):  # ROOT bins commencent à 1
                x_min = histo_KSref.GetBinLowEdge(i)
                x_max = x_min + histo_KSref.GetBinWidth(i)
                content = histo_KSref.GetBinContent(i)
                error = histo_KSref.GetBinError(i)
                print(f"{i:5} | {x_min:10.2f} | {x_max:10.2f} | {content:10.2f} | {error:10.2f}")

            root_file = pathDATA + input_ref_file
            print(root_file)
            aaa = gr.histogram_to_dataframe(root_file, "DQMData/Run 1/EgammaV/Run summary/ElectronMcSignalValidator/" + branches[ij])
            print(aaa)
            print(aaa.shape)

        else:
            print('%s KO' % branches[ij])

    toc = time.time()
    print('Done in {:.4f} seconds'.format(toc-tic))

print("Fin !")
