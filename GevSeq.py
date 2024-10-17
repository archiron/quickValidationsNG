#! /usr/bin/env python
#-*-coding: utf-8 -*-

################################################################################
# GevSeqDev: a tool to generate Release Comparison                              
#
# version 3.2 : add png pictures
#                                                                              
# Arnaud Chiron-Turlay LLR - arnaud.chiron@llr.in2p3.fr                         
#                                                                              
################################################################################

import os,sys,shutil
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

#from sys import argv
#argv.append( '-b-' )
import ROOT
ROOT.gROOT.SetBatch(True)
#ROOT.gErrorIgnoreLevel = ROOT.kWarning # remove info like : Info in <TCanvas::Print>: gif file gifs/h_ele_vertexPhi.gif has been created
ROOT.gErrorIgnoreLevel = ROOT.kFatal # ROOT.kBreak # 
ROOT.PyConfig.DisableRootLogon = True
ROOT.PyConfig.IgnoreCommandLineOptions = True
#argv.remove( '-b-' )

root_version = ROOT.gROOT.GetVersion()
print('PYTHON     version : {}'.format(sys.version))
print("ROOT      version : {}".format(root_version))

class GevSeq():
    def __init__(self):
        print('begin to run')
        gr = Graphic()
        gr.initRoot()

        if len(sys.argv) > 1:
            print(sys.argv)
            print("arg. 0 :", sys.argv[0]) # name of the script
            print("arg. 1 :", sys.argv[1][:-3]) # name of the file to be used
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
        print('Validation_reference : %s' % cf2.Validation_reference)
        print('web_repo : %s' % cf2.web_repo)
        print('picture_ext : %s' % cf2.picture_ext)

        sys.path.append(os.getcwd()) # path where you work
        valEnv_d = env_default()
        DB = DecisionBox()
        net = networkFunctions()
        tl = Tools()

        print('working in %s\n' % valEnv_d.workDir() )

        if os.path.exists(valEnv_d.workDir() + '/DATA/'): # True
            print("/DATA/ already created\n")
        else: # False
            os.makedirs(valEnv_d.workDir() + '/DATA/')

        mods = dir(cf2)
        listGeV = []
        for elem in mods:
            if re.search('GeV_', elem):
                listGeV.append(elem)
        print(listGeV)

        #table1=getattr(cf2, listGeV[0])
        print('')

        self.KS_reference_release = KS_reference_release
        if (KS_reference_release != ''):
            print('Kolmogorov-Smirnov reference release to be used if needed : %s' % KS_reference_release)

        print('\nSequential')

        # sequential
        # get time for begin
        start = time.time()           # let's see how long this takes

        for val in listGeV: # loop over GUI configurations
            #print('\n ***** %s ***** \n' % val)
            validation = getattr(cf2, val)
            print('validation : %s' % validation) # temp
            release = validation[0][0]
            reference = validation[0][1]
            print('long rel : %s' % release) # temp
            shortRelease = release[6:] # CMSSW_ removed
            shortReference = reference[6:] # CMSSW_ removed
            print('short rel : %s' % shortRelease) # temp
            releaseExtent = validation[1][0]
            referenceExtent = validation[1][1]
            print('rel extent : %s' % releaseExtent) # temp
            print('ref extent : %s' % referenceExtent) # temp
            choiceT = validation[3]
            print('choiceT : %s' % choiceT) # temp

            print('web repo : %s' % web_repo)
            print('DB Flag : %s' % validation[7])
            relrefVT = validation[4]
            print('relrefVT %s' % relrefVT)
            if (web_repo[1] == 'dev'):
                tmp = valEnv_d.KS_Path()[2] + 'Dev/'
            elif(web_repo[1] == 'test'):
                tmp = valEnv_d.KS_Path()[2] + 'Test/'
            else:
                tmp = valEnv_d.KS_Path()[2] + 'Releases/'
            print('KS_Path : %s' % valEnv_d.KS_Path())
            self.webURL = tmp

            print('config relExtent %s' % releaseExtent)
            print('config refExtent %s' % referenceExtent)
            if ( referenceExtent != '' ):
                webFolder = choiceT + '_' + reference + "_" + referenceExtent
            else:
                webFolder = choiceT + '_' + reference
            if ( releaseExtent != '' ):
                webFolder = shortRelease + "_" + releaseExtent + "_DQM_" + web_repo[1] + '/' + webFolder
            else:
                webFolder = shortRelease + "_DQM_" + web_repo[1] + '/' + webFolder
            self.shortWebFolder = webFolder
            webFolder = web_repo[0] + webFolder + '/'

            if not os.path.exists(webFolder): # only create the first folder for saving gifs, i.e. release folder.
                self.exist_webFolder = False
            else:
                self.exist_webFolder = True

            if self.exist_webFolder: # True
                print("%s already created\n" % str(webFolder))
            else: # False
                os.makedirs(str(webFolder))

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
            if ( N_GT == 2*N):
                print('OK for globalTags : %d' % N_GT)
                print('globalTags : %s' % globalTag)
            else:
                print('PBM with globalTags, N = %d' % N_GT)
            # need to test if there is as rel & ref files as datasets
            N_Files = len(validation[6])
            for it3 in validation[6]:
                if ( it3 == '' ):
                    N_Files -= 1
            print('N_Files : %d' % N_Files)
            relFile = validation[6][0::2] # must be rewritten
            refFile = validation[6][1::2]
            if ( N_Files == 2*N):
                print('OK for nb of files : %d' % N_Files)
                print('rel file : %s' % relFile)
                print('ref file : %s' % refFile)
            else:
                print('PBM with input files, N = %d' % N_Files)
            print('')

            # begin test for GT/files
            nb_coherGT = 0
            if (N_GT > 0):
                for it4 in globalTag:
                    print(it4)
                    if re.search(release, it4):
                        nb_coherGT +=1
                    elif re.search(reference, it4):
                        nb_coherGT +=1
            if (nb_coherGT == N):
                print('OK for GT')
            else:
                print('KO for GT')

            nb_coherFiles = 0
            if (N_Files > 0):
                for it4 in relFile:
                    #print(it4)
                    if re.search(release, it4):
                        nb_coherFiles +=1
                    else:
                        nb_coherFiles -=1
                for it4 in refFile:
                    #print(it4)
                    if re.search(reference, it4):
                        nb_coherFiles +=1
                    else:
                        nb_coherFiles -=1
                #for it4 in relFile: # test with datasets on files
                #    if re.search(datasets[0], it4):
                #        nb_coherFiles +=1
                #    else:
                #        nb_coherFiles -=1
            print('nb_coherFiles : %d' % nb_coherFiles)
            if (nb_coherFiles == 2*N):
                print('OK for files')
            else:
                print('KO for files')

            if ( nb_coherFiles > 0 ):
                print('working with files for %s' % val)
            elif (nb_coherGT > 0 ):
                print('working with GT for %s' % val)

                # get the list for RELEASE
                list_0 = net.list_search_0()
                item_0 = ''
                #print(list_0)
                for item in list_0:
                    it = item[:-1]
                    #print(it, shortRelease)
                    if re.search(it[6:], shortRelease):
                        print('OK pour %s' % item)
                        item_0 = it
                releasesList_1 = net.list_search_1(item_0 + 'x')
                #print('there is %d files for %s' % (len(releasesList_1), item_0))
                # get the list for REFERENCE
                if ( reference != release):
                    item_1 = ''
                    for item in list_0:
                        it = item[:-1]
                        if re.search(it[6:], shortReference):
                            print('OK pour %s' % item)
                            item_1 = it
                    referencesList_1 = net.list_search_1(item_1 + 'x')
                    #print('there is %d files for %s' % (len(referencesList_1), item_0))
                else: # reference == release
                    referencesList_1 = releasesList_1
                    item_1 = item_0

                list_rel = []
                for item in releasesList_1:
                    if re.search(shortRelease, item):
                        list_rel.append(item)
                #print('there is %d release files for %s' % (len(list_rel), release))
                #print(list_rel)
                list_ref = []
                for item in referencesList_1:
                    if re.search(shortReference, item):
                        list_ref.append(item)
                #print('there is %d release files for %s' % (len(list_ref), reference))
                #print(list_ref)

                list_rel2 = [] # get the list of the files for all the datasets for release
                nb_rel2 = [] # get the number of files per dataset
                for item1 in datasets:
                    i = 0
                    for item2 in list_rel:
                        if re.search(item1, item2):
                            #print(item2, item1)
                            list_rel2.append(item2)
                            i += 1
                    nb_rel2.append(i)
                #for item1 in enumerate(list_rel2):
                #    print('[%2d] : %s' %(item1[0], list_rel2[item1[0]]))
                list_ref2 = [] # get the list of the files for all the datasets for reference
                nb_ref2 = [] # get the number of files per dataset
                for item1 in datasets:
                    i = 0
                    for item2 in list_ref:
                        if re.search(item1, item2):
                            #print(item2, item1)
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
                    if (nb_relFiles + nb_refFiles) == nb_coherFiles:
                        print('OK for files loading')
                    else:
                        print('PBM for files loading')
                        print('%d + %d vs %d' % (nb_relFiles, nb_refFiles, nb_coherFiles))
                        exit()
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
                    #print(rel3)
                    #print(ref3)
                    relFile = list(set(rel3)) # rel3, elimine les doublons
                    refFile = list(set(ref3)) # ref3, elimine les doublons
                    relFile = [str(r) for r in relFile] # elimine le u'...'
                    refFile = [str(r) for r in refFile] # elimine le u'...'
                    #print(relFile)
                    #print(refFile)

                # Load files
                os.chdir(valEnv_d.workDir() + '/DATA/')
                print('appel cmd_load_files')
                print('item_0', item_0)
                print('item_1', item_1)
                net.cmd_load_files(relFile, item_0+'x')
                net.cmd_load_files(refFile, item_1+'x')
                os.chdir(valEnv_d.workDir())

            else: # no files & no GT
                print('no GT nor files for %s' % val)
                exit()

            print('')
            os.chdir(webFolder) # going into finalFolder

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

            relFile = []
            refFile = []
            for elem1 in globos:
                #print('globos : %s' % elem1)
                relFile.append(elem1[1])
                refFile.append(elem1[2])

            #stop
            #relFile = ['DQM_V0001_R000000001__RelValZEE_14__CMSSW_12_1_0_pre5-121X_mcRun3_2021_realistic_v15-v1__DQMIO.root']
            #refFile = ['DQM_V0001_R000000001__RelValZEE_14__CMSSW_12_1_0_pre4-121X_mcRun3_2021_realistic_v10-v1__DQMIO.root']

            for i, elt in enumerate(datasets):
                dts = elt
                print('===== dataset : %s' % dts)
                print('Decision Box Flag : %s' % validation[7][i])
                DB_flag = validation[7][i]
                if (KS_reference_release == ''):
                    DB_flag = False # empty KS reference release always implies False
                print('len dataset : %d - len relFile : %d - len refFile : %d' % (len(datasets), len(relFile), len(refFile)))
                print('dataset : %s' % datasets)
                print('relFile : %s' % relFile)
                print('refFile : %s' % refFile)

                dataSetFolder = str(relrefVT[0] + '-' + relrefVT[1] + '_' + dts)
                tl.createDatasetFolder(dataSetFolder, picture_ext) # gifs / pngs
                os.chdir(dataSetFolder) # going to dataSetFolder

                # get config files
                #(it1, it2, tp_1, tp_2) = tl.testForDataSetsFile2(valEnv_d.tmpPath(), relrefVT, dts)
                (it1, it2, tp_1, tp_2) = tl.testForDataSetsFile2(valEnv_d.tmpPath(), relrefVT) # only for DEV !!!
                print("config file for target : %s" % it1)
                print("config file for reference : %s" % it2)
                print("tree path for target : %s" % tp_1)
                print("tree path for reference : %s" % tp_2)
                print('chemin : %s' % os.getcwd())
                print('tmpPath : %s' % valEnv_d.tmpPath())
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
                print('      h1 for dataset : %s' % dts)
                print(h1)

                input_ref_file = valEnv_d.workDir() + '/DATA/' + str(refFile[i])

                if not os.path.isfile(input_ref_file): # the ref root file does not exist
                    print('%s does not exist' % input_ref_file)
                    exit()
                else:
                    print(input_ref_file)

                f_ref = ROOT.TFile(input_ref_file)
                h2 = gr.getHisto(f_ref, tp_2)
                print("CMP_CONFIG = %s\n" % CMP_CONFIG)
                print("input_rel_file = %s\n" % input_rel_file)
                print("input_ref_file = %s\n" % input_ref_file)
                print('      h2 for dataset : %s' % dts)

                if (DB_flag == True):
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
                #stop

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
                for i in range(0, len(titlesList)):
                    for elem in histoArray_0[titlesList[i]]:
                        if ( elem != "endLine" ):

                            short_histo_name, short_histo_names, histo_positions = tl.shortHistoName(elem)
                            #gif_name = "gifs/" + short_histo_names[0] + ".C"
                            gif_name = "gifs/" + short_histo_names[0] + ".gif"
                            picture_name = picture_ext + "/" + short_histo_names[0] + '.' + picture_ext[0:-1]
                            png_name = "pngs/" + short_histo_names[0] + ".png" # for DB yellow curves
                            png_cumul_name = "pngs/" + short_histo_names[0] + "_cum.png" # for DB yellow curves
                            print('\npicture name : {:s}'.format(picture_name))
                            #print('\nshort histo name : {:s}'.format(short_histo_names[0]))

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
                                    print('no histo in {:s} for {:s}'.format(self.KS_reference_release, short_histo_names[0]))
                                    ycFlag = False

                            print('ycFlag : %s : %s' % (short_histo_names[0], ycFlag))
                            gr.PictureChoice(histo_1, histo_2, histo_positions[1], histo_positions[2], picture_name, 0)
                            if ycFlag:
                                tl.createPngDatasetFolder()
                                gr.PictureChoice_DB(histo_1, histo_3, histo_positions[1], histo_positions[2], png_name, 0, yellowCurves)
                                gr.PictureChoice_DB3(histo_1, histo_3, histo_positions[1], histo_positions[2], png_cumul_name, 0, yellowCurvesCum)

                                percentage = 0.05
                                #if ( KS_values_1[4] >= percentage ):
                                if ( KS_values_3[1] >= percentage ):
                                    #color = 'green'
                                    DB_picture = valEnv_d.imageOK()
                                else:
                                    #color = 'red'
                                    DB_picture = valEnv_d.imageKO()
                            if (  histo_positions[3] == "0" ):
                                # insert here the decision box
                                if DB_flag and ycFlag:
                                    KS_V = [KS_values_1, KS_values_2, KS_values_3]
                                    #KS_V = [KS_values_1]
                                    Names = [short_histo_name, gif_name, short_histo_names[0], png_name, png_cumul_name]
                                    DB.DBwebPage(fHisto, Names, KS_V, DB_picture, self.webURL, self.shortWebFolder, dataSetFolder, KS_Path0, KS_Path1, ycFlag, shortRelease, shortReference)
                            else: # line_sp[3]=="1"
                                if DB_flag and ycFlag:
                                    KS_V = [KS_values_1, KS_values_2, KS_values_3]
                                    #KS_V = [KS_values_1]
                                    Names = [short_histo_name, gif_name, short_histo_names[0], png_name, png_cumul_name]
                                    DB.DBwebPage(fHisto, Names, KS_V, DB_picture, self.webURL, self.shortWebFolder, dataSetFolder, KS_Path0, KS_Path1, ycFlag, shortRelease, shortReference)

                            if DB_flag:
                                fHisto.close()

                if DB_flag:
                    DB.generateExplanation()

                os.chdir('../') # back to the final folder.

        # get time for end
        finish = time.time()
        print('total time to execute : %8.4f' % (finish-start)) # python2

        print('end of run')

