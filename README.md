# DJHeroku
The example project for the deployment of Django + Celery on the Heroku hosting.
For the article found here:
https://garmoncheg.blogspot.com/2019/02/running-tasks-with-celery-on-heroku.html

# The Stack
1. Web Framework - Python 3/Django https://docs.djangoproject.com
1. Celery https://celery.readthedocs.io/en/latest/index.html

# Install (OSX-specific)

In a terminal window:
1. `git clone https://github.com/garmoncheg/djheroku`
1. `cd djheroku`
1. ````mkvirtualenv --python=`which python3` djheroku```` (Install virtualenvwrapper if you don't have it https://virtualenvwrapper.readthedocs.io/en/latest/)

1. `workon djheroku`
1. `pip install -r requirements.txt`
1. `python manage.py migrate`

# Running celery for debug

`$ celery worker --loglevel=info --beat`

# Running Django server:

`$ ./manage.py runserver 0.0.0.0:8000`