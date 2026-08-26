# Development
This document describes the process for running this application on your local computer.

# Getting started
This web application is powered by Django. :rocket:

It runs on Windows and Linux environments.

You'll need python to run this application check the version in Pipfile.lock. To install Python https://www.python.org/downloads/.

Once you've installed Python (which includes pip package manager), open Terminal and run one of the following:

- git clone git@github.com:Fluffy-J/django_notesapp.git (for SSH clone)
- git clone https://github.com/Fluffy-J/django_notesapp.git (for http clone)

Then proceed to running:

- [ ] cd django_notesapp/
- [ ] pip install pipenv
- [ ] pipenv shell
- [ ] pipenv sync
- [ ] python manage.py runserver

You should now have a running server! Visit localhost:8000 in your browser.

When you're ready to stop your local server, type Ctrl + C in your terminal window.

Note that pipenv sync is a step that typically should only be run once after a clone.

pipenv sync updates the projects Pipfile file's for dependency management. 

# README

For more info about working with this site,[Read the README](./docs/README2.md)
