from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from django.contrib.auth import get_user_model
User = get_user_model()

@require_http_methods(["POST", "GET"])
def user_signup(request):
    if request.method == "GET":
        return render(request, 'user_form.html', {'action':'signup'})

    username = request.POST['username']
    password = request.POST['password']
    if username and password:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return HttpResponse("Successfully created user: {}. Edit this response or set a redirect in accounts/views.py".format(username))
    else:
        return HttpResponse(403, "Failed to create user: {}. Is the form sending a POST request that includes a username and password?".format(username))

@require_http_methods(["POST", "GET"])
def user_login(request):
    if request.method == "GET":
        return render(request, 'user_form.html', {'action':'login'})

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Login success! Edit this response or set a redirect in accounts/views.py")
    else:
        return HttpResponse("Login failed! Maybe the user was not created properly? Edit this response in accounts/views.py")

@require_http_methods(["POST", "GET"])
def user_logout(request):
    logout(request)
    return HttpResponse("Logged out")