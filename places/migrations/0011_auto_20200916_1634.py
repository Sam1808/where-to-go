# Generated by Django 3.0.7 on 2020-09-16 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_auto_20200826_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='short_image_description',
            new_name='short_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='long_place_description',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='short_place_description',
            new_name='short_description',
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.Place', verbose_name='Картинка локации'),
        ),
    ]