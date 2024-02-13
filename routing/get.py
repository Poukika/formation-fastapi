from fastapi import APIRouter, Request, HTTPException
import services.get_service as getService
from datas.csv_reader_service import datas

router = APIRouter()


@router.get('/', tags=['home'])
async def welcome()-> str:
    """Return Bienvenue
    """
    return "Bienvenue"

@router.get('/it-works', tags=['home'])
async def it_works()-> str:
    """Return api enable
    """
    return "API is enable"

@router.get('/user/{id:int}/use', tags=['user'])
async def get_use(id: int):
    """Return type de QCM d'un user
    """
    try:
        return getService.get_use(id)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail='Bad Type'
        )

@router.get('/user/{id:int}/subjects', tags=['user'])
async def get_subjects(id: int):
    """Returns les subjects d'un user
    """
    try:
        return getService.get_subjects(id)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail='Bad Type'
        )

@router.get('/user/{id:int}/qcm/{nb_questions:int}', tags=['user'])
async def get_qcm(id: int, nb_questions: int):
    """Retourne un qcm en fonction du nombre de question démandé
    """
    try:
        return getService.get_qcm(id, nb_questions)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail='Bad Type'
        )

@router.get("/login", tags=['autre'])
async def login(request: Request):
    """login endpoint
    """
    return getService.login(request.headers.get('Authorization'))

@router.get("/datas", tags=['autre'])
async def get_datas()-> dict:
    """Données extraite du fichier bdd csv
    """
    return datas