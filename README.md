This is a Django project template with my preferred structure. It's currently set to use Django 1.9. You can use other versions of Django, but some changes to settings and other files may be needed.

## Features
* **Apps** folder to better organize your apps.
* **Utilities** folder for project-wide utilities
* **Settings** have been broken out into 3 files for ease of deployment and source control.

## Set Up Your Virtual Environment
Create your Python virtual environment and activate it. For more information on virtual environments, check out: https://virtualenvwrapper.readthedocs.io/en/latest/

## Install Django 1.9
``pip install django==1.9``

## Start Your Project

To start a new project with this template, run:

``django-admin.py startproject --template=https://github.com/codyparker/django-project-template-cp/zipball/master your_project_name``

## Django Secret Key

Django requires a secret key in the settings file. This template expects an environment variable of DJANGO_SECRET_KEY to run. You can generate a good one here: http://www.miniwebtool.com/django-secret-key-generator/

Once you have one, you can add it to the environment variables in Linux/Mac with ``export DJANGO_SECRET_KEY=your_generated_key``.
If using PyCharm, you can set it in your run configuration or settings to make it easy.

Alternatively, you can replace ``SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')`` in the base_settings.py file with ``SECRET_KEY = your_generated_key``


## Install additional requirements if you like

Other useful apps are already set up in the requirements directory. To install those use:

``pip install requirements/base.txt``

and for development:

``pip install requirements/local.txt``
