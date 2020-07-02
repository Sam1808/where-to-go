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

class Image(models.Model):
    image = models.ImageField("Картинка")
    description_short = models.TextField("Описание картинки", )
    place = models.ForeignKey(Place, verbose_name='Картинка локации', on_delete=models.CASCADE,
                             related_name='place_images', blank = True, null=True)

    def __str__(self):
        return f'{self.id} {self.place}'