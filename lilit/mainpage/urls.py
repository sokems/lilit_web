from django.urls import path
from .views import *

urlpatterns = [
    path('', mainpage_index, name='mainpage'),
    path('logout/', logout_index, name='logout'),
]
