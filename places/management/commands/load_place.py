import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image

class Command(BaseCommand):
    help = 'Add location info to database.'

    def add_arguments(self, parser):
        parser.add_argument('location_data')

    def handle(self, *args, **options):
        json_url = options['location_data']

        response = requests.get(json_url)
        response.raise_for_status()
        
        json_data = response.json()

        if 'error' in json_data: # for crooked sites with errors and code 200
            raise requests.exceptions.HTTPError(json_data['error'])

        location, created = Place.objects.get_or_create(
            title=json_data['title'],
            short_description=json_data['description_short'],
            long_description=json_data['description_long'],
            lng=json_data['coordinates']['lng'],
            lat=json_data['coordinates']['lat'],
        )
        if not created:
            return f'Location "{location}" has already been added.'

        image_urls_catalog = json_data['imgs']
        for image_url in image_urls_catalog:
            image_name = image_url.split('/')[-1]
                
            response = requests.get(image_url)
            response.raise_for_status
                                            
            picture, created = Image.objects.get_or_create(
                image=image_name,
                place=location,
                )
            picture.image.save(image_name, ContentFile(response.content))

        return f'Created location: "{location}"'
