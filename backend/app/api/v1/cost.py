from fastapi import APIRouter
from app.services.cost_service import analyze_cost

router = APIRouter()

@router.get("/cost")

def cost_report():

    return analyze_cost()