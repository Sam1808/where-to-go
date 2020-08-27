import requests
import os
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.conf import settings
from places.models import Place, Image

class Command(BaseCommand):
    help = 'Add location info to database.'

    def add_arguments(self, parser):
        parser.add_argument('location_data')

    def handle(self, *args, **options):

        json_url = options['location_data']
        response = requests.get(json_url)
        json_data = response.json()

        location, created = Place.objects.get_or_create(
            title=json_data['title'],
            short_place_description=json_data['description_short'],
            long_place_description=json_data['description_long'],
            lng=json_data['coordinates']['lng'],
            lat=json_data['coordinates']['lat'],
        )
        if created:
            media_folder = settings.MEDIA_ROOT
            image_urls_catalog = json_data['imgs']
            for image_url in image_urls_catalog:
                image_name = image_url.split('/')[-1]
                image_path = os.path.join(media_folder, image_name)
                response = requests.get(image_url)
                picture, created = Image.objects.get_or_create(
                    image=image_name,
                    place=location,
                    )
                picture.image.save(image_path, ContentFile(response.content))

            print(f'Created location: {location}')
