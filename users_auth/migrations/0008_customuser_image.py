# Generated by Django 2.1.4 on 2018-12-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth', '0007_customuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
