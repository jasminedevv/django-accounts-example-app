# How to add this app to your project
NOTE: Project under construction

## Requirements
1. A new project
2. Empty database (no existing users)
3. Python 3

## Steps
Start by copying this app folder into the project root. To create a new project from scratch try:
```sh
$ django-admin startproject
```
(will either need to have django installed globally or be in an active virtualenv with django installed)

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
AUTH_USER_MODEL = 'yourapp.User'
```
### in urls.py (main app)
Add this to your main url dispatcher (the urls.py in your project's main app):
```py
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('accounts.urls'),
]
```
### in other apps
To use the custom user model in other apps:
```py
from django.contrib.auth import get_user_model
User = get_user_model()
```
### in terminal
Run:
```sh
$ python manage.py makemigrations accounts && python manage.py migrate
```
This command will not work (and probably break things) if you already have users in your database.
