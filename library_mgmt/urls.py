from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router= DefaultRouter()

router.register(r'book',BookViewset,basename='book'),
router.register(r'reservation',ReservationViewset,basename='reservation'),
urlpatterns = [
    path('',include(router.urls)),
]
