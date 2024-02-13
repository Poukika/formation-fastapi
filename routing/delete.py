from fastapi import APIRouter
import services.delete_service as deleteService

router = APIRouter()

@router.delete('/user/{id}/delete/subjects', tags=['user'])
async def delete_subjects(id: int)-> dict:
    """Reset sujet d'un user
    """
    if isinstance(id, int):
        return deleteService.delete_subjects(id)

