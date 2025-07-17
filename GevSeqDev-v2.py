#! /usr/bin/env python
#-*-coding: utf-8 -*-

################################################################################
# GevSeqDev: a tool to generate Release Comparison                              
#
# version 3.2 : add png pictures
# version 3.3 : reduce the print/check part with new functions
#                                                                              
# Arnaud Chiron-Turlay LLR - arnaud.chiron@llr.in2p3.fr                         
#                                                                              
################################################################################

import os
import sys
import re
import shutil
import time
import importlib.machinery
import importlib.util

sys.path.append('../ChiLib_CMS_Validation')

from graphicFunctions import Graphic
from functions import *
from networkFunctions import networkFunctions
from DecisionBox import DecisionBox
from valEnv_default import env_default
from config import * # WARNING, must be the local version and not the remote one !!!

from multiprocessing import Pool

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gErrorIgnoreLevel = ROOT.kFatal # ROOT.kBreak # 
ROOT.PyConfig.DisableRootLogon = True
ROOT.PyConfig.IgnoreCommandLineOptions = True

root_version = ROOT.gROOT.GetVersion()
print('PYTHON     version : {}'.format(sys.version))
print("ROOT      version : {}".format(root_version))

if __name__=="__main__":
    gr = Graphic()
    gr.initRoot()

    tl = Tools()

    if len(sys.argv) > 1:
        tl.p_args(sys.argv)
        extFile = sys.argv[1]
        CompleteExtFile = os.getcwd()+'/'+ extFile
        # Import mymodule
        loader = importlib.machinery.SourceFileLoader( extFile, CompleteExtFile)
        spec = importlib.util.spec_from_loader( extFile, loader )
        cf2 = importlib.util.module_from_spec( spec )
        loader.exec_module( cf2 )
    else:
        print("classical way")
        import config as cf2

    Validation_reference = cf2.Validation_reference
    web_repo = cf2.web_repo
    KS_reference_release = cf2.KS_reference_release
    picture_ext = cf2.picture_ext
    tl.p_cf2(cf2)
    tl.checkPictureExt(picture_ext)

    sys.path.append(os.getcwd()) # path where you work
    valEnv_d = env_default()
    DB = DecisionBox()
    net = networkFunctions()

    tl.createWorkingDir(valEnv_d.workDir() + '/DATA/')

    mods = dir(cf2)
    listGeV = []
    for elem in mods:
        if re.search('GeV_', elem):
            listGeV.append(elem)

    if (KS_reference_release != ''):
        print('Kolmogorov-Smirnov reference release to be used if needed : %s' % KS_reference_release)

    # get time for begin
    start = time.time()           # let's see how long this takes

    for val in listGeV: # loop over GUI configurations
        validation = getattr(cf2, val)
        release = validation[0][0]
        reference = validation[0][1]
        shortRelease = release[6:] # CMSSW_ removed
        shortReference = reference[6:] # CMSSW_ removed
        releaseExtent = validation[1][0]
        referenceExtent = validation[1][1]
        choiceT = validation[3]

        relrefVT = validation[4]
        if (web_repo[1] == 'dev'):
            tmp = valEnv_d.KS_Path()[2] + 'Dev/'
        elif(web_repo[1] == 'test'):
            tmp = valEnv_d.KS_Path()[2] + 'Test/'
        else:
            tmp = valEnv_d.KS_Path()[2] + 'Releases/'
        webURL = tmp

        tl.p_RelRef(validation, release, reference, shortRelease, shortReference, releaseExtent, referenceExtent, choiceT, web_repo, validation[7], relrefVT, valEnv_d.KS_Path())

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

        tl.checkCreateWebFolder(webFolder)

        datasets = validation[2]
        N = len(datasets)
        print('there is %d datasets : %s' % (N, datasets))
        # need to test if there is as rel & ref GT as datasets
        # must have 2 x # of datasets
        globalTag = validation[5]
        N_GT = len(globalTag)
        for it3 in globalTag:
            if ( it3 == '' ):
                N_GT -= 1
        tl.checkN_GT(N_GT, N, globalTag)

        # need to test if there is as rel & ref files as datasets
        N_Files = len(validation[6])
        print('N_Files : {:d}'.format(N_Files))
        for it3 in validation[6]:
            if ( it3 == '' ):
                N_Files -= 1
        relFile = validation[6][0::2] # must be rewritten
        refFile = validation[6][1::2]
        tl.checkN_Files(N_Files, N, relFile, refFile)

        # begin test for GT/files
        nb_coherGT = 0
        if (N_GT > 0):
            for it4 in globalTag:
                print('Global Tag : %s' % it4)
                if re.search(release, it4):
                    nb_coherGT +=1
                elif re.search(reference, it4):
                    nb_coherGT +=1
        tl.checkN_coherGT(nb_coherGT, N)

        nb_coherFiles = 0
        if (N_Files > 0):
            for it4 in relFile:
                if re.search(release, it4):
                    nb_coherFiles +=1
                    print('rel OK')
                else:
                    nb_coherFiles -=1
                    print('rel KO')
            for it4 in refFile:
                if re.search(reference, it4):
                    nb_coherFiles +=1
                    print('ref OK')
                else:
                    nb_coherFiles -=1
                    print('ref KO')
        tl.checkN_coherFiles(nb_coherFiles, N)

        if ( nb_coherFiles > 0 ):
            print('working with files for %s' % val)
        elif (nb_coherGT > 0 ):
            print('working with GT for %s' % val)

            # get the list for RELEASE
            list_0 = net.list_search_0()
            item_0 = ''
            for item in list_0:
                it = item[:-1]
                if re.search(it[6:], shortRelease):
                    print('OK pour %s' % item)
                    item_0 = it
            releasesList_1 = net.list_search_1(item_0 + 'x')
            # get the list for REFERENCE
            if ( reference != release):
                item_1 = ''
                for item in list_0:
                    it = item[:-1]
                    if re.search(it[6:], shortReference):
                        print('OK pour %s' % item)
                        item_1 = it
                referencesList_1 = net.list_search_1(item_1 + 'x')
            else: # reference == release
                referencesList_1 = releasesList_1
                item_1 = item_0

            list_rel = []
            for item in releasesList_1:
                if re.search(shortRelease, item):
                    list_rel.append(item)
            list_ref = []
            for item in referencesList_1:
                if re.search(shortReference, item):
                    list_ref.append(item)
            #tl.p_listRelRef(list_rel, list_ref, release, reference)

            list_rel2 = [] # get the list of the files for all the datasets for release
            nb_rel2 = [] # get the number of files per dataset
            for item1 in datasets:
                i = 0
                for item2 in list_rel:
                    if re.search(item1, item2):
                        list_rel2.append(item2)
                        i += 1
                nb_rel2.append(i)
            list_ref2 = [] # get the list of the files for all the datasets for reference
            nb_ref2 = [] # get the number of files per dataset
            for item1 in datasets:
                i = 0
                for item2 in list_ref:
                    if re.search(item1, item2):
                        list_ref2.append(item2)
                        i += 1
                nb_ref2.append(i)

            if ( nb_coherFiles > 0 ):
                print('working with files for %s' % val)
                # compare the files to load with the list, to be OK
                nb_relFiles = 0
                nb_refFiles = 0
                for item1 in list_rel2:
                    for item2 in relFile:
                        if item1 == item2 :
                            nb_relFiles += 1
                for item1 in list_ref2:
                    for item2 in refFile:
                        if item1 == item2 :
                            nb_refFiles += 1
                tl.checkN_RelRefcoherFiles(nb_coherFiles, nb_relFiles, nb_refFiles)
            elif (nb_coherGT > 0 ):
                print('working with GT for %s' % val)
                # extract files which correspond to GT
                # first extract rel/ref GT
                relGT = globalTag[0::2]
                refGT = globalTag[1::2]
                rel3 = []
                ref3 = []
                for item1 in list_rel2:
                    for item2 in relGT:
                        if re.search(item2, item1):
                            rel3.append(item1)
                for item1 in list_ref2:
                    for item2 in refGT:
                        if re.search(item2, item1):
                            ref3.append(item1)
                relFile = list(set(rel3)) # rel3, elimine les doublons
                refFile = list(set(ref3)) # ref3, elimine les doublons
                relFile = [str(r) for r in relFile] # elimine le u'...'
                refFile = [str(r) for r in refFile] # elimine le u'...'
                #tl.p_listRelRefGT(relFile, refFile, release, reference)

            # Load files
            os.chdir(valEnv_d.workDir() + '/DATA/')
            tl.p_Items(item_0, item_1)
            net.cmd_load_files(relFile, item_0+'x')
            net.cmd_load_files(refFile, item_1+'x')
            os.chdir(valEnv_d.workDir())

        else: # no files & no GT
            print('no GT nor files for %s' % val)
            exit()

        print('')
        os.chdir(webFolder) # going into finalFolder

        print(relFile)
        print(refFile)
        globos = [] # summary of datasets relFile & refFile
        for elem1 in datasets:
            toto = []
            toto.append(elem1)
            for elem2 in relFile:
                if re.search(elem1, elem2):
                    toto.append(elem2)
            for elem2 in refFile:
                if re.search(elem1, elem2):
                    toto.append(elem2)
            globos.append(toto)
        print(globos)

        relFile = []
        refFile = []
        for elem1 in globos:
            print(elem1)
            relFile.append(elem1[1])
            refFile.append(elem1[2])

        #relFile = ['DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0_pre7-140X_mcRun3_2024_realistic_v21_STD_RegeneratedGS_2024_noPU-v1__DQMIO.root', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_1_0_pre7-140X_mcRun3_2024_realistic_v21_STD_RegeneratedGS_2024_noPU-v1__DQMIO.root', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0_pre7-140X_mcRun3_2024_realistic_v21_STD_2024_PU-v1__DQMIO.root', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_1_0_pre7-140X_mcRun3_2024_realistic_v21_STD_2024_PU-v1__DQMIO.root']
        #refFile = ['DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0_pre5-140X_mcRun3_2024_realistic_v11_STD_2024_noPU-v1__DQMIO.root', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_1_0_pre5-140X_mcRun3_2024_realistic_v11_STD_2024_noPU-v1__DQMIO.root', 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_14_1_0_pre5-PU_140X_mcRun3_2024_realistic_v11_STD_2024_PU-v1__DQMIO.root', 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_14_1_0_pre5-PU_140X_mcRun3_2024_realistic_v11_STD_2024_PU-v1__DQMIO.root']

        for i, elt in enumerate(datasets):
            dts = elt
            print('===== dataset : %s' % dts)
            print('Decision Box Flag : %s' % validation[7][i])
            DB_flag = validation[7][i]
            if (KS_reference_release == ''):
                DB_flag = False # empty KS reference release always implies False
            #tl.p_listRelRef(relFile, refFile, release, reference)

            dataSetFolder = str(relrefVT[0] + '-' + relrefVT[1] + '_' + dts)
            if (relrefVT[2] != ''):
                dataSetFolder = str(relrefVT[2] + '-') + dataSetFolder
            tl.createDatasetFolder(dataSetFolder, picture_ext) # gifs / pngs
            os.chdir(dataSetFolder) # going to dataSetFolder

            # get config files
            (it1, it2, tp_1, tp_2) = tl.testForDataSetsFile2(valEnv_d.tmpPath(), relrefVT)
            tl.p_valPaths(it1, it2, tp_1, tp_2, os.getcwd(), valEnv_d.tmpPath())
            shutil.copy2(it1, 'config_target.txt')
            shutil.copy2(it2, 'config_reference.txt')

            # create gifs pictures & web page
            CMP_CONFIG = 'config_target.txt'
            CMP_TITLE = 'gedGsfElectrons ' + dts

            f = open(CMP_CONFIG, 'r')
            input_rel_file = valEnv_d.workDir() + '/DATA/' + str(relFile[i])

            if not os.path.isfile(input_rel_file): # the rel root file does not exist
                print('%s does not exist' % input_rel_file)
                exit()
            else:
                print(input_rel_file)

            f_rel = ROOT.TFile(input_rel_file)
            h1 = gr.getHisto(f_rel, tp_1)

            input_ref_file = valEnv_d.workDir() + '/DATA/' + str(refFile[i])

            if not os.path.isfile(input_ref_file): # the ref root file does not exist
                print('%s does not exist' % input_ref_file)
                exit()
            else:
                print(input_ref_file)

            f_ref = ROOT.TFile(input_ref_file)
            h2 = gr.getHisto(f_ref, tp_2)
            print("CMP_CONFIG = %s\n" % CMP_CONFIG)
            tl.p_inputRelRefFiles(input_rel_file, input_ref_file)

            if DB_flag:
                tl.createDBoxDatasetFolder() # create DBox folder
                print('DB_flag = True')
                f_KS_file = valEnv_d.workDir() + '/DATA/' + str(KS_reference_ROOT_File)
                f_KS = ROOT.TFile(f_KS_file)
                h3 = gr.getHisto(f_KS, tp_1)
            else:
                tl.deleteDBoxDatasetFolder()  # delete DBox folder
            
            datas = []
            datas.append(CMP_TITLE) # LINE 7
            datas.append(relrefVT[0])
            datas.append(shortRelease)
            datas.append(str(relFile[i])) # LINE 8
            datas.append(relrefVT[1])
            datas.append(shortReference)
            datas.append(str(refFile[i])) # LINE 9
            if (f_ref == 0):
                datas.append(release)
                datas.append(release)
            else:
                datas.append(release)
                datas.append(reference)
            if (Validation_reference != ""):
                datas.append(Validation_reference)
            else:
                datas.append('none')
            datas.append(CMP_CONFIG)
            tl.createDefinitionsFile(datas, '')

            # remplissage tableau titres et dict
            histoArray_0 = {}
            titlesList = [] # needed with python < 3.7. dict does not keep the correct order of the datasets histograms
            key = ""
            tmp = []
            for line in f:
                if ( len(line) == 1 ): # len == 0, empty line
                    if ( ( len(key) != 0 ) and ( len(tmp) != 0) ):
                        histoArray_0[key] = tmp
                        key = ""
                        tmp = []
                else: # len <> 0
                    if ( len(key) == 0 ):
                        key = line # get title
                        titlesList.append(line)
                    else:
                        tmp.append(line) # histo name
                        t1 = line.split("/")
                        t2 = str(t1[1])
                        short_positions = t2.split()
                        if ( short_positions[3] == '1' ): # be careful it is '1' and not 1 (without quote)
                            tmp.append("endLine")

            # fin remplissage tableau titres et dict
            f.close()

            # ecriture des histos
            '''for i in range(0, len(titlesList)):
                for elem in histoArray_0[titlesList[i]]:
                    if ( elem != "endLine" ):
                        short_histo_name, short_histo_names, histo_positions = tl.shortHistoName(elem)
                        gif_name = "gifs/" + short_histo_names[0] + ".gif"
                        picture_name = picture_ext + "/" + short_histo_names[0] + '.' + picture_ext[0:-1]
                        png_name = "pngs/" + short_histo_names[0] + ".png" # for DB yellow curves
                        png_cumul_name = "pngs/" + short_histo_names[0] + "_cum.png" # for DB yellow curves
                        #print('\npicture name : {:s}'.format(picture_name))
                        print('{:s} : [{:s}, {:s}] - {:s}/{:s}'.format(val, relrefVT[0], relrefVT[1], dts, short_histo_name))

                        # creating shortHistoName file in DBox folder
                        if DB_flag:
                            fHisto = open('DBox/' + short_histo_name + '.txt', 'w') # web page
                            fHisto.write('<table border="1" bordercolor=green cellpadding="2" style="margin-left:auto;margin-right:auto">' + '\n')

                        histo_1 = h1.Get(short_histo_names[0]) #
                        histo_2 = h2.Get(short_histo_names[0]) #

                        ycFlag = False
                        if DB_flag:
                            try:
                                histo_3 = h3.Get(short_histo_names[0]) # KS reference
                                KS_Path1 = valEnv_d.KS_Path()[1] + KS_reference_release
                                KS_Path0 = valEnv_d.KS_Path()[0] + KS_reference_release
                                KS_values_1 = DB.decisionBox1(short_histo_names[0], histo_1, histo_3, KS_Path0, shortRelease, shortReference)
                                KS_values_2 = DB.decisionBox2(short_histo_names[0], histo_1, histo_3, KS_Path0, shortRelease, shortReference)
                                KS_values_3 = DB.decisionBox3(short_histo_names[0], histo_1, histo_3, KS_Path0, shortRelease, shortReference)
                                #DB.decB(short_histo_names[0], histo_1, histo_3, KS_Path0, shortRelease)
                                
                                if (len(KS_values_1) > 5):
                                    yellowCurves = [ KS_values_1[5] ]
                                    yellowCurvesCum = [ KS_values_1[6] ]
                                    ycFlag = True
                            except:
                                print('no histo in {:s} for {:s}'.format(KS_reference_release, short_histo_names[0]))
                                ycFlag = False

                        #print('ycFlag : %s : %s' % (short_histo_names[0], ycFlag))
                        gr.initRootStyle()
                        gr.PictureChoice(histo_1, histo_2, histo_positions[1], histo_positions[2], picture_name, 0)
                        if ycFlag:
                            tl.createPngDatasetFolder()
                            gr.PictureChoice_DB(histo_1, histo_3, histo_positions[1], histo_positions[2], png_name, 0, yellowCurves)
                            gr.PictureChoice_DB3(histo_1, histo_3, histo_positions[1], histo_positions[2], png_cumul_name, 0, yellowCurvesCum)

                            percentage = 0.05
                            if ( KS_values_3[1] >= percentage ):
                                DB_picture = valEnv_d.imageOK()
                            else:
                                DB_picture = valEnv_d.imageKO()
                        if (  histo_positions[3] == "0" ):
                            # insert here the decision box
                            if DB_flag and ycFlag:
                                KS_V = [KS_values_1, KS_values_2, KS_values_3]
                                Names = [short_histo_name, gif_name, short_histo_names[0], png_name, png_cumul_name]
                                DB.DBwebPage(fHisto, Names, KS_V, DB_picture, webURL, shortWebFolder, dataSetFolder, KS_Path0, KS_Path1, ycFlag, shortRelease, shortReference)
                        else: # line_sp[3]=="1"
                            if DB_flag and ycFlag:
                                KS_V = [KS_values_1, KS_values_2, KS_values_3]
                                Names = [short_histo_name, gif_name, short_histo_names[0], png_name, png_cumul_name]
                                DB.DBwebPage(fHisto, Names, KS_V, DB_picture, webURL, shortWebFolder, dataSetFolder, KS_Path0, KS_Path1, ycFlag, shortRelease, shortReference)

                        if DB_flag:
                            fHisto.close()'''
            
            def process_histo(tt_histos):
                t_histos, input_rel_file, tp_1, input_ref_file, tp_2 = tt_histos
                f_rel = ROOT.TFile(input_rel_file)
                h_1 = gr.getHisto(f_rel, tp_1)

                f_ref = ROOT.TFile(input_ref_file)
                h_2 = gr.getHisto(f_ref, tp_2)
                for elem in t_histos:
                    if ( elem != "endLine" ):
                        #print(elem)
                        short_histo_name, short_histo_names, histo_positions = tl.shortHistoName(elem)
                        gif_name = "gifs/" + short_histo_names[0] + ".gif"
                        picture_name = picture_ext + "/" + short_histo_names[0] + '.' + picture_ext[0:-1]
                        png_name = "pngs/" + short_histo_names[0] + ".png" # for DB yellow curves
                        png_cumul_name = "pngs/" + short_histo_names[0] + "_cum.png" # for DB yellow curves
                        print('== {:s} : [{:s}, {:s}] - {:s}/{:s}'.format(val, relrefVT[0], relrefVT[1], dts, short_histo_name))

                        # creating shortHistoName file in DBox folder
                        if DB_flag:
                            fHisto = open('DBox/' + short_histo_name + '.txt', 'w') # web page
                            fHisto.write('<table border="1" bordercolor=green cellpadding="2" style="margin-left:auto;margin-right:auto">' + '\n')

                        histo_1 = h_1.Get(short_histo_names[0]) #
                        histo_2 = h_2.Get(short_histo_names[0]) #
                        ycFlag = False
                        if DB_flag:
                            try:
                                histo_3 = h3.Get(short_histo_names[0]) # KS reference
                                KS_Path1 = valEnv_d.KS_Path()[1] + KS_reference_release
                                KS_Path0 = valEnv_d.KS_Path()[0] + KS_reference_release
                                KS_values_1 = DB.decisionBox1(short_histo_names[0], histo_1, histo_3, KS_Path0, shortRelease, shortReference)
                                KS_values_2 = DB.decisionBox2(short_histo_names[0], histo_1, histo_3, KS_Path0, shortRelease, shortReference)
                                KS_values_3 = DB.decisionBox3(short_histo_names[0], histo_1, histo_3, KS_Path0, shortRelease, shortReference)
                                
                                if (len(KS_values_1) > 5):
                                    yellowCurves = [ KS_values_1[5] ]
                                    yellowCurvesCum = [ KS_values_1[6] ]
                                    ycFlag = True
                            except:
                                print('no histo in {:s} for {:s}'.format(KS_reference_release, short_histo_names[0]))
                                ycFlag = False

                        gr.initRootStyle()
                        gr.PictureChoice(histo_1, histo_2, histo_positions[1], histo_positions[2], picture_name, 0)
                        if ycFlag:
                            tl.createPngDatasetFolder()
                            gr.PictureChoice_DB(histo_1, histo_3, histo_positions[1], histo_positions[2], png_name, 0, yellowCurves)
                            gr.PictureChoice_DB3(histo_1, histo_3, histo_positions[1], histo_positions[2], png_cumul_name, 0, yellowCurvesCum)

                            percentage = 0.05
                            if ( KS_values_3[1] >= percentage ):
                                DB_picture = valEnv_d.imageOK()
                            else:
                                DB_picture = valEnv_d.imageKO()
                        if (  histo_positions[3] == "0" ):
                            # insert here the decision box
                            if DB_flag and ycFlag:
                                KS_V = [KS_values_1, KS_values_2, KS_values_3]
                                Names = [short_histo_name, gif_name, short_histo_names[0], png_name, png_cumul_name]
                                DB.DBwebPage(fHisto, Names, KS_V, DB_picture, webURL, shortWebFolder, dataSetFolder, KS_Path0, KS_Path1, ycFlag, shortRelease, shortReference)
                        else: # line_sp[3]=="1"
                            if DB_flag and ycFlag:
                                KS_V = [KS_values_1, KS_values_2, KS_values_3]
                                Names = [short_histo_name, gif_name, short_histo_names[0], png_name, png_cumul_name]
                                DB.DBwebPage(fHisto, Names, KS_V, DB_picture, webURL, shortWebFolder, dataSetFolder, KS_Path0, KS_Path1, ycFlag, shortRelease, shortReference)

                        if DB_flag:
                            fHisto.close()
                return

            with Pool(processes=4) as pool:
                args = [ (histoArray_0[ titlesList[i_pool] ], input_rel_file, tp_1, input_ref_file, tp_2) for i_pool in range(len(titlesList))]
                pool.map(process_histo, args)
            '''args = [ (histoArray_0[ titlesList[i_pool] ], input_rel_file, tp_1, input_ref_file, tp_2) for i_pool in range(len(titlesList))]
            with ProcessPoolExecutor() as executor:
                    executor.map(process_histo, args)'''

            if DB_flag:
                DB.generateExplanation()

            os.chdir('../') # back to the final folder.

    # get time for end
    finish = time.time()
    print('total time to execute : %8.4f' % (finish-start))

    print('end of run')

