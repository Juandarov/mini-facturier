from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Project

# Create your views here.

def homepage(request):
    return render(request, "homepage.html")


class ProjectList(ListView):
    model = Project
    context_object_name = "projects"

class ProjectDetail(DetailView):
    model = Project

class ProjectCreation():
    pass
