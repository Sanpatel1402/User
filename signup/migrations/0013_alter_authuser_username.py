# Generated by Django 4.2.3 on 2023-07-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0012_authuser_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
