# Generated by Django 2.0 on 2018-06-14 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chewa_app', '0002_auto_20180614_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='lesson',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chewa_app.Question'),
        ),
    ]
