from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django import forms


# Create your models here.

class Profile (models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    score = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name

    def save_Profile(self):
        self.save()

    def delete_Profile(self):
        self.delete()

    @classmethod
    def profile (cls):
        profile_details = cls.objects.all()
        return profile_details


class Language (models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_Language(self):
        self.save()

    def delete_Language(self):
        self.delete()

    @classmethod
    def language (cls):
        language_details = cls.objects.all()
        return language_details


class Content (models.Model):
    language = models.ForeignKey(Language,on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=60)

    def __str__(self):
        return self.category

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
    level = models.CharField(max_length = 30)

    def __str__(self):
        return self.level

    def save_Level(self):
        self.save()

    def delete_Level(self):
        self.delete()


class Lesson (models.Model):
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    choice1=models.CharField(max_length=50)
    choice2=models.CharField(max_length=50)
    content=models.ForeignKey(Content,on_delete=models.CASCADE)
    language = models.ForeignKey(Language,on_delete=models.CASCADE, null=True)
    level = models.ForeignKey(Level,on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to = 'chewa_img/',null=True)
    score = models.ManyToManyField(User, related_name='answer_score', blank=True)

    def __str__(self):
        return self.question

    def save_Lesson(self):
        self.save()

    def delete_Lesson(self):
        self.delete()

    @classmethod
    def lesson_details(cls):
        lesson_details = cls.objects.all()
        return lesson_details

    @classmethod
    def single_lesson(cls,single_category):
        single = cls.objects.filter(content__category__icontains=single_category)
        print(single)
        return single

class Score (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    score=models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.user.name

    @classmethod
    def get_likes(cls):
        score=cls.objects.all()
        return score
