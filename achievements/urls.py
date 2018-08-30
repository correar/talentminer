from django.urls import path
from . import views
app_name='achievements'
urlpatterns = [
    path('', views.index, name='index'),
    path('createtask/', views.createtask, name="createtask"),
    path('<int:task_id>/createachievement/', views.createachievement, name="createachievement")
]
