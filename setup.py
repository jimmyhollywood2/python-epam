import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-office-manager',
    version='0.1',
    packages=find_packages(),
    license='MIT License',
    description='A simple Django app to manage departments and employees.',
    #coveralls or python-coveralls?
    install_requires=[
        'django==2.2.20',
        'django-mysql>=3.2',
        'djangorestframework>=3.10.2',
        'mysqlclient>=1.4.4',
        'pylint-django',
        'pylint',
        'requests',
        ],
    author='Dmitri Zawadski',
    author_email='dzdimati@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2.4',
        'License :: MIT License',
        'Operating System :: Linux Ubuntu',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)