from django.conf.urls import include, url, patterns
from django.contrib import admin
from mister import views


urlpatterns = [
    url(r'^', include('mister.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
]

