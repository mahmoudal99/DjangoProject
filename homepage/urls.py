from django.urls import path
from homepage.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]
