#!/bin/bash
# This file is called ./validations.sh
#
LOG_SOURCE=$PWD
echo "LOG_SOURCE : $LOG_SOURCE"

git clone https://github.com/archiron/quickValidationsNG quickValidationsNG
git clone https://github.com/archiron/ChiLib_CMS_Validation ChiLib_CMS_Validation
# the config.py file is assumed to be modified.
cp config.py quickValidationsNG/config.py
cd quickValidationsNG/

python mainSeq.py
