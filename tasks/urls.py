from django.urls import path, include
from .views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView
from . import views

urlpatterns = [
    # path('', views.todo_list, name='todo_list'),
    path('', TodoListView.as_view(), name='todo_list'),
    path('todo/create/', TodoCreateView.as_view(), name='todo_create'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name="todo_update"),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name="todo_delete"),
]
