from fastapi import APIRouter
from .service import get_depression
from .schema import DepressionRequest


router = APIRouter()

@router.post('/depression', tags=["Depression"])
def assess_depression(data: DepressionRequest):
    return get_depression()

@router.get('/info', tags=["Depression"])
def info():
    return {"service": "Depression Assessment API", "version":"1.0"}

