from uuid import UUID
from fastapi import APIRouter
from geojson import MultiPolygon, Feature, dumps, FeatureCollection

from config import settings
from api.models import PublicSpaceIn, PublicSpace
from api.utils.mongo import get_or_404, get_all_or_404

# TODO: proper config
SEARCH_RADIUS = 25

router = APIRouter(prefix='/places')


@router.get('/{lat}/{lon}')
async def list_places(lat: float, lon: float):
    """List all places within a specified latitude and longitude."""
    places = await get_all_or_404(PublicSpace.objects(
        bounds__near=[lon, lat], bounds__max_distance=settings.place_search_radius))
    geojson_places = []
    for place in places:
        # Iterate and convert to GeoJSON
        geojson_places.append(
            Feature(geometry=place['bounds'], properties={
                "name": place['name'],
                "type": place['type']
            })
        )
    return FeatureCollection(geojson_places)


@router.post('/')
async def create_place(place: PublicSpaceIn):
    """Create a new place with given boundary."""
    rec = PublicSpace(
        name=place.name,
        type=place.type,
        bounds=place.bounds,
    )
    rec.save()
    return rec.to_mongo()


@router.get('/{place_id}')
async def get_place(place_id: UUID):
    """Gets the place with the given ID"""
    place = await get_or_404(PublicSpace.objects(
        id=place_id
    ))
    return place.to_mongo()


@router.delete('/{place_id}', status_code=204)
async def delete_place(place_id: UUID):
    """Deletes the place with the given ID"""
    place = await get_or_404(PublicSpace.objects(
        id=place_id
    ))
    place.delete()
    return 