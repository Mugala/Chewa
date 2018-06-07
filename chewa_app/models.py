from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name
        
BOOL_CHOICES = ((True, 'Easy'), (False, 'Hard'))
class Easy(models.Model):
    easy_or_hard = models.BooleanField(max_length=100,choices=BOOL_CHOICES)

    def __str__(self):
        return str(self.easy_or_hard)

class Language(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Content(models.Model):
    language=models.ForeignKey(Language, on_delete=models.CASCADE)
    Category=models.CharField(max_length=250)


    def __str__(self):
        return self.Category

class Lessons(models.Model):
    Question=models.CharField(max_length=500)
    Answer=models.CharField(max_length=500)
    Language=models.ForeignKey(Language,on_delete=models.CASCADE )
    category=models.ForeignKey(Content,on_delete=models.CASCADE)
    Level=models.ForeignKey(Easy ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Question

