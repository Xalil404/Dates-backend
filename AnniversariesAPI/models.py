from django.db import models

# Create your models here.

class Anniversary(models.Model):
    name = models.CharField(max_length=100)
    anniversary_date = models.DateField()

    def __str__(self):
        return self.name
