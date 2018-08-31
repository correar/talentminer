from django import forms
from .models import Task, Achievement

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'info_text', 'icon', 'star', )
        labels = {
            'name':'Nome',
            'info_text': 'Informação',
            'icon':'Icone',
            'star':'Estrela',
        }
        widgets = {
            'name': forms.TextInput(attrs={'maxlength':200}),
            'info_text': forms.TextInput(attrs={'maxlength':200}),
        }

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ('achievement', 'point')
        labels =  {
            'achievement':'Conquista',
            'point':'Pontos',
        }
        widgets = {
            'achievement': forms.TextInput(attrs={'maxlength':200}),
            'point': forms.NumberInput(),
        }
