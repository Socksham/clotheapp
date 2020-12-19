from main.views import signup_view
from django.urls import path, include
import main.views as main_views


urlpatterns = [
    path('', main_views.home, name="home"),
    path('signup', main_views.signup_view, name="signup_view"),
]