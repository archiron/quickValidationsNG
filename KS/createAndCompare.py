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
from graphicAutoEncoderFunctions import createCompLossesPicture, createCompLossesPicture3
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
    
        '''if (dts == 'ZEE_14'):
            if (relrefVT[0] == 'RECO'):
                if (releaseExtent == 'PHASE2'):
                    rootSources = rootSourcesRelValZEE_14mcRun4RECO
                    print('leNom1 : rootSourcesRelValZEE_14mcRun4RECO')
                else:
                    rootSources = rootSourcesRelValZEE_14mcRun3RECO
                    print('leNom1 : rootSourcesRelValZEE_14mcRun3RECO')
            elif (relrefVT[0] == 'PU'):
                if (releaseExtent == 'PHASE2'):
                    rootSources = rootSourcesRelValZEE_14mcRun4PU
                    print('leNom1 : rootSourcesRelValZEE_14mcRun4PU')
                else:
                    rootSources = rootSourcesRelValZEE_14mcRun3PU
                    print('leNom1 : rootSourcesRelValZEE_14mcRun3PU')
            else:
                print('Houston we have a pbm !!!')
                exit()
        elif (dts == 'TTbar_14TeV'):
            if (relrefVT[0] == 'RECO'):
                if (releaseExtent == 'PHASE2'):
                    rootSources = rootSourcesRelValTTbar_14TeVmcRun4RECO
                    print('leNom1 : rootSourcesRelValTTbar_14TeVmcRun4RECO')
                else:
                    rootSources = rootSourcesRelValTTbar_14TeVmcRun3RECO
                    print('leNom1 : rootSourcesRelValTTbar_14TeVmcRun3RECO')
            elif (relrefVT[0] == 'PU'):
                if (releaseExtent == 'PHASE2'):
                    rootSources = rootSourcesRelValTTbar_14TeVmcRun4PU
                    print('leNom1 : rootSourcesRelValTTbar_14TeVmcRun4PU')
                else:
                    rootSources = rootSourcesRelValTTbar_14TeVmcRun3PU
                    print('leNom1 : rootSourcesRelValTTbar_14TeVmcRun3PU')
            else:
                print('Houston we have a pbm !!!')
                exit()
        elif (dts == 'SingleEFlatPt2To100'):
            if (relrefVT[0] == 'RECO'):
                rootSources = rootSourcesRelValSingleEFlatPt2To100mcRun4RECO
                print('leNom1 : rootSourcesRelValSingleEFlatPt2To100mcRun4RECO')
            elif (relrefVT[0] == 'PU'):
                rootSources = rootSourcesRelValSingleEFlatPt2To100mcRun4PU
                print('leNom1 : rootSourcesRelValSingleEFlatPt2To100mcRun4PU')
            else:
                print('Houston we have a pbm !!!')
                exit()
        elif (dts == 'ZpToEE_m6000_14TeV'):
            if (relrefVT[0] == 'RECO'):
                rootSources = rootSourcesRelValZpToEE_m6000_14TeVmcRun3RECO
                print('leNom1 : rootSourcesRelValZpToEE_m6000_14TeVmcRun3RECO')
            elif (relrefVT[0] == 'PU'):
                rootSources = rootSourcesRelValZpToEE_m6000_14TeVmcRun3PU
                print('leNom1 : rootSourcesRelValZpToEE_m6000_14TeVmcRun3PU')
            else:
                print('Houston we have a pbm !!!')
                exit()'''
        #print(rootSources)
        '''if (leNom == 'rootSourcesRelValZEE_14mcRun3RECO'):
            print('leNom2 : rootSourcesRelValZEE_14mcRun3RECO')
            rootSources = rootSourcesRelValZEE_14mcRun3RECO
        elif (leNom == 'rootSourcesRelValZEE_14mcRun3PU'):
            print('leNom2 : rootSourcesRelValZEE_14mcRun3PU')
            rootSources = rootSourcesRelValZEE_14mcRun3PU
        elif (leNom == 'rootSourcesRelValZEE_14mcRun4RECO'):
            print('leNom2 : rootSourcesRelValZEE_14mcRun4RECO')
            rootSources = rootSourcesRelValZEE_14mcRun4RECO
        elif (leNom == 'rootSourcesRelValZEE_14mcRun4PU'):
            print('leNom2 : rootSourcesRelValZEE_14mcRun4PU')
            rootSources = rootSourcesRelValZEE_14mcRun4PU
        elif (leNom == 'rootSourcesRelValTTbar_14TeVmcRun3RECO'):
            print('leNom2 : rootSourcesRelValTTbar_14TeVmcRun3RECO')
            rootSources = rootSourcesRelValTTbar_14TeVmcRun3RECO
        elif (leNom == 'rootSourcesRelValTTbar_14TeVmcRun3PU'):
            print('leNom2 : rootSourcesRelValTTbar_14TeVmcRun3PU')
            rootSources = rootSourcesRelValTTbar_14TeVmcRun3PU
        elif (leNom == 'rootSourcesRelValTTbar_14TeVmcRun4RECO'):
            print('leNom2 : rootSourcesRelValTTbar_14TeVmcRun4RECO')
            rootSources = rootSourcesRelValTTbar_14TeVmcRun4RECO
        elif (leNom == 'rootSourcesRelValTTbar_14TeVmcRun4PU'):
            print('leNom2 : rootSourcesRelValTTbar_14TeVmcRun4PU')
            rootSources = rootSourcesRelValTTbar_14TeVmcRun4PU
        elif (leNom == 'rootSourcesRelValSingleEFlatPt2To100mcRun4RECO'):
            print('leNom2 : rootSourcesRelValSingleEFlatPt2To100mcRun4RECO')
            rootSources = rootSourcesRelValSingleEFlatPt2To100mcRun4RECO
        elif (leNom == 'rootSourcesRelValSingleEFlatPt2To100mcRun4PU'):
            print('leNom2 : rootSourcesRelValSingleEFlatPt2To100mcRun4PU')
            rootSources = rootSourcesRelValSingleEFlatPt2To100mcRun4PU
        elif (leNom == 'rootSourcesRelValZpToEE_m6000_14TeVmcRun3RECO'):
            print('leNom2 : rootSourcesRelValZpToEE_m6000_14TeVmcRun3RECO')
            rootSources = rootSourcesRelValZpToEE_m6000_14TeVmcRun3RECO
        elif (leNom == 'rootSourcesRelValZpToEE_m6000_14TeVmcRun3PU'):
            print('leNom2 : rootSourcesRelValZpToEE_m6000_14TeVmcRun3PU')
            rootSources = rootSourcesRelValZpToEE_m6000_14TeVmcRun3PU
        else:
            print('\nHouston we have a pbm with {:s} !!!'.format(leNom))
            exit()'''
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
            if ((elem[0] == '+') or (elem[0] == '*')):
                tmpSource1.append(elem[1])
                if (elem[0] == '*'):
                    # extract release from source reference
                    input_ref_file = elem[1]
                    release = elem[1].split('__')[2].split('-')[0]
                    print('extracted release : {:s}'.format(release))
        rootFilesList = []
        for elem in tmpSource1:
            #print('elem : {:s}'.format(elem))
            name = pathDATA + '/' + elem
            if exists(name):
                rootFilesList.append(elem)
            else:
                print("{:s} n'existe pas".format(name))
        #print(rootFilesList)

        print('we use the files :')
        for item in rootFilesList:
            tmp_branch = []
            nbHistos = 0
            print('\n%s' % item)
            b = (item.split('__')[2]).split('-')
            rels.append([b[0], b[0][6:], item])
            f_root = ROOT.TFile(pathDATA + item)
            h_rel = gr.getHisto(f_root, tp_1)
            for i in range(0, N_histos): # 1 N_histos histo for debug
                histo_rel = h_rel.Get(branches[i])
                if (histo_rel):
                    d = gr.getHistoConfEntry(histo_rel)
                    s_tmp = gr.fill_Snew2(d, histo_rel)
                    if (s_tmp.min() < 0.):
                        print('pbm whith histo %s, min < 0' % branches[i])
                    elif (np.floor(s_tmp.sum()) == 0.):
                        print('pbm whith histo %s, sum = 0' % branches[i])
                    else:
                        nbHistos += 1
                        tmp_branch.append(branches[i])
                else:
                    print('%s KO' % branches[i])
            nb_ttl_histos.append(nbHistos)
            tmp_branches.append(tmp_branch)

        print('nb_ttl_histos : ', nb_ttl_histos)
        if(len(set(nb_ttl_histos))==1):
            print('All elements are the same with value {:d}.'.format(nb_ttl_histos[0]))
        else:
            print('All elements are not the same.')
            print('nb ttl of histos : ' , nb_ttl_histos)
        newBranches = optimizeBranches(tmp_branches)

        if (len(branches) != len(newBranches)):
            print('len std branches : {:d}'.format(len(branches)))
            print('len new branches : {:d}'.format(len(newBranches)))
            branches = newBranches
            N_histos = len(branches)
        print('N_histos : %d' % N_histos)

        sortedRels = sorted(rels, key = lambda x: x[0]) # gives an array with releases sorted
        # get the "reference" root file datas
        f_KSref = ROOT.TFile(pathDATA + input_ref_file)
        print('we use the %s file as KS reference' % input_ref_file)

        h_KSref = gr.getHisto(f_KSref, tp_1)
        print(h_KSref)

        diffTab = pd.DataFrame()
        print(diffTab)
        toto = []

        for i in range(0, N_histos):#, N_histos-1 range(N_histos - 1, N_histos):  # 1 N_histos histo for debug
            #print('histo : {:s}'.format(branches[i])) # print histo name
            r_rels = []
            
            histo_rel = h_rel.Get(branches[i])
            if (histo_rel):
                print('%s OK' % branches[i])

                # create the datas for the p-Value graph
                # by comparing 1 curve with the others.
                histo_KSref = h_KSref.Get(branches[i])
                s_KSref = []
                for entry in histo_KSref:
                    s_KSref.append(entry)
                s_KSref = np.asarray(s_KSref)
                s_KSref = s_KSref[1:-1]
                print('s_KSref has {:d} elements'.format(len(s_KSref)))

                #print('\nWorking with sorted rels\n')
                ind_rel = 0
                diffValues = []
                for elem in sortedRels:
                    #print(elem)
                    rel = elem[1]
                    file = elem[2]

                    # get the "new" root file datas
                    input_rel_file = file
                    f_rel = ROOT.TFile(pathDATA + input_rel_file)
                    #print('we use the {:s} file as new release '.format(input_rel_file))

                    h_rel = gr.getHisto(f_rel, tp_1)
                    histo_rel = h_rel.Get(branches[i])

                    s_new = []
                    for entry in histo_rel:
                        s_new.append(entry)
                    s_new = np.asarray(s_new)
                    s_new = s_new[1:-1]
                    #print('s_KSref has {:d} elements for {:s}'.format(len(s_KSref), rel))
                    #print('s_new has {:d} elements for {:s}'.format(len(s_new), rel))
                    if (len(s_KSref) != len(s_new)):
                        print('pbm whith histo %s, lengths are not the same' % branches[i])
                        continue

                    if (s_new.min() < 0.):
                        print('pbm whith histo %s, min < 0' % branches[i])
                        continue
                    if (np.floor(s_new.sum()) == 0.):
                        print('pbm whith histo %s, sum = 0' % branches[i])
                        continue
                        
                    # diff max between new & old
                    diffMax0, posMax0, sDKS = DB.diffMAXKS3(s_KSref, s_new)
                    #print("diffMax0 : %f - posMax0 : %f" % (diffMax0, posMax0))
                    #print('ind rel : {:d} : {:s} : {:e}\n'.format(ind_rel, branches[i], diffMax0)) # OK

                    diffValues.append(diffMax0)
                    r_rels.append(str(rel))
                    #print(diffValues)
                    ind_rel += 1
                
                toto.append(diffValues)
                lab = r_rels
                val = diffValues
                print('il y a {:d} points dans les valeurs'.format(len(val)))
                print('il y a {:d} points dans les labels'.format(len(lab)))
                pictureName = webFolder + dataSetFolder + '/pngs/maxDiff_comparison_' + branches[i] + '_1.png' # 
                print(pictureName)
                title = 'KS cum diff values vs releases. ' + branches[i]
                #createCompLossesPicture(lab,val, pictureName, title, 'Releases', 'max diff')
                #pictureName = webFolder + dataSetFolder + '/pngs/maxDiff_comparison_' + branches[i] + '_3.png' # 
                createCompLossesPicture3(lab,val, pictureName, title, 'Releases', 'max diff')
            else:
                print('%s KO' % branches[i])
        diffTab = pd.DataFrame(toto, columns=r_rels)
        globos = diffTab.mean(axis=0, numeric_only=True)
        print(diffTab.shape)

        # generate pictures
        dt = globos.head(50)
        lab = list(dt.index.values)
        val = globos.to_list()
        print(dataSetFolder)
        print(webFolder)
        pictureName = webFolder + dataSetFolder + '/pngs/maxDiff_comparison_values_1.png' # 
        print(pictureName)
        title = r"$\bf{total}$" + ' : KS cum diff values vs releases.'
        createCompLossesPicture(lab,val, pictureName, title, 'Releases', 'max diff')

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

        print('we use the files :')
        for item in rootFilesList2:
            tmp_branch = []
            nbHistos = 0
            print('\n%s' % item)
            b = (item.split('__')[2]).split('-')
            rels2.append([b[0], b[0][6:], item])
            f_root = ROOT.TFile(pathDATA + item)
            h_rel = gr.getHisto(f_root, tp_1)
            for i in range(0, N_histos): # 1 N_histos histo for debug
                histo_rel = h_rel.Get(branches[i])
                if (histo_rel):
                    d = gr.getHistoConfEntry(histo_rel)
                    s_tmp = gr.fill_Snew2(d, histo_rel)
                    if (s_tmp.min() < 0.):
                        print('pbm whith histo %s, min < 0' % branches[i])
                    elif (np.floor(s_tmp.sum()) == 0.):
                        print('pbm whith histo %s, sum = 0' % branches[i])
                    else:
                        nbHistos += 1
                        tmp_branch.append(branches[i])
                else:
                    print('%s KO' % branches[i])
            nb_ttl_histos2.append(nbHistos)
            tmp_branches2.append(tmp_branch)

        print('nb_ttl_histos : ', nb_ttl_histos2)
        if(len(set(nb_ttl_histos))==1):
            print('All elements are the same with value {:d}.'.format(nb_ttl_histos[0]))
        else:
            print('All elements are not the same.')
            print('nb ttl of histos : ' , nb_ttl_histos)
        newBranches2 = optimizeBranches(tmp_branches2)

        if (len(branches) != len(newBranches2)):
            print('len std branches : {:d}'.format(len(branches)))
            print('len new branches : {:d}'.format(len(newBranches2)))
            branches = newBranches2
            N_histos = len(branches)

        print('N_histos : %d' % N_histos)

        sortedRels2 = sorted(rels2, key = lambda x: x[0]) # gives an array with releases sorted
        # get the "reference" root file datas
        f_KSref = ROOT.TFile(pathDATA + input_ref_file)
        print('we use the %s file as KS reference' % input_ref_file)

        h_KSref = gr.getHisto(f_KSref, tp_1)
        print(h_KSref)

        diffTab = pd.DataFrame()
        print(diffTab)
        toto = []

        for i in range(0, N_histos):#, N_histos-1 range(N_histos - 1, N_histos):  # 1 N_histos histo for debug
            #print('histo : {:s}'.format(branches[i])) # print histo name
            r_rels2 = []
            
            histo_rel = h_rel.Get(branches[i])
            if (histo_rel):
                print('%s OK' % branches[i])

                # create the datas for the p-Value graph
                # by comparing 1 curve with the others.
                histo_KSref = h_KSref.Get(branches[i])
                s_KSref = []
                for entry in histo_KSref:
                    s_KSref.append(entry)
                s_KSref = np.asarray(s_KSref)
                s_KSref = s_KSref[1:-1]
                print('s_KSref has {:d} elements'.format(len(s_KSref)))

                #print('\nWorking with sorted rels\n')
                ind_rel = 0
                diffValues = []
                for elem in sortedRels2:
                    #print(elem)
                    rel = elem[1]
                    file = elem[2]

                    # get the "new" root file datas
                    input_rel_file = file
                    f_rel = ROOT.TFile(pathDATA + input_rel_file)
                    #print('we use the {:s} file as new release '.format(input_rel_file))

                    h_rel = gr.getHisto(f_rel, tp_1)
                    histo_rel = h_rel.Get(branches[i])

                    s_new = []
                    for entry in histo_rel:
                        s_new.append(entry)
                    s_new = np.asarray(s_new)
                    s_new = s_new[1:-1]
                    #print('s_KSref has {:d} elements for {:s}'.format(len(s_KSref), rel))
                    #print('s_new has {:d} elements for {:s}'.format(len(s_new), rel))
                    if (len(s_KSref) != len(s_new)):
                        print('pbm whith histo %s, lengths are not the same' % branches[i])
                        continue

                    if (s_new.min() < 0.):
                        print('pbm whith histo %s, min < 0' % branches[i])
                        continue
                    if (np.floor(s_new.sum()) == 0.):
                        print('pbm whith histo %s, sum = 0' % branches[i])
                        continue
                        
                    # diff max between new & old
                    diffMax0, posMax0, sDKS = DB.diffMAXKS3(s_KSref, s_new)
                    #print("diffMax0 : %f - posMax0 : %f" % (diffMax0, posMax0))
                    #print('ind rel : {:d} : {:s} : {:e}\n'.format(ind_rel, branches[i], diffMax0)) # OK

                    diffValues.append(diffMax0)
                    r_rels2.append(str(rel))
                    #print(diffValues)
                    ind_rel += 1
                
                toto.append(diffValues)
                lab = r_rels2
                val = diffValues
                print('il y a {:d} points dans les valeurs'.format(len(val)))
                print('il y a {:d} points dans les labels'.format(len(lab)))
                pictureName = webFolder + dataSetFolder + '/pngs/maxDiff_comparison_' + branches[i] + '_2.png' # 
                print(pictureName)
                title = 'KS cum diff values vs releases. ' + branches[i]
                #createCompLossesPicture(lab,val, pictureName, title, 'Releases', 'max diff')
                createCompLossesPicture3(lab,val, pictureName, title, 'Releases', 'max diff')
            else:
                print('%s KO' % branches[i])
        diffTab = pd.DataFrame(toto, columns=r_rels2)
        globos = diffTab.mean(axis=0, numeric_only=True)

        # generate pictures
        dt = globos.head(50)
        lab = list(dt.index.values)
        val = globos.to_list()
        print(dataSetFolder)
        print(webFolder)
        pictureName = webFolder + dataSetFolder + '/pngs/maxDiff_comparison_values_2.png' # 
        print(pictureName)
        title = r"$\bf{total}$" + ' : KS cum diff values vs releases.'
        createCompLossesPicture(lab,val, pictureName, title, 'Releases', 'max diff')

    toc = time.time()
    print('Done in {:.4f} seconds'.format(toc-tic))

print("Fin !")
