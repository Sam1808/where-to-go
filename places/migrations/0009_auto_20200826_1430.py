# Generated by Django 3.0.7 on 2020-08-26 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20200826_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='description_short',
            new_name='short_image_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_long',
            new_name='long_place_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_short',
            new_name='short_place_description',
        ),
    ]
