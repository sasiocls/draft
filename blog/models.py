from django.db import models

# Create your models here.
class Registrated(models.Model):
    name = models.CharField(blank=True, max_length=20)
    erfahrung = models.TextField(blank=True)
    junge = models.IntegerField(max_length=3)

    def __str__(self):
        return {}.format(self.name)