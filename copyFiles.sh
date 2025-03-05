#!/bin/sh
# This file is called . copyFiles.sh

#Black        0;30     Dark Gray     1;30
#Red          0;31     Light Red     1;31
#Green        0;32     Light Green   1;32
#Brown/Orange 0;33     Yellow        1;33
#Blue         0;34     Light Blue    1;34
#Purple       0;35     Light Purple  1;35
#Cyan         0;36     Light Cyan    1;36
#Light Gray   0;37     White         1;37

RED='\033[0;31m'
BLUE='\033[0;34m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color
echo -e "I ${BLUE}love${GREEN} Stack Overflow${NC}"

# cp CONFIG_FILES/config.*.py -v /afs/cern.ch/work/a/archiron/private/CONFIG/
a=`ls config.*.py`
for name in ${a[@]}
do
  #echo $name
  target='/afs/cern.ch/work/a/archiron/private/CONFIG/'$name
  #echo $target
  if [ ! -f $target ]; then
    echo -e "cp ${BLUE}$name${NC} $target"
    cp $name $target
  else
    echo -e "cp ${GREEN}$name${NC} $target"
    cp $name $target
  fi
done

# cp DATA/*.root -v /afs/cern.ch/work/a/archiron/private/TEST_GITCLONE/quickValidationsNG/DATA/
a=`ls DATA/DQM*.root`
for name in ${a[@]}
do
  #echo $name
  target='/afs/cern.ch/work/a/archiron/private/TEST_GITCLONE/quickValidationsNG/'$name
  #echo $target
  if [ ! -f $target ]; then
    echo -e "cp ${BLUE}$name${NC} $target"
    cp $name $target
  else
    echo -e "cp ${GREEN}$name${NC} $target"
    cp $name $target
  fi
done
