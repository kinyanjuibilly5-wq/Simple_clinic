from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=20, choices=[
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
    ], default='patient')

    def __str__(self):
        return self.username
