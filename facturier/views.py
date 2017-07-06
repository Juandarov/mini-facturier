from django.shortcuts import render, reverse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from .forms import ProjectInlineFormset

from django.forms import inlineformset_factory

from .models import *

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

class ProjectList(ListView):
    model = Project
    context_object_name = "projects"

class ProjectDetail(DetailView):
    model = Project
    def lines(self):
        return ProjectLine.objects.filter(project=self.object)

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['status']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('project-detail', kwargs={'pk': self.object.id})

class ClientCreate(CreateView):
    model = Client
    fields = "__all__"

    def get_success_url(self):
        return reverse('client-list')

class ClientList(ListView):
    model = Client
    context_object_name = "clients"

class ProjectCreate(CreateView):
    model = Project
    fields = "__all__"

    def get_context_data(self):
        context = CreateView.get_context_data(self)
        context["facturier_formset"] = ProjectInlineFormset()
        return context

    def form_valid(self, form):
        facturier_resp = CreateView.form_valid(self, form)
        facturier_formset = ProjectInlineFormset(self.request.POST, instance=self.object)

        if facturier_formset.is_valid():
            facturier_formset.save()

        return facturier_resp

    def get_success_url(self):
        return reverse('project-list')
