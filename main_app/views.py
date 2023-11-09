from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UpdateUserForm, UpdateProfileForm
from .models import Workspace
from django.views.generic.edit import CreateView
# Create your views here.


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid Signup', form.error_messages



  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



class WorkspaceCreate(CreateView):
  model = Workspace
  fields = ['name', 'description']
  success_url = '/workspaces/'
















def home(request):
  return render(request, 'index.html')

# @login_required
def profile(request):
  if request.method == 'POST':
    user_form = UpdateUserForm(request.POST, instance=request.user)
    profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, 'Profile updated successfully!')
      return redirect(to='users-profile')
  else:
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)

  return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})



def workspaces_index(request):
  workspaces = Workspace.objects.all()
  return render(request, 'workspaces/index.html', {'workspaces': workspaces})

