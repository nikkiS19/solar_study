from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user=models.OneToOneField(User,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
