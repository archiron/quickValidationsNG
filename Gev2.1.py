#! /usr/bin/env python
#-*-coding: utf-8 -*-

import os,sys,subprocess,shutil
import concurrent.futures
import time
import numpy as np

sys.path.append('/afs/cern.ch/user/a/archiron/lbin/ChiLib/')

from graphicFunctions import *
from functions import *

class Gev2(): 
    def __init__(self):
        print('begin to run')
        initRoot()

        sys.path.append(sys.argv[1])
        from valEnv import env
        valEnv = env()
        
        ### PLEASE WARNING DO NOT FORGET TO COMPLETE THE DEFINITION IN valEnv.py ###
        print('working in %s\n' % valEnv.workDir() )
        #stop

        webFolder = valEnv.webFolder()
        print('webFolder : %s' % webFolder)
        if not os.path.exists(webFolder): # only create the first folder for saving gifs, i.e. release folder. 
            self.exist_webFolder = False
        else:
            self.exist_webFolder = True

        if self.exist_webFolder: # True
            print("%s already created\n" % str(webFolder))
        else: # False
            os.makedirs(str(webFolder))

        datasets = valEnv.dataSets()
        
        # get time for begin
        start = time.time()           # let's see how long this takes
        
        # create new list from rel_files& ref_files
        N = len(datasets)
        rel_ref = []
        for i in range(0, N):
            rel_ref.append([valEnv.relFiles()[i], valEnv.refFiles()[i]])
        
        # Threading : same as Processes with concurrent.futures.ThreadPoolExecutor() as executor: instead of concurrent.futures.ProcessPoolExecutor() as executor:
        
        print('\nProcessPool')
        #print(valEnv.relVT(), valEnv.refVT())
        print(valEnv.relrefVT()[0], valEnv.relrefVT()[1])
        # Processes
        ''''''
        output1 = list()
        with concurrent.futures.ProcessPoolExecutor() as executor:
            args = ((self, webFolder, valEnv.redRel(), valEnv.blueRef(), valEnv.relrefVT()[0], valEnv.relrefVT()[1], valEnv.rel(), valEnv.ref(), b, datasets[b], rel_ref[b]) for b in range(0, N-0))
            for out1 in executor.map(createWebPage, args):
                # put results into correct output list
                output1.append(out1)
        #print('original inputs: %s' % repr(output1))
        # get time for end
        finish = time.time()
        print('total time to execute : %8.4f' % (finish-start)) # python2

        #stop
            
        print('end of run')


