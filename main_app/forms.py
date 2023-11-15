from django import forms
from django.contrib.auth.models import User
from .models import Profile,Task, Comment
from django.forms import ModelForm



class UpdateUserForm(forms.ModelForm):
  username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

  email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))


  class Meta:
    model = User
    fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
  model = Profile
  first_name = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

  last_name = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

  image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

  class Meta:
    model = Profile
    fields = ['first_name', 'last_name', 'image']
    


class TaskForm(ModelForm):
  class Meta: 
    model = Task
    fields = ['name', 'description','duedate','status']



class CommentForm(ModelForm):
  class Meta: 
    model = Comment
    fields = ['text']


