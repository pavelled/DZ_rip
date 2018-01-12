import os
from django.db import models
from django.contrib.auth.models import User



def avatar_upload_to(instance, filename):
    return os.path.join('uploads', instance.name + os.path.splitext(filename)[1])

class group(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=avatar_upload_to)
# Create your models here.

class Group_user(models.Model):
    group_id = models.ForeignKey(group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

