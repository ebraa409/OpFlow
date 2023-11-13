
from django.urls import path 
from .import views
from .views import profile







urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('profile/', profile, name='users-profile'),
  path('workspaces/', views.workspaces_index, name='index'),
  path('workspaces/<int:workspace_id>', views.workspaces_detail, name='detail'),
  ##Workspace CRUDS:
  path('workspaces/create', views.WorkspaceCreate.as_view(), name='workspaces_create'),
  path('workspaces/<int:pk>/update/', views.WorkspaceUpdate.as_view(), name='workspaces_update'),
  path('workspaces/<int:pk>/delete/', views.WorkspaceDelete.as_view(), name='workspaces_delete'),
  path('workspaces/<int:workspace_id>/add_tasks/', views.TaskCreate.as_view(), name='tasks_create'),


  ## Tasks CRUDS
  # path('tasks/<int:workspace_id>/create/', views.TaskCreate.as_view(), name='tasks_create'),

  path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='tasks_update'),
  path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='tasks_delete'),
  path('tasks/', views.TaskList.as_view(), name='tasks_index'),
  path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='tasks_detail'), 
  ## Assoc:
  path('workspaces/<int:workspace_id>/assoc_task/<int:task_id>/', views.assoc_task, name='assoc_task'),
  
  path('workspaces/<int:workspace_id>/unassoc_task/<int:task_id>/', views.unassoc_task, name='unassoc_task'),

]
