# Generated by Django 3.0.8 on 2020-08-03 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='/static/404.jpg', upload_to='posts/'),
        ),
    ]
