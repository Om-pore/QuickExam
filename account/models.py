from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # email_address = models.CharField(max_length=50, unique = True, null = True, verbose_name='Email')
    bio = models.TextField(blank = True, null = True)
    profile_img = models.ImageField(upload_to='profile_images', null = True, default='user.png', blank = True, verbose_name='Profile Pic')
    location = models.CharField(max_length=100, blank = True, null = True)

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    gender =   models.CharField(max_length=10, choices = GENDER, blank = True, null = True)

    def __str__(self):
        return self.user.username
    

    # @property
    # def full_name(self):

    #     return f"{self.user.first_name} {self.user.last_name}"