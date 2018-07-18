# PythonPractice
Python and Django code samples from udemy courses

# Intro
basics of Python
* strings
* arrays
* loops
* classes
* functions
* etc

# WordCount
App to count appearences of a word in a given text input. Multiple pages, python + html

# Portfolio
App to showoff myself. Bootstrap styling, multiple pages/multple apps, postgres database, etc. 
-- virtual environments -- how apps work -- add models view to an app -- work with Media files, static files, urls, etc

# Common commands to know
* pip install virtualenv
* django-admin startproject ProjectName
* django-admin startapp AppName
* python manage.py runserver

* Virtual Environment
    * Start : myvenv\Scripts\activate.bat

* Migrations -- get database stuffs organized based on models
    * python manage.py makemigrations
    * python manage.py migrate

* Create a superuser for db access
    * python manage.py createsuperuser

* Model Creation Steps!
    * Create a new model
    * Add the new model app to the settings
    * Create a migration
    * Migrate
    * Add to the admin page 

* Cool things!::
    * Add these lines in your model to show pretty text in the Django admin page!
        * def __str__(self):
        * return self.title


# Things to do before committing
* settings.py
    * remove the SECRET_KEY
    * Set debug = False signifying production mode


