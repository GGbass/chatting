from django.urls import path, include
from . import views

urlpatterns = [
    path("" , views.index, name='task'),
    path("view/<int:id>",views.view,name='task_view'),
    path("edit/<int:id>",views.edit,name='task_edit'),
    path("create/",views.create, name='task_create'),
    path("delete/<int:id>",views.delete,name='task_delete'),
]