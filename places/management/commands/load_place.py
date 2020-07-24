import requests
import os
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

        # Create location object
        location, created = Place.objects.get_or_create(
            title=json_data['title'],
            description_short=json_data['description_short'],
            description_long=json_data['description_long'],
            lng=json_data['coordinates']['lng'],
            lat=json_data['coordinates']['lat'],
        )
        if created:
            # Get location images
            media_folder = settings.MEDIA_ROOT
            image_urls_catalog = json_data['imgs']
            for image_url in image_urls_catalog:
                image_name = image_url.split('/')[-1]
                image_path = os.path.join(media_folder, image_name)
                response = requests.get(image_url)
                with open(image_path, 'wb') as file:
                    file.write(response.content)
                picture, created = Image.objects.get_or_create(
                    image=image_name,
                    place=location,
                    )
            print(f'Created location: {location}')
