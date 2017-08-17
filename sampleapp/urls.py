from django.conf.urls import url
from sampleapp.views import home

urlpatterns = [
    url(r'^home/$', home, name='home'),
]
