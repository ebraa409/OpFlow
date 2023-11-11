from django.db import models
from django.contrib.auth.models import auth, User
from django.urls import reverse
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

  def get_absolute_url(self):
    return reverse('detail', kwargs={'workspace_id': self.id})


class Task(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=300)
  due_date = models.DateField()
  status = models.CharField(max_length=100, choices=STATUS, default=STATUS[0][0])
  workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.workspace.name} - {self.get_status_display()} on {self.date}'