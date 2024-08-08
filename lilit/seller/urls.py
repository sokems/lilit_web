from django.urls import path
from .views import *

urlpatterns = [
    path('', seller_index, name='seller'),
    path('<slug:name_bot>/', name_bot_seller_index, name='shop'),
    path('<slug:name_bot>/managers', managers_seller_index, name='managers'),
    path('<slug:name_bot>/addman', add_managers_seller_index, name='addman'),
    path('<slug:name_bot>/goods', goods_seller_index, name='goods'),
    path('<slug:name_bot>/addgoods', add_goods_seller_index, name='addgoods'),
    path('<slug:name_bot>/communication', communication_seller_index, name='communication'),
    path('<slug:name_bot>/statistic', statistic_seller_index, name='statistic'),
]
