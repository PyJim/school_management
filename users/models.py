from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# users/models.py

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('admin', 'Administrator'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='admin')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

