from django.urls import path
from .views import *

urlpatterns = [
    path('', guestpage_index, name='guest'),
]
