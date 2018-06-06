from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name

class Level(models.Model):
    is_easy=models.BooleanField()
    is_hard=models.BooleanField()

    def __int__(self):
        return self.is_easy

class Language(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Content(models.Model):
    language=models.ForeignKey(Language, on_delete=models.CASCADE)
    Category=models.CharField(max_length=250)


    def __int__(self):
        return self.language

class Lessons(models.Model):
    Question=models.CharField(max_length=500)
    Answer=models.CharField(max_length=500)
    Language=models.ForeignKey(Language,on_delete=models.CASCADE )
    category=models.ForeignKey(Content,on_delete=models.CASCADE)
    Level=models.ForeignKey(Level ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.category

