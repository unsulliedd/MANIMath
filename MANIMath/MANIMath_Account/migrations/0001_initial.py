# Generated by Django 4.2.2 on 2023-06-17 19:36

import MANIMath_Account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bio', models.TextField(blank=True, default=None, null=True)),
                ('profile_photo', models.ImageField(blank=True, default='media/img/Default_Profile_Picture.png', null=True, upload_to=MANIMath_Account.models.get_profile_photo_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
    ]
