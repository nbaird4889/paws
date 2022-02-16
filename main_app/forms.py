from django.forms import ModelForm
from .models import Visitors

class VisitorsForm(ModelForm):
  class Meta:
    model = Visitors
    fields = ['name', 'date']