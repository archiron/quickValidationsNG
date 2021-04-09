#!/bin/bash
# This file is called ./validations.sh
#
LOG_SOURCE=$PWD
echo "LOG_SOURCE : $LOG_SOURCE"

git clone https://github.com/archiron/quickValidationsNG quickValidationsNG
git clone https://github.com/archiron/ChiLib_CMS_Validation ChiLib_CMS_Validation
cd quickValidationsNG/
# preparation of the config.py file (see later)
# cp config.py.test config.py
echo ls
python mainSeq.py
