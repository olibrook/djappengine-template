# {{ cookiecutter.project_name }} Readme

{{ cookiecutter.project_name }} was generated using djappengine-template.


## Getting started

1. Create a virtualenv with python 2.7:

    mkvirtualenv {{ cookiecutter.project_name }}
    workon {{ cookiecutter.project_name }}
    pip install Pillow

2. Run buildout:

    python bootstrap.py
    ./bin/buildout

3. Run the app:

    python bootstrap.py
    ./bin/dev_appserver appengine
