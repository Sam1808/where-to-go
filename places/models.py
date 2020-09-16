from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    title = models.CharField("Название", max_length=50)
    short_description = models.TextField("Короткое описание", blank=True)
    long_description = HTMLField("Полное описание", blank=True)
    lng = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField("Картинка")
    position = models.PositiveIntegerField("Позиция", default=0, db_index=True)
    short_description = models.TextField("Описание картинки", blank=True)
    place = models.ForeignKey(Place, verbose_name='Картинка локации', on_delete=models.CASCADE,
                             related_name='images')

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place}'
