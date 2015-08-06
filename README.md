# paiji2
[![Build Status](https://travis-ci.org/rezometz/paiji2.svg?branch=master)](https://travis-ci.org/rezometz/paiji2)
[![Code Climate](https://codeclimate.com/github/rezometz/paiji2/badges/gpa.svg)](https://codeclimate.com/github/rezometz/paiji2)
[![Coverage Status](https://coveralls.io/repos/rezometz/paiji2/badge.svg?branch=master&service=github)](https://coveralls.io/github/rezometz/paiji2?branch=master)

## Install guidelines

### Getting last version
First, you have to get the last release of this repository (or a previous one).
For so, clone it into the directory of your choice :

    git clone https://github.com/rezometz/paiji2.git

Then go into the newly created directory named "paiji2" which
will be referenced as "working directory" in the next paragraphs.

See http://wiki.rezometz.org for more details.

### Virtualenv
As we are using new releases of python packages and to avoid 
inconsistency in your system configuration with python packages,
we advice you to configure a virtual environment.

First, you have to install virtualenv and virtualenvwrapper (recommended).

Then create the virtualenv by typing (in your working directory) :

    mkvirtualenv paiji2 -r 'requirement/devs.txt'
	pip install -r 'requirements/custom_packages.txt'

### Configure the website
You can now configure your website. Start by copying the settings_example.py 
file as settings.py (in the paiji2 directory) :

    cd paiji2
    cp settings_example.py settings.py

Then open the settings.py file and change the different environments variables
as you wish.

### Static Files ###

First you will need to install nodejs and bower in the virtualenv.

    npm install -g bower

Then in django to fetch the JS and CSS files run:

    python manage.py bower install

### Debug mode
You are now fully prepared to work on on the project on development mode. The project can be launched using :

    python manage.py runserver

Nevertheless, never forget two things :
* you have to use your defined virtual env when launching the server (or
in any cases using the manage.py file)
* never use this in production mode.

Further explanations will be given to deploy it in production mode later
