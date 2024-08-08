from django.urls import path
from .views import *

urlpatterns = [
    path('', manag_index, name='manag'),
    path('<slug:name_bot>/requests', requests_manag_index, name='requests'),
    path('<slug:name_bot>/myrequests', myrequests_manag_index, name='myrequests'),
    path('<slug:name_bot>/goods', goods_manag_index, name='goods'),
    path('<slug:name_bot>/addgoods', add_goods_manag_index, name='addgoods'),
    path('<slug:name_bot>/crm', crm_manag_index, name='crm'),
    path('<slug:name_bot>/communication', communication_manag_index, name='communication'),
    path('update-request/<int:request_id>/', update_request, name='update_request'),
]
