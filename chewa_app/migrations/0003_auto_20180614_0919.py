# Generated by Django 2.0 on 2018-06-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chewa_app', '0002_auto_20180612_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='score',
        ),
        migrations.AddField(
            model_name='lesson',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
