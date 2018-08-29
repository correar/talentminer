from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    info_text = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='images/')
    star = models.ImageField(upload_to='images/')

class Achievement(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    achievement = models.CharField(max_length=200)
    point = models.IntegerField(default=0)
    status = models.BooleanField(default=False)