from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    role = models.CharField(max_length=50)

User._meta.get_field('groups').related_name = None
User._meta.get_field('user_permissions').related_name = None
User._meta.get_field('groups').remote_field.related_name = 'user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'user_permissions'