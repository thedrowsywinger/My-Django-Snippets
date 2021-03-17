from django.db import models

# Create your models here.
class DRF_Model(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return str(self.first_name + self.last_name)
