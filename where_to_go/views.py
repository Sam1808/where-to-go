from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from places.models import Place, Image


def show_mainpage(request):    
    places_content = []
    for place in Place.objects.all():
        
        place_description = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
                },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": f'/places/{place.id}'
                }
            }
        places_content.append(place_description)

    frontend_json_source ={
        "type": "FeatureCollection",
        "features": places_content
        }
    return render(request, 'index.html', context={'frontend_json_source': frontend_json_source})

def get_location(request,id):
    place = get_object_or_404(Place, pk=id)
    image_catalog = [
        image_object.image.url for image_object in place.place_images.all()
        ]

    json_answer = {
        "title":place.title,
        "imgs": image_catalog,
        "description_short": place.short_place_description,
        "description_long": place.long_place_description,
        "coordinates":{"lat":place.lat,"lng":place.lng}
    }

    response = JsonResponse(json_answer)
    return response
