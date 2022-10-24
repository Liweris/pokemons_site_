from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class NewsDB(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    img = models.ImageField(upload_to='myapp/img/news')
    date = models.DateTimeField(default=timezone.now)

class ProfileDB(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade_book = models.IntegerField()
    patronymic = models.CharField(max_length=100)
    date = models.DateField()
    sex = models.CharField(max_length=3)
    characters = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    img = models.ImageField(upload_to='myapp/img/users')

"""@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileDB.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()"""


class SchedulsDB(models.Model):
    date = models.DateField()
    number = models.IntegerField()
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    time = models.TimeField()
    id_user = models.IntegerField()
    auditorium = models.CharField(max_length=10)
    group = models.CharField(max_length=10)

class LattersToRector(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=500)
    username = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    confirmation = models.BooleanField(default=False)