from django.urls import path,include
from .views import *


urlpatterns = [
    path('login/',TokenViewset.as_view()),
]
