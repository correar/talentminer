from django import forms
from .models import Task, Achievement

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'info_text', 'icon', 'star', )

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ('achievement', 'point')
