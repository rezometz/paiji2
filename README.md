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

# Modules

| Name | Travis | CodeClimate | Coveralls |
| ---- | ------ | ----------- | --------- |
| [paiji2](http://github.com/rezometz/paiji2) | [![Build Status](https://travis-ci.org/rezometz/paiji2.svg?branch=master)](https://travis-ci.org/rezometz/paiji2) | [![Code Climate](https://codeclimate.com/github/rezometz/paiji2/badges/gpa.svg)](https://codeclimate.com/github/rezometz/paiji2) | [![Coverage Status](https://coveralls.io/repos/rezometz/paiji2/badge.svg?branch=master&service=github)](https://coveralls.io/github/rezometz/paiji2?branch=master) |
| [shoutbox](http://github.com/rezometz/django-paiji2-shoutbox) | [![Build Status](https://travis-ci.org/rezometz/django-paiji2-shoutbox.svg?branch=master)](https://travis-ci.org/rezometz/django-paiji2-shoutbox) | [![Code Climate](https://codeclimate.com/github/rezometz/django-paiji2-shoutbox/badges/gpa.svg)](https://codeclimate.com/github/rezometz/django-paiji2-shoutbox) | [![Coverage Status](https://coveralls.io/repos/rezometz/django-paiji2-shoutbox/badge.svg?branch=master&service=github)](https://coveralls.io/github/rezometz/django-paiji2-shoutbox?branch=master) |
| [carpooling](http://github.com/rezometz/django-paiji2-carpooling) | [![Build Status](https://travis-ci.org/rezometz/django-paiji2-carpooling.svg?branch=master)](https://travis-ci.org/rezometz/django-paiji2-carpooling) | [![Code Climate](https://codeclimate.com/github/rezometz/django-paiji2-carpooling/badges/gpa.svg)](https://codeclimate.com/github/rezometz/django-paiji2-carpooling) | [![Coverage Status](https://coveralls.io/repos/rezometz/django-paiji2-carpooling/badge.svg?branch=master&service=github)](https://coveralls.io/github/rezometz/django-paiji2-carpooling?branch=master) |
| [infoconcert](http://github.com/rezometz/django-paiji2-infoconcert) | [![Build Status](https://travis-ci.org/rezometz/django-paiji2-infoconcert.svg?branch=master)](https://travis-ci.org/rezometz/django-paiji2-infoconcert) | [![Code Climate](https://codeclimate.com/github/rezometz/django-paiji2-infoconcert/badges/gpa.svg)](https://codeclimate.com/github/rezometz/django-paiji2-infoconcert) | [![Coverage Status](https://coveralls.io/repos/rezometz/django-paiji2-infoconcert/badge.svg?branch=master&service=github)](https://coveralls.io/github/rezometz/django-paiji2-infoconcert?branch=master) |
| [survey](http://github.com/rezometz/django-paiji2-survey) | [![Build Status](https://travis-ci.org/rezometz/django-paiji2-survey.svg?branch=master)](https://travis-ci.org/rezometz/django-paiji2-survey) | [![Code Climate](https://codeclimate.com/github/rezometz/django-paiji2-survey/badges/gpa.svg)](https://codeclimate.com/github/rezometz/django-paiji2-survey) | [![Coverage Status](https://coveralls.io/repos/rezometz/django-paiji2-survey/badge.svg?branch=master&service=github)](https://coveralls.io/github/rezometz/django-paiji2-survey?branch=master) |
| [weather](http://github.com/rezometz/django-paiji2-weather) | [![Build Status](https://travis-ci.org/rezometz/django-paiji2-weather.svg?branch=master)](https://travis-ci.org/rezometz/django-paiji2-weather) | [![Code Climate](https://codeclimate.com/github/rezometz/django-paiji2-weather/badges/gpa.svg)](https://codeclimate.com/github/rezometz/django-paiji2-weather) | [![Coverage Status](https://coveralls.io/repos/rezometz/django-paiji2-weather/badge.svg?branch=master&service=github)](https://coveralls.io/github/rezometz/django-paiji2-weather?branch=master) |
| [mettis](http://github.com/rezometz/django-paiji2-mettis) | [![Build Status](https://travis-ci.org/rezometz/django-paiji2-mettis.svg?branch=master)](https://travis-ci.org/rezometz/django-paiji2-mettis) | [![Code Climate](https://codeclimate.com/github/rezometz/django-paiji2-mettis/badges/gpa.svg)](https://codeclimate.com/github/rezometz/django-paiji2-mettis) | [![Coverage Status](https://coveralls.io/repos/rezometz/django-paiji2-mettis/badge.svg?branch=master&service=github)](https://coveralls.io/github/rezometz/django-paiji2-mettis?branch=master) |
|![forum](https://github.com/rezometz/django-paiji2-forum) | [![Build Status](https://travis-ci.org/rezometz/django-paiji2-forum.svg?branch=master)](https://travis-ci.org/rezometz/django-paiji2-forum) | [![Code Climate](https://codeclimate.com/github/rezometz/django-paiji2-forum/badges/gpa.svg)](https://codeclimate.com/github/rezometz/django-paiji2-forum) | [![Coverage Status](https://coveralls.io/repos/rezometz/django-paiji2-forum/badge.svg?branch=master&service=github)](https://coveralls.io/github/rezometz/django-paiji2-forum?branch=master) |
