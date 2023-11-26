from django.urls import path
from .views import todo_list, todo_add, update_completion_status

urlpatterns = [
    path('todo_list/', todo_list, name='todo_list'),
    path('todo_add/', todo_add, name='todo_add'),
    path('update_completion_status/', update_completion_status, name='update_completion_status'),
    # Weitere URLs können hier hinzugefügt werden
]