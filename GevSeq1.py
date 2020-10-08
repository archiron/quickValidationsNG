#! /usr/bin/env python
#-*-coding: utf-8 -*-

import os,sys,subprocess,shutil
import concurrent.futures
import time
import numpy as np

sys.path.append('/afs/cern.ch/user/a/archiron/lbin/ChiLib')

from graphicFunctions import *
from functions import *

class GevSeq(): 
    def __init__(self):
        print('begin to run')
        initRoot()

        sys.path.append(sys.argv[1]) # path where you work
        from valEnv import env
        valEnv = env()
        
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
        
        print('\nSequential')
        
        # sequential
        # get time for begin
        start = time.time()           # let's see how long this takes

        os.chdir(webFolder) # going into finalFolder
        
        for i, elt in enumerate(datasets):
            dts = elt
            print('dataset : %s' % dts)
            dataSetFolder = str(valEnv.relVT() + '-' + valEnv.refVT() + '_' + dts)
            createDatasetFolder(dataSetFolder)
            os.chdir(dataSetFolder) # going to dataSetFolder
            
            # get config files 
            it1 = valEnv.workDir() + 'ElectronMcSignalHistos.txt' # valEnv.tmpPath() + 
            #it1 = valEnv.tmpPath() + 'ElectronMcSignalHistosMiniAOD.txt'
            it2 = it1
            tp_1 = 'ElectronMcSignalValidator'
            tp_2 = 'ElectronMcSignalValidator'

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
            #input_rel_file = workDir + '/DATA/' + str(valEnv.relFiles()[i])
            input_rel_file = valEnv.workDir() + '/DATA/' + str(valEnv.relFiles()[i])
            print(input_rel_file)
            
            #histoTest = 'h_recEleNum'
            #histoTest = 'h_ele_PoPtrueVsEta_pfx'

            f_rel = ROOT.TFile(input_rel_file)
            h1 = getHisto(f_rel, tp_1)
            print("h1")
            print(h1)

            input_ref_file = valEnv.workDir() + '/DATA/' + str(valEnv.refFiles()[i])
            f_ref = ROOT.TFile(input_ref_file)
            h2 = getHisto(f_ref, tp_2)
            print("CMP_CONFIG = %s\n" % CMP_CONFIG)
            print("input_rel_file = %s\n" % input_rel_file)
            print("input_ref_file = %s\n" % input_ref_file)
            print("h2")

            wp = open('index.html', 'w') # web page
            wp.write("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 3.2 Final//EN\">\n")
            wp.write("<html>\n")
            wp.write("<head>\n")
            wp.write("<meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\" />\n")
            wp.write("<title> " + CMP_TITLE + " </title>\n") #option -t dans OvalFile
            wp.write("</head>\n")
            wp.write("<a NAME=\"TOP\"></a>")
            wp.write("<h1><a href=\"../\"><img border=0 width=\"22\" height=\"22\" src=\"../../../../img/up.gif\" alt=\"Up\"/></a>&nbsp; " + CMP_TITLE + " </h1>\n" ) # option -t dans OvalFile
        
            wp.write("<b><font color='red'> " + valEnv.relVT() + " " + valEnv.rel() + " </font></b>")
            wp.write(" : " + str(valEnv.relFiles()[i]) )
            wp.write("<br>\n")
            wp.write("<b><font color='blue'> " + valEnv.refVT() + " " + valEnv.ref() + " </font></b>")
            wp.write(" : " + str(valEnv.refFiles()[i]) )
            wp.write("<br>\n")
        
            if (f_ref == 0):
                wp.write("<p>In all plots below, there was no reference histograms to compare with")
                wp.write(", and the " + valEnv.redRel() + " histograms are in red.") # new release red in OvalFile
            else:
                wp.write("<p>In all plots below")
                wp.write(", the <b><font color='red'> " + valEnv.redRel() + " </font></b> histograms are in red") # new release red in OvalFile
                wp.write(", and the <b><font color='blue'> " + valEnv.blueRef() + " </font></b> histograms are in blue.") # ref release blue in OvalFile
            wp.write(" Some more details") # 
            wp.write(", <a href=\"" + CMP_CONFIG + "\">specification</a> of histograms") # .txt file
            wp.write(", <a href=\"gifs/\">images</a> of histograms" + "." ) # 
            wp.write("</p>\n")

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
            wp.write( "<table border=\"1\" cellpadding=\"5\" width=\"100%\">" )
        
            # ecriture du tableau general
            firstFlag= True
            for i in range(0, len(titlesList)):
                if ( i % 5  == 0 ):
                    wp.write( "\n<tr valign=\"top\">" )
                textToWrite = ""
                wp.write( "\n<td width=\"10\">\n<b> " + titlesList[i] + "</b>" )
                titles = titlesList[i].split() # explode(" ", $clefs[$i])
                if len(titles) > 1 :
                    titleShortName = titles[0] + "_" + titles[1]
                else:
                    titleShortName = titles[0]
                wp.write( "&nbsp;&nbsp;" + "<a href=\"#" + titleShortName + "\">" ) # write group title
                #wp.write( "<img width=\"18\" height=\"15\" border=\"0\" align=\"center\" src=" + image_point + " alt=\"Top\"/>" + "<br><br>" )
                wp.write( "<img width=\"18\" height=\"15\" border=\"0\" align=\"center\" src=" + valEnv.imagePoint() + " alt=\"Top\"/>" + "<br><br>" )
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
                wp.write( textToWrite )
                    
                # fin ecriture du tableau general
                wp.write( "</td>" )
                if ( i % 5 == 4 ):
                    wp.write( "</tr>" )
                    firstFlag = False
                else:
                    firstFlag = True
        
            if firstFlag:
                extWrite( "</tr>" , wp_Files)
            wp.write( "</table>\n" )
            wp.write( "<br>" )
        
            lineFlag = True
            wp.write( "<table border=\"0\" cellpadding=\"5\" width=\"100%\">" )
            # ecriture des histos
            for i in range(0, len(titlesList)):
                wp.write( "\n<tr valign=\"top\">" )
                wp.write( "\n<td><a href=\"#TOP\"><img width=\"18\" height=\"18\" border=\"0\" align=\"middle\" src=" + valEnv.imageUp() + " alt=\"Top\"/></a></td>\n" )
                titles = titlesList[i].split()
                if len(titles) > 1 :
                    titleShortName = titles[0] + "_" + titles[1]
                else:
                    titleShortName = titles[0]
                wp.write( "\n<td>\n<b> " )
                wp.write( "<a id=\"" + titleShortName + "\" name=\"" + titleShortName + "\"></a>" )
                wp.write( titlesList[i] + "</b></td>" )
                wp.write( "</tr>" )
                for elem in histoArray_0[titlesList[i]]:
                    if ( elem != "endLine" ): 
                        if ( lineFlag ):
                            extWrite( "\n<tr valign=\"top1\">" , wp_Files)
                        
                        short_histo_name, short_histo_names, histo_positions = shortHistoName(elem)
                        gif_name = "gifs/" + short_histo_names[0] + ".gif"
                        histo_name_recomp = short_histo_names[0]
                        print('%s/%s' % (elt, short_histo_names[0]))
                        histo_2 = h2.Get(short_histo_names[0]) #  
                        #coeff_array_1 = []
                        #coeff_array_2 = []
                        #coeff_array_3 = []
                        #print('nb bins : %d' % histo_2.GetXaxis().GetNbins())
                        #i=0
                        #s1 = []
                        #e1 = []
                        #print("histo 2")
                        #for entry in histo_2:
                        #    print("%d/%d : %s - %s") % (i, histo_2.GetXaxis().GetNbins(), entry, histo_2.GetBinError(i))
                        #    s1.append(entry)
                        #    e1.append(histo_2.GetBinError(i))
                        #    i += 1
                        '''if ("ChargeTrue" in short_histo_names[0]):
                            print(s1)
                            print(e1)'''
                        if checkRecompInName(histo_name_recomp): # 
                            short_histo_names[0] = histo_name_recomp.replace("_recomp", "")
                            gif_name = "gifs/" + short_histo_names[0] + "_recomp.gif"
                    
                        histo_1 = h1.Get(short_histo_names[0]) #
                        #print('nb bins : %d' % histo_1.GetXaxis().GetNbins())
                        #i=0
                        #s0 = []
                        #e0 = []
                        #i=0
                        #print("histo 1")
                        #for entry in histo_1:
                        #    print("%d/%d : %s - %s") % (i, histo_1.GetXaxis().GetNbins(), entry, histo_1.GetBinError(i))
                        #    s0.append(entry)
                        #    e0.append(histo_1.GetBinError(i))
                        #    i += 1
                        #print(s0)
                        #print(e0)
                        #d_max_1, r_mask_1 = getDifference_1(s0, e0, s1, e1)
                        #d_max_2, r_mask_2 = getDifference_2(s0, e0, s1, e1) # same as above without couples (0., 0.)
                        #d_max_3, r_mask_3 = getDifference_3(s0, e0, s1, e1) # same as above without couples first & end (0., 0.) couple.
                        '''if ("ChargeTrue" in short_histo_names[0]):
                            print(s0)
                            print(e0)
                            #print('diff. max 1 : %0.4e' % d_max_1)
                            #print('diff. max 2 : %0.4e' % d_max_2)
                            #print('diff. max 3 : %0.4e' % d_max_3)
                            print('mask 1 : ' + ' '.join("{:4d}".format(x) for x in r_mask_1))
                            print('mask 2 : ' + ' '.join("{:4d}".format(x) for x in r_mask_2))
                            print('mask 3 : ' + ' '.join("{:4d}".format(x) for x in r_mask_3))'''
                        #coeff_1 = getCoeff(r_mask_1)
                        #coeff_2 = getCoeff(r_mask_2)
                        #coeff_3 = getCoeff(r_mask_3)
                        '''print('coeff 1 : %6.4f' % coeff_1)
                        print('coeff 2 : %6.4f' % coeff_2)
                        print('coeff 3 : %6.4f' % coeff_3)
                        print(' ')'''
                        #coeff_array_1.append(coeff_1)
                        #coeff_array_2.append(coeff_2)
                        #coeff_array_3.append(coeff_3)
                        
                        if checkRecompInName(histo_name_recomp): # RECO vs miniAOD. For miniAOD vs miniAOD, we do not do this.
                            # we inverse histo1 & histo2 in order to keep the term "recomputed" into the title.
                            PictureChoice(histo_2, histo_1, histo_positions[1], histo_positions[2], gif_name, self, 0)
                        else:
                            PictureChoice(histo_1, histo_2, histo_positions[1], histo_positions[2], gif_name, self, 0)
                    
                        #stop
                        if ( lineFlag ):
                            wp.write( "\n<td><a href=\"#TOP\"><img width=\"18\" height=\"18\" border=\"0\" align=\"middle\" src=" + valEnv.imageUp() + " alt=\"Top\"/></a></td>\n" )
                        if (  histo_positions[3] == "0" ):
                            wp.write( "<td>" )
                            wp.write( "<a id=\"" + short_histo_name + "\" name=\"" + short_histo_name + "\"" )
                            wp.write( " href=\"" + gif_name + "\"><img border=\"0\" class=\"image\" width=\"440\" src=\"" + gif_name + "\"></a>" )
                            #wp.write( "<br>" )
                            #wp.write("<b>confiance : </b>%s - %s - %s\n" % (setColor(coeff_1), setColor(coeff_2), setColor(coeff_3)))
                            #wp.write( "<br>" )
                            #wp.write( "<br>" )
                            wp.write( " </td>\n" )
                            lineFlag = False
                        else: # line_sp[3]=="1"
                            wp.write( "<td>" )
                            wp.write( "<a id=\"" + short_histo_name + "\" name=\"" + short_histo_name + "\"" )
                            wp.write( " href=\"" + gif_name + "\"><img border=\"0\" class=\"image\" width=\"440\" src=\"" + gif_name + "\"></a>" )
                            #wp.write( "<br>" )
                            #wp.write("<b>confiance : </b>%s - %s - %s\n" % (setColor(coeff_1), setColor(coeff_2), setColor(coeff_3)))
                            #wp.write( "<br>" )
                            #wp.write( "<br>" )
                            wp.write( "</td></tr>" )
                            lineFlag = True

            # fin ecriture des histos
            wp.write( "\n</table>\n" )

            '''m_coeff_array_1 = np.asarray(coeff_array_1).mean()
            m_coeff_array_2 = np.asarray(coeff_array_2).mean()
            m_coeff_array_3 = np.asarray(coeff_array_3).mean()
            print('mean coeff 1 : %6.4f' % m_coeff_array_1)
            print('mean coeff 2 : %6.4f' % m_coeff_array_2)
            print('mean coeff 3 : %6.4f' % m_coeff_array_3)
            wp.write("<tr align=\'center\'><b>Global confiance : </b>%s - %s - %s\n<br></tr>" % (setColor(m_coeff_array_1), setColor(m_coeff_array_2), setColor(m_coeff_array_3)))'''

            #wp.write( "</table>\n" )

            wp.close()
            os.chdir('../') # back to the final folder.
        

        # get time for end
        finish = time.time()
        print('total time to execute : %8.4f' % (finish-start)) # python2
            
        print('end of run')


