
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
]
