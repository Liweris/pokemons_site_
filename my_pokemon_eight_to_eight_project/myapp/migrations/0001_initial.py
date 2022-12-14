# Generated by Django 4.1 on 2022-10-23 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LattersToRector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(max_length=350)),
                ('username', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('content', models.TextField()),
                ('shortcontent', models.TextField(max_length=70)),
                ('img', models.ImageField(upload_to='myapp/img/news')),
                ('teg', models.CharField(max_length=20)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SchedulsDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('number', models.IntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('id_user', models.IntegerField()),
                ('auditorium', models.CharField(max_length=10)),
                ('group', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_book', models.IntegerField()),
                ('patronymic', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('sex', models.CharField(max_length=3)),
                ('characters', models.CharField(max_length=3)),
                ('phone_number', models.IntegerField()),
                ('img', models.ImageField(upload_to='myapp/img/users')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
