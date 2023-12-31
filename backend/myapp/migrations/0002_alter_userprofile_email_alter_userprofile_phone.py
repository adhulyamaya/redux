# Generated by Django 4.1.7 on 2023-10-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.PositiveIntegerField(max_length=10, unique=True),
        ),
    ]
