### quickValidationsNG

if you want to make validations (simple ones) without GUI, you can make it with this script. See README file for use.

#### First of all you have to create a local area for the work
#### go into your favorite folder, and execute the following commands :
git clone https://github.com/archiron/quickValidationsNG quickValidationsNG  
git clone https://github.com/archiron/ChiLib_CMS_Validation ChiLib_CMS_Validation  
cd quickValidationsNG/  
preparation of the config.py file (see later). You have a a config.py.test file that you can use with the command : cp config.py.test config.py  

#### launch the validation :
then, when the config.py file is ready, you can launch the validation with :  
python mainSeq.py

#### work in local area 
you have : workDir = os.getcwd() and the ROOT files are located into a DATA folder.  
The ROOT files are downloaded automatically, or you can download them into the DATA folder with the quickRootDown script.  

#### modify the config.py as you want

#### batch (to be evaluated !)
you can use all precedings commands with a batch file named quickValidationSeq.sh  
Into the folder you want to work, copy locally the quickValidationSeq.sh (& quickValidationSeq.submit) and the config.py.test file(s).  
cp config.py.test config.py  
modify the config.py file with the values you want (SEE BELOW )  
launch : ./quickValidationSeq.sh (be careful of rights! - 755).  
launch : condor_submit quickValidationSeq.submit !!! NOT yet tested  

### ===================================
### Data to be initiated in config.py
### ===================================
you can use the quickValGen script.  
all validations mut be written as :  
#############################################################################  
#### global data
web_repo = ['/eos/project/c/cmsweb/www/egamma/validation/Electrons/Dev/', 'dev']  
#web_repo = ['/eos/project/c/cmsweb/www/egamma/validation/Electrons/Releases/', 'std']  
KS_reference_release = 'CMSSW_11_2_0_pre11_2021' # only for Kolmogorov-Smirnov use  

#### personalization 1
GeV_1 = [  
['CMSSW_11_1_0_pre4', 'CMSSW_11_1_0_pre3'] , # release/reference  
['quick_2021', '2021.04.02'] , # relref_extent  
['TTbar_14TeV', 'ZEE_14'] ,  #datasets  
'FullvsFull' , # choice  
['RECO', 'RECO'] , # relrefValtype RECO vs RECO  
['', ''] ,  # GT one couple rel/ref for each dataset  
['DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_11_1_0_pre4-110X_mcRun3_2021_realistic_v8-v1__DQMIO.root', # release ROOT file  
 'DQM_V0001_R000000001__RelValTTbar_14TeV__CMSSW_11_1_0_pre3-110X_mcRun3_2021_realistic_v8-v1__DQMIO.root', # reference ROOT file  
 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_11_1_0_pre4-110X_mcRun3_2021_realistic_v8-v1__DQMIO.root',  
 'DQM_V0001_R000000001__RelValZEE_14__CMSSW_11_1_0_pre3-110X_mcRun3_2021_realistic_v8-v1__DQMIO.root',], # relref files one couple rel/ref for each dataset  
[False, False], # DB flag for Kolmogorov-Smirnov use  
]  

#############################################################################

 .  
/!\ You can have multiple part of personalization (i.e. GeV_1, GeV_2, GeV_3, ..) by copying the first (GeV_1) repeatedly you want.  
---  

if you have the ROOT files names, then Global Tags are not necessary.   
You MUST have the same number of DB flags than datasets idem for Global Tags if you use them.   
GT MUST be in the complte form (i.e. CMSSW_11_1_0_pre4-110X_mcRun3_2021_realistic_v8-v1) only one choice per validation.  
ROOT files are on the form : release ROOT file, reference ROOT file and so on.  
