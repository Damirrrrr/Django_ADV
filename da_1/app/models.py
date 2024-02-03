from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', "Female"),
        ('U', "Unsure"),
    )
    sex = models.CharField(max_length = 1, choices = SEX_CHOICES)