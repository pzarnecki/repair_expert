from pydantic import BaseModel, Field
from datetime import date

class CalculationCreate(BaseModel):
    start_date: date = Field(..., description="Data rozpoczęcia polisy (YYYY-MM-DD)")
    license_plate: str = Field(..., max_length=20, description="Numer rejestracyjny pojazdu")
    insurance_formula: int = Field(..., description="11 = OC, 13 = OC + AC")

class CalculationResponse(BaseModel):
    calculation_id: str = Field(..., description="Identyfikator kalkulacji (UUID)")
    premium: float = Field(..., description="Wyliczona składka OC/AC w zł")




'''
from pydantic import BaseModel
from datetime import date

class CalculationCreate(BaseModel):
    start_date: date
    license_plate: str
    insurance_formula: int

class CalculationResponse(BaseModel):
    calculation_id: str
    premium: float
'''