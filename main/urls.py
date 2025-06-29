from django.urls import path
from .views import main_view


urlpatterns = [
    path('', main_view, name="main"),
    path('home', main_view, name="home"),
    path('login', main_view, name="login"),
    path('login', main_view, name="register"),
]
