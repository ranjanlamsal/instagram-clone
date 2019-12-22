from django.db import models

# Create your models here.

class UserModel(models.Model):
    display_name = models.CharField(max_length=255)
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pic')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username