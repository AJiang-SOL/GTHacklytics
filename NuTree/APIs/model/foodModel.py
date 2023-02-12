from django.db import models

class Food(models.Model):
    food = models.FileField()