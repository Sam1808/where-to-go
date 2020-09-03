import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image
from requests.exceptions import ConnectionError, HTTPError

class Command(BaseCommand):
    help = 'Add location info to database.'

    def add_arguments(self, parser):
        parser.add_argument('location_data')

    def handle(self, *args, **options):
        json_url = options['location_data']

        try: #test connection
            response = requests.get(json_url)
            response.raise_for_status()
        except ConnectionError:
            print('Connection Error')
            exit()
        
        headers = {'Accept': 'application/json'}
        response_status = requests.get(  
            f'https://httpstat.us/{response.status_code}', headers=headers).json() # get description for status code
       

        if response_status['code'] != 200:
            print( f"Error:{response_status['description']}")
            exit()
        

        json_data = response.json()

        if 'error' in json_data: # for crooked sites with errors and code 200
            raise requests.exceptions.HTTPError(json_data['error'])

        location, created = Place.objects.get_or_create(
            title=json_data['title'],
            short_place_description=json_data['description_short'],
            long_place_description=json_data['description_long'],
            lng=json_data['coordinates']['lng'],
            lat=json_data['coordinates']['lat'],
        )
        if created:
            image_urls_catalog = json_data['imgs']
            for image_url in image_urls_catalog:
                image_name = image_url.split('/')[-1]
                response = requests.get(image_url)
                
                response_status= requests.get(
                    f'https://httpstat.us/{response.status_code}', headers=headers).json()

                if response_status['code'] != 200:
                    print(f"Error:{response_status['description']}")
                    # exit() Maybe I will be lucky with the next picture...

                picture, created = Image.objects.get_or_create(
                    image=image_name,
                    place=location,
                    )
                picture.image.save(image_name, ContentFile(response.content))

            print(f'Created location: {location}')
