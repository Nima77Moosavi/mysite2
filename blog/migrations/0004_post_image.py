# Generated by Django 4.2.5 on 2023-10-12 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/feature-img1/jpg', upload_to='blog/'),
        ),
    ]
