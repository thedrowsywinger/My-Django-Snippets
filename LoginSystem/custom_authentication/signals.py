from django.db.models.signals import pre_save
from django.contrib.auth.models import User
import uuid

def random_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = uuid.uuid4().hex[:30]
pre_save.connect(random_username, sender=User)