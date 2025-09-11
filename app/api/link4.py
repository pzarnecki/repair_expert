# wariant pod kalkulację - demo
from fastapi import APIRouter
from app.schemas.calculation import CalculationCreate, CalculationResponse
import uuid
import random

router = APIRouter()

@router.post("/calculate", response_model=CalculationResponse)
def calculate(data: CalculationCreate):
    # Prosta logika demo: składka zależna od roku auta + losowość
    base_premium = 1000
    age_penalty = max(0, (2025 - data.car_year)) * 20
    random_bonus = random.uniform(-100, 150)

    final_premium = base_premium + age_penalty + random_bonus
    final_premium = round(final_premium, 2)

    return CalculationResponse(
        calculation_id=str(uuid.uuid4()),
        premium=final_premium
    )


'''
# app/api/link4.py
# wariant pod api link 5

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from uuid import uuid4

from app.schemas.calculation import CalculationCreate, CalculationResponse
from app.db.database import get_session
from app.models.calculation import Calculation
from app.services.link4.client import Link4Client
from datetime import date

router = APIRouter()
client = Link4Client(partner_id="876")  # testowy partner ID

@router.post("/calculate", response_model=CalculationResponse)
def calculate_insurance(data: CalculationCreate, session: Session = Depends(get_session)):
    calculation_id = str(uuid4())

    # Krok 1: prepareCalculation
    prepare = client.prepare(
        calculation_id=calculation_id,
        start_date=data.start_date.isoformat(),
        license_plate=data.license_plate,
        insurance_formula=data.insurance_formula
    )

    if "errors" in prepare:
        raise HTTPException(status_code=400, detail=prepare["errors"])

    # Krok 2: calculate
    result = client.calculate(calculation_id=calculation_id)

    if "errors" in result:
        raise HTTPException(status_code=400, detail=result["errors"])

    premium = result.get("calculation", {}).get("price", 0.0)

    calc = Calculation(
        calculation_id=calculation_id,
        start_date=data.start_date,
        license_plate=data.license_plate,
        insurance_formula=data.insurance_formula,
        premium=premium
    )
    session.add(calc)
    session.commit()

    return {"calculation_id": calculation_id, "premium": premium}

'''