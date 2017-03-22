expanse
===============================

Getting Started
---------------

- Change directory into your newly created project.
  cd expanse

- Create a Python virtual environment.
  virtualenv expanse --> Python2

- Activate your env
  source $PATH_TO_YOUR_ENV/bin/activate

- Install requirements:
  (env)$ pip install -r requirements.txt

- Upgrade packaging tools.
  (env)$ pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.
  (env)$ pip install -e ".[testing]"

- Run your project.
  (env)$ pserve development.ini --reload
