#!/bin/bash

# Assuming that you're on project folder

# Create ~/envs/ folder
echo -e "Creating ~/envs/ folder\n"
mkdir ~/envs/

# Create virtual env
echo -e "Creating virtualenv...\n"
cd ~/envs/
virtualenv expanse
cd -

# Activating env
echo -e "Activate env\n"
source ~/envs/expanse/bin/activate

# Installing dependencies
echo -e "Install dependencies\n"
install -r requirements.txt
pip install --upgrade pip setuptools
pip install -e ".[testing]"
