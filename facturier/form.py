from django.forms import inlineformset_factory
from .models import Project, ProjectLine

inlineform = inlineformset_factory(Project, ProjectLine, fields="__all__", extra=1)
