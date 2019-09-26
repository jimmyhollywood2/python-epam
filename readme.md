# Readme
## Web Application Office Manager

[![Build Status](https://travis-ci.org/jimmyhollywood/python-epam.svg?branch=master)](https://travis-ci.org/jimmyhollywood/python-epam) [![Coverage Status](https://coveralls.io/repos/github/jimmyhollywood/python-epam/badge.svg?branch=master)](https://coveralls.io/github/jimmyhollywood/python-epam?branch=master)

#### Office Manager will provide the following functions:
* displaying list of departments
* displaying list of employees
* adding/editing/deleting department/employee information

#### Instalation:
1. Install MySQL
```sudo apt-get install mysql```
2. Upload code from github repository
```git clone http://github.com/jimmyhollywood/pythonepam```
3. Create a virtualenv and install package from setup.py
```virtualenv env```
```source path/to/env/bin/activate```
```python install officemanager/setup.py -q```
4. Install and configure MySQL
```sudo apt-get install mysql```
5. Create a new database
```CREATE DATABASE dbname;```
6. Configure sttings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bdname',
        'USER': 'bduser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
        'TEST' : {
            'NAME': 'test',
        }
    },
}
```
7. Start gunicorn server
```cd officemanager```
```gunicorn officemanager.wsgi:application --bind 0.0.0.0:8000```