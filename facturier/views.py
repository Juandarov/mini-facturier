from django.shortcuts import render, reverse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from form import inlineform

from django.forms import inlineformset_factory

from .models import Project, ProjectLine

# Create your views here.

def homepage(request):
    return render(request, "homepage.html")


class ProjectList(ListView):
    model = Project
    context_object_name = "projects"

class ProjectDetail(DetailView):
    model = Project
    # project_line = ProjectLine.objects.all()
    #
    # def get_data(self, context):
    #
    #     context = {
    #         "model" : Project,
    #         "project_line" : ProjectLine
    #     }
    #
    #     return context


class ProjectUpdate(DetailView):
    model = Project
    # fields = ['status', 'Project_name']
    #
    # def get_success_url(self):
    #     return reverse('profile-detail', kwargs={'slug': self.object.user.username})

class ProjectCreate(CreateView):
    model = Project

    fields = "__all__"

    def lines(self):
        if self.request.POST:
            return inlineform(self.request.POST)
        else:
            return inlineform()

    def form_valid(self, form):
        projectLine = self.lines()
        self.object = form.save()

        if projectLine.is_valid():
            projectLine.instance = self.object
            projectLine.save()

        return super(ProjectCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('project-list')
