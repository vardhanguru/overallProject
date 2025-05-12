
from django.urls import path
from secondApp.views import second_view
urlpatterns = [
    path('second/', second_view, name='second')
]
