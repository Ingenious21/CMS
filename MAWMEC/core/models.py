from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Administrator', 'Administrator'),
        ('Registrar', 'Registrar'),
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Registrar')

    def __str__(self):
        return self.username
