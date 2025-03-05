### quickValidationsNG

if you want to make validations (simple ones) without GUI, you can make it with this script. See README file for use.

**05/03/2025** - Add a copyFiles.sh to launch after the validations. It copy config files into /afs/cern.ch/work/a/archiron/private/CONFIG/ folder & DQM ROOT files into /afs/cern.ch/work/a/archiron/private/TEST_GITCLONE/quickValidationsNG/DATA/ folder.

**29/01/2025** - Add a KS check (KS folder) to generate some comparisons pictures with KS.

**26/11/2024** - add a correction for TProfiles into graphicFunctions.py

**22/11/2024** - add a correction for Pt1000 & Fake cases.

**04/11/2024** - add a test for the correct writteness of picture_ext.

**22/10/2024** - minor bug correction : transfert of globalTag into a check function.

**17/10/2024** - minor bug correction (tesForDataSetsFile2()). new display for dataset operation.  

**16/10/2024** - reduce the print/check part with new functions.  

**15/10/2024** - add png pictures creation.  

#### First of all you have to create a local area for the work
#### go into your favorite folder, and execute the following commands :
git clone https://github.com/archiron/quickValidationsNG quickValidationsNG  
git clone https://github.com/archiron/ChiLib_CMS_Validation ChiLib_CMS_Validation  
cd quickValidationsNG/  
preparation of the config.py file (see later). You have a a config.py.test file that you can use with the command : cp config.py.test config.py   
do not forget to update the KS_reference_release (if needed) and the Validation_reference with the corrects link which is given at the end of the mail dedicated to the validation.

#### launch the validation :
then, when the config.py file is ready, you can launch the validation with :  
python3 mainSeq.py

#### work in local area 
you have : workDir = os.getcwd() and the ROOT files are located into a DATA folder. If you use the preceeding instructions, the DATA folder is always created.
The ROOT files are downloaded automatically, or you can download them into the DATA folder with the quickRootDown script.
For local use (your own ROOT files), you have to put uour own into the DATA folder.  

#### batch 
you can use all precedings commands with a batch file named quickValidationSeq.sh  
Into the folder you want to work, copy the quickValidationSeq.sh locally.  
launch : chmod 755 quickvalidationSeq.sh
launch : . quickValidationSeq.sh
#### WARNING : there is no "/" between the dot and quickValidationSeq.sh (only a blank).


### ===================================
### Data to be initiated in config.py
### ===================================
you can use the quickValGen script.  
all validations mut be written as :  
#############################################################################  
#### global data
web_repo = ['/eos/project/c/cmsweb/www/egamma/validation/Electrons/Dev/', 'dev']  
!#web_repo = ['/eos/project/c/cmsweb/www/egamma/validation/Electrons/Releases/', 'std']  
!#web_repo = ['/eos/project/c/cmsweb/www/egamma/validation/Electrons/Test/', 'dev']  
KS_reference_release = 'CMSSW_11_2_0_pre11_2021' # only for Kolmogorov-Smirnov use  
Validation_reference = 'https://cms-talk.web.cern.ch/t/new-validation-campaign-12-5-0-pre5-phase2-d88-added/14722'

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

for the web_repo you can choose between 3 locations and 2 extensions.
 .  
/!\ You can have multiple part of personalization (i.e. GeV_1, GeV_2, GeV_3, ..) by copying the first (GeV_1) repeatedly you want. 

if you have the ROOT files names, then Global Tags are not necessary.   
You MUST have the same number of DB flags than datasets idem for Global Tags if you use them.   
GT MUST be in the complete form (i.e. CMSSW_11_1_0_pre4-110X_mcRun3_2021_realistic_v8-v1) only one choice per validation.  
ROOT files are on the form : release ROOT file, reference ROOT file and so on.  

### size reduction of the ROOT files.
reduceSizeFile1.py is callable with : python3 reduceSizeFile1.py and reduce the size of the ROOT files located into the DATA folder (line84). The name of the folder can be modified
but have to be located into the same folder as the reduceSizeFile1.py file.
