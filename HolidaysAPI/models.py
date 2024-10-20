from django.db import models

# Create your models here.

class Holiday(models.Model):
    name = models.CharField(max_length=100)
    month = models.IntegerField()
    day = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.month}/{self.day}"
