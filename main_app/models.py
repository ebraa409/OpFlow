from django.db import models
from django.contrib.auth.models import auth, User
# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  image = models.ImageField(upload_to = 'main_app/static/uploads', default='')
  def __str__(self):
    return self.user.username