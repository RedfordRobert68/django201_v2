# Generated by Django 4.1.4 on 2023-10-14 18:02

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_image_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default='/media/profiles/default_bg.jpg', upload_to='profiles'),
        ),
    ]
