# Generated by Django 3.2.5 on 2021-10-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_email_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='security_code',
            field=models.CharField(default='931374', max_length=6),
        ),
    ]
