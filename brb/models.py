from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):
    pass

class Away(models.Model):
    reason = models.CharField(max_length=512, blank=True)
    creation_time = models.DateTimeField(default=now, editable=True)
    return_time = models.DateTimeField(default=now, editable=True)
    phone = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creators")
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk}, {self.return_time}, {self.reason}, {self.active}'
