from fastapi import APIRouter
from app.services.security_services import security_scan

router = APIRouter()

@router.get("/security")
def security():

    return security_scan()