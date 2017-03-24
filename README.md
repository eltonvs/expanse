# expanse

## Getting Started

To install this project on localhost, you'll need to follow these steps:

1 - Change directory into your newly created project.
```Shell
$ cd expanse
```

2 - Create a Python virtual environment.
```Shell
$ virtualenv expanse --> Python2
```

3 - Activate your env
```Shell
$ source $PATH_TO_YOUR_ENV$/bin/activate
```

4 - Install requirements:
```Shell
(env)$ pip install -r requirements.txt
```

5 - Upgrade packaging tools.
```Shell
(env)$ pip install --upgrade pip setuptools
```

6 - Install the project in editable mode with its testing requirements.
```Shell
(env)$ pip install -e ".[testing]"
```

7 - Run your project.
```Shell
(env)$ pserve development.ini --reload
```

or, if you're lazy, just run this script (on project folder, of course):
```Shell
$ sh install_project.sh
```
