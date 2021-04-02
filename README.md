### quickValidationsNG

if you want to make validations (simple ones) without GUI, you can make it by downloading the files located at :
/eos/project/c/cmsweb/www/egamma/validation/Electrons/quickValidationSeq/

### you can make some simple validations with this python script.
### First of all you have to create a local area for the work

 cmsrel CMSSW_10_6_0
 cd CMSSW_10_6_0/src
 cmsenv
 mkdir DATA
### work in local area : you have : workDir = os.getcwd() and the root files are located into a DATA folder.
### download the root files into the DATA folder with the quickRootDown script.

### copy locally the config.py file into config.py

### modify the config.py as you want

### launch the command :
 python /eos/project/c/cmsweb/www/egamma/validation/Electrons/quickValidationSeq/mainSeq.py for sequential tasks
  
### batch
copy locally the config.py file into config.py
copy locally the quickValidationSeq.sh & quickValidationSeq.submit files
modify the config.py file with the values you want
verify that in the quickValidationSeq.sh there is the correct work path (workDir)
launch : condor_submit quickValidationSeq.submit

===================================
Data to be initiated in config.py
===================================
all validations mut be written as :
### personalization 1
GUI_1 = [
['CMSSW_11_1_0_pre4', 'CMSSW_11_1_0_pre3'] , # release/reference
['quick_2021', ''] , # relref_extention
['TTbar_14TeV', 'ZEE_14'] ,  #datasets
'FullvsFull' , # choice
['RECO', 'RECO'] , # relrefValtype RECO vs RECO
['', ''] ,  # GT one couple rel/ref for each dataset
['DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_11_1_0_pre4-110X_mcRun3_2021_realistic_v8-v1__DQMIO.root',
 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_11_1_0_pre3-110X_mcRun3_2021_realistic_v8-v1__DQMIO.root',
 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_11_1_0_pre4-110X_mcRun3_2021_realistic_v8-v1__DQMIO.root',
 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_11_1_0_pre3-110X_mcRun3_2021_realistic_v8-v1__DQMIO.root',], # relref files one couple rel/ref for each dataset
[False, True], # DB flag
]

if you have the ROOT files names, then Global Tags are not necessary.
You MUST have the same number of DB flags than datasets
idem for Global Tags if you use them.
only one choice per validation.
Root files are on the form : release ROOT file, reference ROOT file and so on.
