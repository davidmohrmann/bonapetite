from django.conf.urls import include, url, patterns
from django.contrib import admin
from mister import views


urlpatterns = [
    url(r'^', include('mister.urls')),
]

