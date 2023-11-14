from django.db import models
from django.contrib.auth.models import auth, User
from django.urls import reverse
from django.utils.timezone import timezone
# Create your models here.

STATUS = (
  ('NS','Not Started'),
  ('IP', 'In Progress'),
  ('S', 'Stuck'),
  ('PF', 'Pending Feedback'),
  ('C', 'Completed')
)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  image = models.ImageField(upload_to = 'main_app/static/uploads', default='')
  def __str__(self):
    return self.user.username


class Workspace(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=300)
  # tasks = models.ManyToManyField(Task)
  def __str__(self):
        return f'{self.name} ({self.id})'
    
  def get_absolute_url(self):
        return reverse('detail', kwargs={'wordspace_id': self.id})


class Task(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=300)
  duedate = models.DateField()
  status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
  workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE,default=1)

  def __str__(self):
    return f'{self.name}'

  def get_absolute_url(self):
    return reverse('tasks_detail', kwargs={'pk': self.id})



  def get_absolute_url(self):
    return reverse('detail', kwargs={'workspace_id': self.id})


class Comment(models.Model):
    # task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    text = models.TextField(max_length=500)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text} ({self.id})'