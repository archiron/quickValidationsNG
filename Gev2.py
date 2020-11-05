#! /usr/bin/env python
#-*-coding: utf-8 -*-

import os,sys,subprocess,shutil
import concurrent.futures
import time
import numpy as np

sys.path.append('/afs/cern.ch/user/a/archiron/lbin/ChiLib')

from graphicFunctions import *
from functions import *
from networkFunctions import list_search_0, list_search_1, cmd_load_files
from valEnv_default import env_default
from config_par import * # WARNING, must be the local version and not the remote one !!!

class Gev2(): 
    def __init__(self):
        print('begin to run')
        initRoot()

        sys.path.append(os.getcwd()) # path where you work
        import config_par as cf2
        valEnv_d = env_default()
        
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
        
        print('\nProcessPool')
        
        # Processes
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
            print('webFolder : %s' % webFolder)
            
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

            # sort datasets & files
            datasets.sort()
            relFile.sort()
            refFile.sort()
        
            #print(valEnv_d.relVT, valEnv_d.refVT)
            print(relrefVT[0], relrefVT[1])
            output1 = list()
            with concurrent.futures.ProcessPoolExecutor() as executor:
                #          0       1              2        3           4            5            6                7        8      9            10           11
                args = ((self, str(webFolder), release, reference, relrefVT[0], relrefVT[1], shortRelease, shortReference, b, datasets[b], rel_ref[b], validation[7][b]) for b in range(0, N)) #in locals()
                for out1 in executor.map(createWebPage, args):
                #    # put results into correct output list
                    output1.append(out1)
            #print('original inputs: %s' % repr(output1))
            # get time for end
            finish = time.time()
            print('total time to execute : %8.4f' % (finish-start)) # python2

            print('end of run')
        
