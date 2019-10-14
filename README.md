# Django Accounts Example
This is an example app that can be used in a Django project to handle authentication and account creation for users. It contains a custom user model and a profile model which can be customized depending on your project's needs.

I created this with students in mind but more advanced devlelopers may find handy code snippets. It could also work as a hackathon starter.

## Requirements
1. A new (or new-ish) project
2. Empty database (no existing users)
3. Python 3

## Steps
Start by copying this app folder into the project root. To create a new project from scratch try:
```sh
$ django-admin startproject
```
_(will either need to have django installed globally or be in an active virtualenv with django installed)_

Next, rename the folder from 'django-accounts-example-app' to just 'accounts'.

_Side note: I would recommend deleting the .git folder above messing around with submodules. This project is meant to be a baseline to build your own thing off of, not a package._

### in settings.py
Add 'accounts' to INSTALLED_APPS:

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    ...
    'accounts',
]
```
So Django uses the custom user model instead of the default one:
```py
AUTH_USER_MODEL = 'accounts.User'
```
### in urls.py (main app)
Add this to your main url dispatcher (the urls.py in your project's main app):
```py
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('accounts.urls')),
]
```
### in terminal
Run:
```sh
$ python manage.py makemigrations accounts && python manage.py migrate
```
This command will not work (and probably break things) if you already have users in your database.

### in other apps
To use the custom user model in other apps:
```py
from django.contrib.auth import get_user_model
User = get_user_model()
```
# Try it out
This app only add __3 routes__: login, logout, and signup. Any other urls should either be handled by another app in your project or return a 404. Got to http://localhost:8000/accounts/signup/ to create an account, next go to http://localhost:8000/accounts/logout to test the logout functionality, then try signing in again at http://localhost:8000/accounts/login/.

That's it! That's all it does.
