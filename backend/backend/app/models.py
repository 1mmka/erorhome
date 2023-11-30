from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()










from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    second_name = models.CharField(max_length=150, blank=True, verbose_name='Отчество')
    image = models.ImageField(upload_to='avatar', default='default.jpeg', verbose_name='Фотография')
