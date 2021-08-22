from uuid import UUID
from fastapi import APIRouter

from api.models import PublicFeedbackIn, PublicFeedback, PublicSpace
from api.utils.mongo import get_or_404, get_all_or_404

router = APIRouter(prefix='/feedback')


@router.get('/{place_id}')
async def get_feedback(place_id: UUID):
    """Get feedback for the specified place"""
    place = await get_or_404(PublicSpace.objects(id=place_id))
    rec = await get_all_or_404(PublicFeedback.objects(place=place))
    return rec


@router.post('/{place_id}')
async def create_feedback(place_id: UUID, feedback: PublicFeedbackIn):
    """Create feedback for the specified place"""
    place = await get_or_404(PublicSpace.objects(id=place_id))
    rec = PublicFeedback(
        place=place,
        **feedback.dict()
    )
    rec.save()
    return rec.to_mongo()

