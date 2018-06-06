from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.

class Profile (models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.name

class language (models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Content (models.Model):
    language = models.CharField(max_length=60)
    category = models.CharField(max_length=60)

    def __str__(self):
        return self.language

    def save_Content(self):
        self.save()

    def delete_Content(self):
        self.delete()

    @classmethod
    def content_details(cls):
        details = cls.objects.all()
        return details

    class Meta:
        ordering = ['language']


class Level (models.Model):
    Easy = models.CharField(max_length=30)
    Hard = models.ForeignKey(User)


class Lessons (models.Model):
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    language = models.IntegerField()
    level = models.IntegerField()
    image = models.ImageField(upload_to = 'chewa_img/',null=True)


    def save_Lesson(self):
        self.save()

    def delete_Lesson(self):
        self.delete()

    @classmethod
    def lesson_details(cls):
        lesson_details = cls.objects.all()
        return lesson_details


    



