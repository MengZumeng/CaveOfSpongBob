# Generated by Django 3.2.9 on 2021-12-12 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_aboutblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_top',
            field=models.BooleanField(default=False, verbose_name='置顶'),
        ),
    ]
