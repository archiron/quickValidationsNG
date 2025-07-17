#!/bin/sh
# This file is called . simple.sh

RED="\\e[31m"
GREEN="\\e[32m"
BLUE="\\e[34m"
NC="\\e[0m"

#source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.32.04/x86_64-almalinux9.4-gcc114-opt/bin/thisroot.sh 
#source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.32.06/x86_64-almalinux9.4-gcc114-opt/bin/thisroot.sh
source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.36.00/x86_64-almalinux9.5-gcc115-opt/bin/thisroot.sh

if [[ -n "$1" ]]; then
    python3 GevSeqDev-v2.py $1
else
    #echo 'il faut un fichier de configuration.'
    echo -e "${BLUE}WE NEED A CONFIGURATION FILE.${NC}"
fi
