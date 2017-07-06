from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^create$', ProjectCreate.as_view(), name="project_create"),
    url(r'^list$', ProjectList.as_view(), name='project-list'),
    url(r'^client_creation$', ClientCreate.as_view(), name="project-client-create"),
    url(r'^client_list$', ClientList.as_view(), name="client-list"),
    url(r'^(?P<pk>\d+)/$', ProjectDetail.as_view(), name="project-detail"),
    url(r'^(?P<pk>\d+)/update/$', ProjectUpdate.as_view(), name="project-update"),
]
