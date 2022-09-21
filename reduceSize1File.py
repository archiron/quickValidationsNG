#! /usr/bin/env python
#-*-coding: utf-8 -*-

################################################################################
# reduceSize1File: a tool to reduce the size of the ROOT files, keeping only
# the used branches.
# for egamma validation comparison                              
#
# MUST be launched with the cmsenv cmd after a cmsrel cmd !!
#                                                                              
# Arnaud Chiron-Turlay LLR - arnaud.chiron@llr.in2p3.fr                        
#                                                                              
################################################################################

import os,sys, re

# lines below are only for func_Extract
from sys import argv
from os import listdir
from os.path import isfile, join

argv.append( '-b-' )
import ROOT
ROOT.gROOT.SetBatch(True)
argv.remove( '-b-' )

from ROOT import *

def changeDirectory(rootFile, path):
    """
    Change the current directory (ROOT.gDirectory) by the corresponding (rootFile,pathSplit)
    module from cmdLineUtils.py
    """
    rootFile.cd()
    theDir = ROOT.gDirectory.Get(path)
    if not theDir:
        print("Directory %s does not exist." % path)
    else:
        theDir.cd()
    return 0

def checkLevel(f_rel, f_out, path0, listkeys, nb, inPath):
    #inPath = 'DQMData/Run 1/Info'
    print('path : %s' % path0)
    if path0 != "":
        path0 += '/'
    
    for elem in listkeys:
        #print('%d == checkLevel : %s' % (nb, elem.GetTitle()))
        if (elem.GetClassName() == "TDirectoryFile"):
            path = path0 + elem.GetName()
            if (nb >= 3 and re.search(inPath, path)):
                print('\npath : %s' % path)
                f_out.mkdir(path)
            tmp = f_rel.Get(path).GetListOfKeys()
            checkLevel(f_rel, f_out, path, tmp, nb+1, inPath)
        elif (elem.GetClassName() == "TTree"):
            #print('------ TTree')
            src = f_rel.Get(path0)
            cloned = src.CloneTree()
            #f_out.WriteTObject(cloned, elem.GetName())
            if (nb >= 3 and re.search(inPath, path0)):
                changeDirectory(f_out, path0[:-1])
                cloned.Write()
        elif (elem.GetClassName() != "TDirectory"):
            #print('copy %s object into %s path' % (elem.GetName(), path0[:-1]))
            #f_out.WriteTObject(elem.ReadObj(), elem.GetName())#:"DQMData/Run 1/EgammaV"
            if (nb >= 3 and re.search(inPath, path0)):
                changeDirectory(f_out, path0[:-1])
                elem.ReadObj().Write()

def getListFiles(path, ext='root'):
    # use getListFiles(str path_where_the_files_are, str 'ext')
    # ext can be root, txt, png, ...
    # default is root
    ext = '.' + ext
    #print('path : %s' % path)
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    onlyfiles = [f for f in onlyfiles if f.endswith(ext)] # keep only root files
    #print(onlyfiles)
    return onlyfiles

print("func_ReduceSize")
folderName = 'DATA/'
# get list of added ROOT files for comparison
rootFilesList = getListFiles(folderName, 'root')
for elem in list(rootFilesList):
    if ('ROOT626' not in elem):
        rootFilesList.remove(elem)
#for elem in list(rootFilesList):
#    if ('Zp' not in elem):
#        rootFilesList.remove(elem)
print('we use the files :')
for item in rootFilesList:
    print(item)
#stop()
for item in rootFilesList:
    '''print(item)'''
    input_file = folderName + item
    racine = input_file.split('.')
    output_file = racine[0] + 'b.' + racine[1]

    print('\n %s' % input_file)
    print(' %s' % output_file)

    paths = ['DQMData/Run 1/EgammaV', 'DQMData/Run 1/Info']

    f_rel = ROOT.TFile(input_file, "UPDATE")
    f_out = TFile(output_file, 'recreate')
    t2 = f_rel.GetListOfKeys()
    print(racine[0] + 'b.' + racine[1])
    for elem in paths:
        checkLevel(f_rel, f_out, "", t2, 0, elem)

    f_out.Close()
    f_rel.Close()

    tmp_file = folderName + item + '.tmp'
    print('\n %s' % tmp_file)
    print('move input_file to tmp_file')
    os.rename(input_file, tmp_file) # mv input_file -> tmp_file
    print('move output_file to input_file')
    os.rename(output_file, input_file) # mv output_file -> input_file
    print('delete tmp_file')
    os.remove(tmp_file) # remove input_file

print("Fin !")

