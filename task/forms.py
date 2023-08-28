from django.forms import DateInput, ModelForm
from .models import Task
class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ('date',)
        widgets = {
            'estimated_end' : DateInput(attrs={'type':'date'}),
        }