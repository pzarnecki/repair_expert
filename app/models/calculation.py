from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional

class Calculation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    calculation_id: str
    start_date: date
    license_plate: str
    insurance_formula: int
    premium: Optional[float]