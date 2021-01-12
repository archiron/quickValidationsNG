#! /usr/bin/env python
#-*-coding: utf-8 -*-

import os,sys,subprocess,shutil
import concurrent.futures
import time
import numpy as np

#sys.path.append('/afs/cern.ch/user/a/archiron/lbin/ChiLib')
sys.path.append('/eos/project-c/cmsweb/www/egamma/validation/Electrons/ChiLib/')

from graphicFunctions import *
from functions import *
from networkFunctions import list_search_0, list_search_1, cmd_load_files
from DecisionBox import *
from valEnv_default import env_default
from config import * # WARNING, must be the local version and not the remote one !!!

class GevSeq():
    def __init__(self):
        print('begin to run')
        initRoot()

        sys.path.append(os.getcwd()) # path where you work
        import config as cf2
        valEnv_d = env_default()
        DB = DecisionBox()

        print('working in %s\n' % valEnv_d.workDir() )

        if os.path.exists(valEnv_d.workDir() + '/DATA/'): # True
            print("/DATA/ already created\n")
        else: # False
            os.makedirs(valEnv_d.workDir() + '/DATA/')

        mods = dir(cf2)
        listGeV = []
        for elem in mods:
            print(elem) # temp
            if re.search('GeV_', elem):
                listGeV.append(elem)
                print('== %s' % elem) # temp
        print(listGeV)

        table1=getattr(cf2, listGeV[0])
        print('personalization 1') # temp
        print(table1) # temp
        print('')

        print('\nSequential')

        # sequential
        # get time for begin
        start = time.time()           # let's see how long this takes

        for val in listGeV: # loop over GUI configurations
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
            print('KS_Path : %s' % valEnv_d.KS_Path())

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
            webFolder = web_repo[0] + webFolder + '/'
            #print('webFolder : %s' % webFolder)

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
                    print(it4)
                    if re.search(release, it4):
                        nb_coherFiles +=1
                    else:
                        nb_coherFiles -=1
                for it4 in refFile:
                    print(it4)
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
            else: # no files & no GT
                print('no GT nor files for %s' % val)
                exit()

            # get the list for RELEASE
            list_0 = list_search_0()
            item_0 = ''
            #print(list_0)
            for item in list_0:
                it = item[:-1]
                #print(it, shortRelease)
                if re.search(it[6:], shortRelease):
                    print('OK pour %s' % item)
                    item_0 = it
            releasesList_1 = list_search_1(item_0 + 'x')
            #print('there is %d files for %s' % (len(releasesList_1), item_0))
            # get the list for REFERENCE
            if ( reference != release):
                item_0 = ''
                for item in list_0:
                    it = item[:-1]
                    if re.search(it[6:], shortReference):
                        print('OK pour %s' % item)
                        item_0 = it
                referencesList_1 = list_search_1(item_0 + 'x')
                #print('there is %d files for %s' % (len(referencesList_1), item_0))
            else: # reference == release
                referencesList_1 = releasesList_1

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
            #for item1 in enumerate(list_ref2):
            #    print('[%2d] : %s' %(item1[0], list_ref2[item1[0]]))

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

            # create new list from rel_files& ref_files
            rel_ref = [] # not used in sequential line
            for i in range(0, N):
                rel_ref.append([relFile[i], refFile[i]])

            # Load files
            os.chdir(valEnv_d.workDir() + '/DATA/')
            cmd_load_files(relFile, item_0+'x')
            cmd_load_files(refFile, item_0+'x')
            os.chdir(valEnv_d.workDir())

            print('')
            os.chdir(webFolder) # going into finalFolder

            # sort datasets & files
            datasets.sort()
            relFile.sort()
            refFile.sort()

            for i, elt in enumerate(datasets):
                dts = elt
                print('===== dataset : %s' % dts)
                print('Decision Box Flag : %s' % validation[7][i])
                DB_flag = validation[7][i]
                print('len dataset : %d - len relFile : %d - len refFile : %d' % (len(datasets), len(relFile), len(refFile)))
                print('dataset : %s' % datasets)
                print('relFile : %s' % relFile)
                print('refFile : %s' % refFile)
                #stop

                dataSetFolder = str(relrefVT[0] + '-' + relrefVT[1] + '_' + dts)
                createDatasetFolder(dataSetFolder)
                os.chdir(dataSetFolder) # going to dataSetFolder

                # get config files
                #it1 = valEnv_d.workDir() + 'ElectronMcSignalHistos.txt' # valEnv.tmpPath() +
                it1 = valEnv_d.tmpPath() + 'ElectronMcSignalHistos.txt'
                it2 = it1
                tp_1 = 'ElectronMcSignalValidator'
                tp_2 = 'ElectronMcSignalValidator'

                (it1, it2, tp_1, tp_2) = self.testForDataSetsFile(valEnv_d.tmpPath(), relrefVT, dts)
                print("config file for target : %s" % it1)
                print("config file for reference : %s" % it2)
                print("tree path for target : %s" % tp_1)
                print("tree path for reference : %s" % tp_2)
                shutil.copy2(it1, 'config_target.txt')
                shutil.copy2(it2, 'config_reference.txt')

                # create gifs pictures & web page
                CMP_CONFIG = 'config_target.txt'
                CMP_TITLE = 'gedGsfElectrons ' + dts

                f = open(CMP_CONFIG, 'r')
                #input_rel_file = workDir + '/DATA/' + str(valEnv.relFile()[i])
                input_rel_file = valEnv_d.workDir() + '/DATA/' + str(relFile[i])

                if not os.path.isfile(input_rel_file): # the rel root file does not exist
                    print('%s does not exist' % input_rel_file)
                    exit()
                else:
                    print(input_rel_file)

                f_rel = ROOT.TFile(input_rel_file)
                h1 = getHisto(f_rel, tp_1)
                print('      h1 for dataset : %s' % dts)
                print(h1)

                input_ref_file = valEnv_d.workDir() + '/DATA/' + str(refFile[i])

                if not os.path.isfile(input_ref_file): # the ref root file does not exist
                    print('%s does not exist' % input_ref_file)
                    exit()
                else:
                    print(input_ref_file)

                f_ref = ROOT.TFile(input_ref_file)
                h2 = getHisto(f_ref, tp_2)
                print("CMP_CONFIG = %s\n" % CMP_CONFIG)
                print("input_rel_file = %s\n" % input_rel_file)
                print("input_ref_file = %s\n" % input_ref_file)
                print('      h2 for dataset : %s' % dts)

                #wp = open('index.html', 'w') # web page
                wp_Files = []
                wp_index = open('index.html', 'w') # web page
                wp_Files.append(wp_index)
                if (DB_flag == True):
                    wp_DB = open('DB_quick_index.html', 'w') # web page for Decision Box
                    wp_Files.append(wp_DB)
                    createDatasetFolder3() # create DBox folder
                    print('DB_flag = True')
                #stop
                extWrite("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 3.2 Final//EN\">\n", wp_Files)
                extWrite("<html>\n", wp_Files)
                extWrite("<head>\n", wp_Files)
                extWrite("<meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\" />\n", wp_Files)
                extWrite("<title> " + CMP_TITLE + " </title>\n", wp_Files) #option -t dans OvalFile
                extWrite("</head>\n", wp_Files)
                extWrite("<a NAME=\"TOP\"></a>", wp_Files)
                extWrite("<h1><a href=\"../\"><img border=0 width=\"22\" height=\"22\" src=\"../../../../img/up.gif\" alt=\"Up\"/></a>&nbsp; " + CMP_TITLE + " </h1>\n" , wp_Files) # option -t dans OvalFile

                extWrite("<b><font color='red'> " + relrefVT[0] + " " + shortRelease + " </font></b>", wp_Files)
                extWrite(" : " + str(relFile[i]) , wp_Files)
                extWrite("<br>\n", wp_Files)
                extWrite("<b><font color='blue'> " + relrefVT[1] + " " + shortReference + " </font></b>", wp_Files)
                extWrite(" : " + str(refFile[i]) , wp_Files)
                extWrite("<br>\n", wp_Files)

                if (f_ref == 0):
                    extWrite("<p>In all plots below, there was no reference histograms to compare with", wp_Files)
                    extWrite(", and the " + release + " histograms are in red.", wp_Files) # new release red in OvalFile
                else:
                    extWrite("<p>In all plots below", wp_Files)
                    extWrite(", the <b><font color='red'> " + release + " </font></b> histograms are in red", wp_Files) # new release red in OvalFile
                    extWrite(", and the <b><font color='blue'> " + reference + " </font></b> histograms are in blue.", wp_Files) # ref release blue in OvalFile
                extWrite(" Some more details", wp_Files) #
                extWrite(", <a href=\"" + CMP_CONFIG + "\">specification</a> of histograms", wp_Files) # .txt file
                extWrite(", <a href=\"gifs/\">images</a> of histograms" + "." , wp_Files) #
                extWrite("</p>\n", wp_Files)

                # remplissage tableau titres et dict
                histoArray_0 = {}
                titlesList = [] # need with python < 3.7. dict does not keep the correct order of the datasets histograms
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
                extWrite( "<table border=\"1\" cellpadding=\"5\" width=\"100%\">" , wp_Files)

                # ecriture du tableau general
                firstFlag= True
                for i in range(0, len(titlesList)):
                    if ( i % 5  == 0 ):
                        extWrite( "\n<tr valign=\"top\">" , wp_Files)
                    textToWrite = ""
                    extWrite( "\n<td width=\"10\">\n<b> " + titlesList[i] + "</b>" , wp_Files)
                    titles = titlesList[i].split() # explode(" ", $clefs[$i])
                    if len(titles) > 1 :
                        titleShortName = titles[0] + "_" + titles[1]
                    else:
                        titleShortName = titles[0]
                    extWrite( "&nbsp;&nbsp;" + "<a href=\"#" + titleShortName + "\">" , wp_Files) # write group title
                    extWrite( "<img width=\"18\" height=\"15\" border=\"0\" align=\"center\" src=" + valEnv_d.imagePoint() + " alt=\"Top\"/>" + "<br><br>" , wp_Files)
                    textToWrite += "</a>"
                    histoPrevious = ""
                    numLine = 0

                    for elem in histoArray_0[titlesList[i]]:
                        otherTextToWrite = ""

                        if ( elem == "endLine" ):
                            otherTextToWrite += "<br>"
                        else: # no endLine
                            short_histo_name, short_histo_names, histo_positions = shortHistoName(elem)
                            #print('histo positions : ', histo_positions)
                            #stop
                            [after, before, common] = testExtension(short_histo_name, histoPrevious)

                            if ( histo_positions[3] == "0" ):
                                if ( numLine == 0 ):
                                    otherTextToWrite += "<a href=\"#" + short_histo_name + "\"><font color=\'green\'>" + short_histo_name + "</font></a>" + "&nbsp;\n"
                                    common = short_histo_name
                                    numLine += 1
                                else: # $numLine > 0
                                    if ( after == "" ):
                                        otherTextToWrite += "<a href=\"#" + short_histo_name + "\"><font color=green>" + before + "</font></a>" + "&nbsp;\n"
                                    else: # $after != ""
                                        otherTextToWrite += "<a href=\"#" + short_histo_name + "\"><font color=green>" + after + "</font></a>" + "&nbsp;\n"
                                    common = before
                            else: # histo_positions[3] == "1"
                                if ( numLine == 0 ):
                                    otherTextToWrite += "<a href=\"#" + short_histo_name + "\"><font color=grey>" + short_histo_name + "</font></a>" + "&nbsp;\n"
                                    common = short_histo_name
                                else: # $numLine > 0
                                    if ( after == "" ):
                                        otherTextToWrite += "<a href=\"#" + short_histo_name + "\"><font color=blue>" + before + "</font></a>" + "&nbsp;\n"
                                    else: # after != ""
                                        otherTextToWrite += "<a href=\"#" + short_histo_name + "\"><font color=blue>" + after + "</font></a>" + "&nbsp;\n"
                                numLine = 0

                            histoPrevious = common
                            if ( histo_positions[4] == "1" ):
                                otherTextToWrite += "<br>"
                            otherTextToWrite = otherTextToWrite.replace("<br><br>", "<br>")
                        textToWrite += otherTextToWrite
                    textReplace = True
                    while textReplace :
                        textToWrite = textToWrite.replace("<br><br>", "<br>")
                        if ( textToWrite.count('<br><br>') >= 1 ):
                            textReplace = True
                        else:
                            textReplace = False
                    if ( textToWrite.count("</a><br><a") >= 1 ):
                        textToWrite = textToWrite.replace("</a><br><a", "</a><a")
                    extWrite( textToWrite , wp_Files)

                    # fin ecriture du tableau general
                    extWrite( "</td>" , wp_Files)
                    if ( i % 5 == 4 ):
                        extWrite( "</tr>" , wp_Files)
                        firstFlag = False
                    else:
                        firstFlag = True

                if firstFlag:
                    extWrite( "</tr>" , wp_Files)
                extWrite( "</table>\n" , wp_Files)
                extWrite( "<br>" , wp_Files)

                lineFlag = True
                extWrite( "<table border=\"0\" cellpadding=\"5\" width=\"100%\">" , wp_Files)
                # ecriture des histos
                for i in range(0, len(titlesList)):
                    extWrite( "\n<tr valign=\"top\">" , wp_Files)
                    extWrite( "\n<td><a href=\"#TOP\"><img width=\"18\" height=\"18\" border=\"0\" align=\"middle\" src=" + valEnv_d.imageUp() + " alt=\"Top\"/></a></td>\n" , wp_Files)
                    titles = titlesList[i].split()
                    if len(titles) > 1 :
                        titleShortName = titles[0] + "_" + titles[1]
                    else:
                        titleShortName = titles[0]
                    extWrite( "\n<td>\n<b> ", wp_Files )
                    extWrite( "<a id=\"" + titleShortName + "\" name=\"" + titleShortName + "\"></a>" , wp_Files)
                    extWrite( titlesList[i] + "</b></td>" , wp_Files)
                    extWrite( "</tr>", wp_Files)
                    for elem in histoArray_0[titlesList[i]]:
                        if ( elem != "endLine" ):
                            if ( lineFlag ):
                                extWrite( "\n<tr valign=\"top1\">" , wp_Files)

                            short_histo_name, short_histo_names, histo_positions = shortHistoName(elem)
                            gif_name = "gifs/" + short_histo_names[0] + ".gif"
                            png_name = "pngs/" + short_histo_names[0] + ".png" # for DB yellow curves
                            png_cumul_name = "pngs/" + short_histo_names[0] + "_cum.png" # for DB yellow curves

                            # creating shortHistoName file in DBox folder
                            fHisto = open('DBox/' + short_histo_name + '.txt', 'w') # web page
                            fHisto.write('<table border="1" bordercolor=green cellpadding="2" style="margin-left:auto;margin-right:auto">' + '\n')

                            #print('%s/%s' % (elt, short_histo_names[0]))
                            if checkRecompInName(short_histo_names[0]): #
                                histo_name_recomp = short_histo_names[0].replace("_recomp", "") # without recomp
                                #short_histo_names[0] = histo_name_recomp
                                gif_name = "gifs/" + histo_name_recomp + "_recomp.gif"
                                png_name = "pngs/" + histo_name_recomp + "_recomp.png" # for DB yellow curves
                                png_cumul_name = "pngs/" + histo_name_recomp + "_cum__recomp.png" # for DB yellow curves
                                histo_1 = h2.Get(short_histo_names[0]) # with recomp
                                histo_2 = h1.Get(histo_name_recomp) # without recomp
                                c_recomp = 1
                            else: # without recomp
                                histo_1 = h1.Get(short_histo_names[0]) # without recomp
                                histo_2 = h2.Get(short_histo_names[0]) # without recomp
                                c_recomp = 0

                            ycFlag = False
                            if DB_flag:
                                KS_values_1 = DB.decisionBox(short_histo_names[0], histo_1, histo_2)
                                KS_values_2 = DB.decisionBox2(short_histo_names[0], histo_1, histo_2)
                                KS_values_3 = DB.decisionBox3(short_histo_names[0], histo_1, histo_2)
                                #print('KS_values_1 : ', len(KS_values_1))
                                #print('KS_values_2 : ', len(KS_values_2))
                                #print('KS_values_3 : ', len(KS_values_3))
                                if (len(KS_values_1) > 5):
                                    yellowCurves = [ KS_values_1[5], KS_values_2[2], KS_values_3[2] ]
                                    yellowCurvesCum = [ KS_values_1[6], KS_values_2[3], KS_values_3[3] ]
                                    ycFlag = True

                            print('ycFlag : ', ycFlag)
                            PictureChoice(histo_1, histo_2, histo_positions[1], histo_positions[2], gif_name, self, 0, c_recomp)
                            if ycFlag:
                                createDatasetFolder2()
                                PictureChoice_DB(histo_1, histo_2, histo_positions[1], histo_positions[2], png_name, self, 0, yellowCurves)
                                PictureChoice_DB2(histo_1, histo_2, histo_positions[1], histo_positions[2], png_cumul_name, self, 0, yellowCurvesCum)

                                percentage = 0.05
                                if ( KS_values_1[4] >= percentage ):
                                    color = 'green'
                                    DB_picture = valEnv_d.imageOK()
                                else:
                                    color = 'red'
                                    DB_picture = valEnv_d.imageKO()
                            #stop
                            if ( lineFlag ):
                                extWrite( "\n<td><a href=\"#TOP\"><img width=\"18\" height=\"18\" border=\"0\" align=\"middle\" src=" + valEnv_d.imageUp() + " alt=\"Top\"/></a></td>\n" , wp_Files)
                            if (  histo_positions[3] == "0" ):
                                extWrite( "<td>" , wp_Files)
                                extWrite( "<a id=\"" + short_histo_name + "\" name=\"" + short_histo_name + "\"" , wp_Files)
                                extWrite( " href=\"" + gif_name + "\"><img border=\"0\" class=\"image\" width=\"440\" src=\"" + gif_name + "\"></a>" , wp_Files)
                                extWrite( " </td>\n" , wp_Files)
                                fHisto.write( "<td>")
                                fHisto.write( "<a id=\"" + short_histo_name + "\" name=\"" + short_histo_name + "\"")
                                fHisto.write( " href=\"" + gif_name + "\"><img border=\"0\" class=\"image\" width=\"440\" src=\"" + gif_name + "\"></a>")
                                fHisto.write( "</td>\n")
                                fHisto.write( "\n")
                                # insert here the decision box
                                if DB_flag:
                                    DB.addKSValues(wp_DB, fHisto, color, KS_values_1, KS_values_2, KS_values_3, DB_picture)
                                    extWrite("\n</table>\n", [fHisto])
                                    fHisto.write( "<br>\n")
                                    fHisto.write( "<table border=\"1\" bordercolor=\"blue\" cellpadding=\"2\" style=\"margin-left:auto;margin-right:auto\">\n")
                                    fHisto.write( "<tr>\n")
                                    fHisto.write( "<th scope=\"col\"> </th>\n")
                                    fHisto.write( "<th scope=\"col\">KS curves</th>\n")
                                    fHisto.write( "<th scope=\"col\">yellow curves</th>\n")
                                    fHisto.write( "<th scope=\"col\">cumulatives curves</th>\n")
                                    fHisto.write( "</tr>\n")
                                    fHisto.write( "<tr>\n")
                                    DB.generatePlotFile(fHisto, valEnv_d.KS_Path(), short_histo_names[0], png_name, png_cumul_name, ycFlag)
                                    DB.addKSPlots(wp_DB, valEnv_d.KS_Path(), short_histo_names[0])
                                    #if ycFlag:
                                    #    DB.addYCPlots(wp_DB, png_name) # refaire les tests existence
                                    #    DB.addCumPlots(wp_DB, png_cumul_name)
                                lineFlag = False
                            else: # line_sp[3]=="1"
                                extWrite( "<td>" , wp_Files)
                                extWrite( "<a id=\"" + short_histo_name + "\" name=\"" + short_histo_name + "\"" , wp_Files)
                                extWrite( " href=\"" + gif_name + "\"><img border=\"0\" class=\"image\" width=\"440\" src=\"" + gif_name + "\"></a>" , wp_Files)
                                extWrite( "</td>" , [wp_index])
                                fHisto.write( "<td>")
                                fHisto.write( "<a id=\"" + short_histo_name + "\" name=\"" + short_histo_name + "\"")
                                fHisto.write( " href=\"" + gif_name + "\"><img border=\"0\" class=\"image\" width=\"440\" src=\"" + gif_name + "\"></a>")
                                fHisto.write( "</td>\n")
                                fHisto.write( "\n")
                                if DB_flag:
                                    #extWrite( "</td>" , [wp_DB])
                                    DB.addKSValues(wp_DB, fHisto, color, KS_values_1, KS_values_2, KS_values_3, DB_picture)
                                    extWrite("\n</table>\n", [fHisto])
                                    fHisto.write( "<br>\n")
                                    fHisto.write( "<table border=\"1\" bordercolor=\"blue\" cellpadding=\"2\" style=\"margin-left:auto;margin-right:auto\">\n")
                                    fHisto.write( "<tr>\n")
                                    fHisto.write( "<th scope=\"col\"> </th>\n")
                                    fHisto.write( "<th scope=\"col\">KS curves</th>\n")
                                    fHisto.write( "<th scope=\"col\">yellow curves</th>\n")
                                    fHisto.write( "<th scope=\"col\">cumulatives curves</th>\n")
                                    fHisto.write( "</tr>\n")
                                    fHisto.write( "<tr>\n")
                                    DB.generatePlotFile(fHisto, valEnv_d.KS_Path(), short_histo_names[0], png_name, png_cumul_name, ycFlag)
                                    DB.addKSPlots(wp_DB, valEnv_d.KS_Path(), short_histo_names[0])
                                    #if ycFlag:
                                    #    DB.addYCPlots(wp_DB, png_name)
                                    #    DB.addCumPlots(wp_DB, png_cumul_name)
                                extWrite( "\n</tr>", wp_Files ) # close the histo names loop
                                lineFlag = True

                            extWrite("</table>\n", [fHisto])
                            fHisto.close()

                # fin ecriture des histos
                extWrite( "\n</table>\n" , wp_Files)

                #wp.close()
                wp_index.close()
                if DB_flag:
                    wp_DB.close() # must have a test if exist

                os.chdir('../') # back to the final folder.
                ''''''

        # get time for end
        finish = time.time()
        print('total time to execute : %8.4f' % (finish-start)) # python2

        print('end of run')

    def testForDataSetsFile(self, tmp_path, type, dataSetsName): # perhaps t_ref is not useful
        # also get the tree path part (tp_rel, tp_ref) for root files :
        # folder location for those files : HistosConfigFiles/
        # ElectronMcSignalValidator
        # ElectronMcSignalValidatorMiniAOD
        # ElectronMcSignalValidatorPt1000
        # ElectronMcFakeValidator

        t_rel = tmp_path + 'ElectronMcSignalHistos.txt'
        t_ref = t_rel
        tp_rel = 'ElectronMcSignalValidator'
        tp_ref = tp_rel
        if ( re.search('Pt1000', dataSetsName) ):
            t_rel = tmp_path + 'ElectronMcSignalHistosPt1000.txt'
            t_ref = t_rel
            tp_rel = 'ElectronMcSignalValidatorPt1000'
            tp_ref = tp_rel
        elif ( re.search('QCD', dataSetsName) ):
            t_rel = tmp_path + 'ElectronMcFakeHistos.txt'
            t_ref = t_rel
            tp_rel = 'ElectronMcFakeValidator'
            tp_ref = tp_rel
        else: # general
            if type[0] == 'RECO': # RECO
                if type[1] == 'miniAOD': # RECO vs miniAOD
                    t_rel = tmp_path + 'ElectronMcSignalHistosMiniAOD.txt' # we have only miniAOD histos to compare.
                    t_ref = tmp_path + 'ElectronMcSignalHistosMiniAOD.txt'
                    tp_rel = 'ElectronMcSignalValidator'
                    tp_ref = 'ElectronMcSignalValidatorMiniAOD'
                else: # RECO vs RECO
                    t_rel = tmp_path + 'ElectronMcSignalHistos.txt'
                    t_ref = t_rel
                    tp_rel = 'ElectronMcSignalValidator'
                    tp_ref = 'ElectronMcSignalValidator'
            elif type[0] == 'miniAOD': # miniAOD vs miniAOD
                t_rel = tmp_path + 'ElectronMcSignalHistosMiniAOD.txt'
                t_ref = t_rel
                tp_rel = 'ElectronMcSignalValidatorMiniAOD'
                tp_ref = tp_rel
        return [t_rel, t_ref, tp_rel, tp_ref]
