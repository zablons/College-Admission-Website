from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    mobile_no = models.CharField(max_length=100, blank=True)
    adm_no = models.CharField(max_length=100, blank=True)
    user_level = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile' 


