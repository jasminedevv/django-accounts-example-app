# How to add this app to your project
NOTE: Project under construction

## Requirements
1. A new project
2. Empty database (no existing users)
3. Python 3

## Steps
Start by copying this app folder into the project root.

Add 'accounts' to INSTALLED_APPS in settings.py:

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    ...
    'accounts',
]
```

Next, add this to your main app settings:
```py
AUTH_USER_MODEL = 'yourapp.User'
```
Add this to your main url dispatcher (the urls.py in your project's main app):
```py
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('accounts.urls'),
]
```

To use the custom user model in other apps:
```py
from django.contrib.auth import get_user_model
User = get_user_model()
```

Run:
```sh
$ python manage.py makemigrations accounts && python manage.py migrate
```
This command will not work (and probably break things) if you already have users in your database.

## Troubleshooting
### 1.TemplateDoesNotExist
Either move `user_form.html` to wherever your other templates are (usually a folder called 'templates' in the project root) OR tell django to look for templates in app folders. Like this:
```py
# root settings.py
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
```
If that doesn't work make sure you added 'accounts' to your installed apps.