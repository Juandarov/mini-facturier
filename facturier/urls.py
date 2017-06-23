from django.conf.urls import url
from .views import *

from views import ProjectList, ProjectDetail, ProjectCreate

urlpatterns = [
    url(r'^create$', ProjectCreate.as_view(), name="project_create"),
    url(r'^list$', ProjectList.as_view(), name='project-list'),
    url(r'^(?P<pk>\d+)/$', ProjectDetail.as_view(), name="project-detail"),
]
