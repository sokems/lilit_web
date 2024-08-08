from django.contrib import admin
from django.urls import path, include

import mainpage.views
from mainpage.views import pageNotFound, аccessIsDenied, serverError, requestError

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls')),
    path('guest/', include('guestpage.urls')),
    path('seller/', include('seller.urls')),
    path('manag/', include('manag.urls')),
]

handler404 = pageNotFound
handler403 = аccessIsDenied
handler500 = serverError
handler400 = requestError