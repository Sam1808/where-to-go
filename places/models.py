from django.db import models

# Create your models here.

class Place(models.Model):
    title = models.CharField("Название", max_length=50)
    description_short = models.TextField("Короткое описание",)
    description_long = models.TextField("Полное описание",)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title