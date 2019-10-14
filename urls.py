from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login),
    path('signup/', views.user_signup),
    path('logout/', views.user_logout),
]
