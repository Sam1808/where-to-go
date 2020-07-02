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
            "detailsUrl": None}}
        places_content.append(place_description)
    frontend_json_source ={"type": "FeatureCollection"}
    frontend_json_source["features"] = places_content
    return render(request, 'index.html', context={'frontend_json_source': frontend_json_source})
