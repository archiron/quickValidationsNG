#!/bin/bash
# This file is called ./validations.sh
#

git clone https://github.com/archiron/quickValidationsNG quickValidationsNG
git clone https://github.com/archiron/ChiLib_CMS_Validation ChiLib_CMS_Validation
# the config.py file is assumed to be modified.
cd quickValidationsNG/
cp config.py.test config.py

