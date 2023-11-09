
from django.urls import path 
from .import views
from .views import profile







urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  path('profile/', views.profile, name='users-profile'),
]
