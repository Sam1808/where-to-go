from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from places.models import Place, Image


def show_mainpage(request):
    all_places = Place.objects.all()
    places_content = []
    for place in all_places:
        place_description = {
            "type": "Feature",
            "geometry": {"type": "Point","coordinates": [place.lng, place.lat]},
            "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": f'/places/{place.id}'}}
        places_content.append(place_description)
    frontend_json_source ={"type": "FeatureCollection"}
    frontend_json_source["features"] = places_content
    return render(request, 'index.html', context={'frontend_json_source': frontend_json_source})

def get_location(request,id):
    place = get_object_or_404(Place, pk=id)
    image_catalog=[]
    for image_object in place.place_images.all():
        image_url = f'{settings.MEDIA_URL}{image_object.image.name}'
        image_catalog.append(image_url)
    json_answer = {
        "title":place.title,
        "imgs": image_catalog,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates":{"lat":place.lat,"lng":place.lng}
    }

    response = JsonResponse(json_answer)
    return response