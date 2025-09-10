# app/api/link4.py

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