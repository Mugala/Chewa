from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django import forms
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator



# Create your models here.


class Profile (models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    total_score = models.IntegerField(default=0)
    user=models.OneToOneField(User, on_delete=models.CASCADE)

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

class Answers(models.Model):
    answer=models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'chewa_img/',null=True)


    def __str__(self):
        return self.answer

class Question (models.Model):
    question = models.CharField(max_length=100)

    def __str__(self):
        return self.question

class Level (models.Model):
    level = models.CharField(max_length = 30)

    def __str__(self):
        return self.level

    def save_Level(self):
        self.save()

    def delete_Level(self):
        self.delete()


class Lesson (models.Model):
    question = models.CharField(max_length = 150)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    choice1=models.CharField(max_length=150)
    choice2=models.CharField(max_length=150)
    content=models.ForeignKey(Content,on_delete=models.CASCADE)
    language = models.ForeignKey(Language,on_delete=models.CASCADE, null=True)
    level = models.ForeignKey(Level,on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to = 'chewa_img/',null=True)
    audio = models.FileField(null=True)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])

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
    @classmethod
    def search_word(cls, search_term):
        results=cls.objects.filter(question__icontains=search_term)
        return results

    @classmethod
    def search_answers(cls,search_term):
        ans = cls.objects.filter(question__question__icontains=search_term)
        print(ans)
        return ans



class Score (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    score=models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.score

    @classmethod
    def get_scores(cls):
        score=cls.objects.all()
        return score
