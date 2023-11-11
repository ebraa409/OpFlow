from django.contrib import admin
from .models import Profile
from .models import Workspace
from .models import Task
# Register your models here.

admin.site.register(Profile)
admin.site.register(Workspace)
admin.site.register(Task)