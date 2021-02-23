from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomProfileModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)
