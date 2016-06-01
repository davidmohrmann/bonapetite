from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^plantinfo/$', views.collection, name='plantinfo'),
    # url(r'^instance/(?P<id>[-\w]+)/$', views.instance_detail, name='instance_detail'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
