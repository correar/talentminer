from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'info_text', 'icon', 'star', )
    '''nome_da_terafa = forms.CharField(max_length=200)
    informação_da_tarefa = forms.CharField(max_length=200)
    icone = forms.ImageField()
    estrela = forms.ImageField()'''