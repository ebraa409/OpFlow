from django.contrib import admin
from .models import Profile
from .models import Workspace
from .models import Task
from .models import Comment

# Register your models here.

admin.site.register(Profile)
admin.site.register(Workspace)
admin.site.register(Task)
admin.site.register(Comment)
