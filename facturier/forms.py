from django.forms import inlineformset_factory
from .models import *

ProjectInlineFormset = inlineformset_factory(Project, ProjectLine, fields="__all__", min_num=1, extra=0)
