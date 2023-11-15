from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UpdateUserForm
from .forms import UpdateProfileForm
from .models import Workspace, Task, Comment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .forms import TaskForm
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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



class WorkspaceCreate(LoginRequiredMixin, CreateView):
  model = Workspace
  fields = ['name', 'description']
  success_url = '/workspaces/'


class WorkspaceUpdate(LoginRequiredMixin, UpdateView):
  model = Workspace
  fields = ['name', 'description']



class WorkspaceDelete(LoginRequiredMixin, DeleteView):
  model = Workspace
  success_url = '/workspaces/'


def home(request):
  return render(request, 'index.html')

@login_required
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


@login_required
def workspaces_index(request):
  workspaces = Workspace.objects.all()
  return render(request, 'workspaces/index.html', {'workspaces': workspaces})

@login_required
def workspaces_detail(request, workspace_id):
  workspace = Workspace.objects.get(id =workspace_id)
  task_form = TaskForm()
  return render(request, 'workspaces/detail.html', {'workspace': workspace, 'task_form':task_form})



# def cats_detail(request, cat_id):
#   #Select * FROM 'main_app_cat' WHERE id = cat_id
#   cat = Cat.objects.get(id=cat_id)
#   feeding_form = FeedingForm()
#   ## Exclude those ids which exist in cat_toys join table with the current cat id
#   toys_cats_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
#   return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form, 'toys':toys_cats_doesnt_have})


class TaskList(LoginRequiredMixin, ListView):
  model = Task

class TaskDetail(LoginRequiredMixin, DetailView):
  model = Task
  
  

# class TaskCreate(CreateView):
#   model = Task
#   fields = ['name', 'description', 'duedate', 'status' ]

@login_required
def add_tasks(request, workspace_id):
  form = TaskForm(request.POST)
  if form.is_valid():
    add_tasks = form.save(commit=False)
    add_tasks.workspace_id = workspace_id
    add_tasks.save()
  return redirect('detail', workspace_id=workspace_id)

# def add_comments(request, task_id):
#   form = TaskForm(request.POST)
#   if form.is_valid():
#     add_comments = form.save(commit=False)
#     add_comments.task_id = task_id
#     add_comments.save()
#   return redirect('tasks_detail', task_id=task_id)

@login_required
def add_comment(request, task_id):

  form = CommentForm(request.POST)
  if request.method == "POST":
    if form.is_valid():
      new_comment = form.save(commit = False)
      new_comment.task_id = task_id
      new_comment.user_id = request.user.id
      new_comment.save()
      return redirect('tasks_detail', pk = task_id)

  form = CommentForm()
  context = {'form': form }
  return render(request, 'main_app/comment_form.html', context)






  # def form_valid(self, form):
  #   workspace_id = self.kwargs['workspace_id']
  #   form.instance.workspace = Workspace.objects.get(id=self.kwargs['workspace_id'])
  #   return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  fields = ['name', 'description', 'duedate', 'status' ]

class TaskDelete(LoginRequiredMixin, DeleteView):
  model = Task
  success_url = '/tasks/'


def assoc_task(request, workspace_id, task_id):
  Workspace.objects.get(id=workspace_id).tasks.add(task_id)
  return redirect('detail', workspace_id=workspace_id)

  
def unassoc_task(request, workspace_id, task_id):
  Workspace.objects.get(id=workspace_id).tasks.remove(task_id)
  return redirect('detail', workspace_id=workspace_id)

class CommentUpdate(LoginRequiredMixin, UpdateView):
  model = Comment
  fields = ['text']

class CommentDelete(LoginRequiredMixin, DeleteView):
  model = Comment
  fields = ['text']
  success_url = '/tasks'

# class CommentCreate(CreateView):
#   model = Comment
#   fields = ['text']
#   success_url = '/tasks/'

#   def form_valid(self, form):
#     form.instance.user = self.request.user
#     form.instance.task_id = self.request.POST.get('task')

#     return super().form_valid(form)
  
