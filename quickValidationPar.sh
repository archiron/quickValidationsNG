#!/bin/sh
# This file is called ./AllSteps_init.sh

LOG_SOURCE=$PWD 

echo "LOG_SOURCE : $LOG_SOURCE"

cd $LOG_SOURCE
#eval `scramv1 runtime -sh`
cd -

#python /afs/cern.ch/user/a/archiron/lbin/quickValidations/main.py /afs/cern.ch/work/a/archiron/private/CMSSW_11_0_0_pre13/src/TMP # for parallel
python main.py $LOG_SOURCE # for sequential

echo 'end'

