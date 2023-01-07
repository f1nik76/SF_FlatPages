from django.contrib import admin
from django.urls import path, include

import NewsPortal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('NewsPortal.urls')),
    path('', include('protect.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
]