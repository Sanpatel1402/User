# Generated by Django 4.2.3 on 2023-07-13 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0011_rename_phone_no_authuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='birth',
            field=models.DateField(null=True),
        ),
    ]