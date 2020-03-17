from django.urls import path
from django.contrib.auth.decorators import login_required
from .import views

urlpatterns = [
#helloword is not defined
#resposta: views.helloword
    path('', login_required(views.taskList), name='task-list'),
    path('task/<int:id>', login_required(views.taskView), name="task-view"),
    path('newtask/', login_required(views.newTask), name='new-task'),
    path('changestatus/<int:id>', login_required(views.changeStatus), name="change-status"),
    path('edit/<int:id>', login_required(views.editTask), name='edit-task'),
    path('delete/<int:id>', login_required(views.deleteTask), name='delete-task'),
]
