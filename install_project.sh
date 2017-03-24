# Assuming that you're on project folder

# Create ~/envs/ folder
echo "Creating ~/envs/ folder\n"
mkdir ~/envs/

# Create virtual env
echo "Creating virtualenv...\n"
cd ~/envs/
virtualenv expanse
cd -

# Activating env
source ~/envs/expanse/bin/activate

# Installing dependencies
pip install -r requirements.txt
pip install --upgrade pip setuptools
pip install -e ".[testing]"
