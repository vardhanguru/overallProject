
from django.urls import path
from overallApp.views import first_view, login_view
urlpatterns = [
    path('first/', first_view, name='first'),
    path('login', login_view, name = 'login')
]
