# {{ cookiecutter.project_name }} Readme

{{ cookiecutter.project_name }} was generated using djappengine-template.


## Getting started

1. Create a virtualenv with python 2.7, if you don't already have one:

        mkvirtualenv {{ cookiecutter.project_name }}
        workon {{ cookiecutter.project_name }}
        pip install Pillow

2. Run buildout:

        python bootstrap.py
        ./bin/buildout

3. Generate a SECRET_KEY for the app and update your settings:

        ./bin/manage.py gen_secret

4. Run the app:

        ./bin/dev_appserver appengine


## Running tests:

        ./bin/manage.py test --settings={{ cookiecutter.project_name }}.settings.test

## Deploying:

        ./bin/appcfg update appengine
