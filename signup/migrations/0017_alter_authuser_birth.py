# Generated by Django 4.2.3 on 2023-07-13 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0016_alter_authuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]