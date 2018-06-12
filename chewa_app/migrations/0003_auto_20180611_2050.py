# Generated by Django 2.0 on 2018-06-11 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chewa_app', '0002_lesson_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='chewa_img/')),
            ],
        ),
        migrations.AlterField(
            model_name='lesson',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chewa_app.Answers'),
        ),
    ]