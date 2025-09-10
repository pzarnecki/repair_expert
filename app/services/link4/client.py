# app/services/link4/client.py

from .endpoints.prepare_calculation import prepare_calculation
from .endpoints.calculate import calculate

class Link4Client:
    def __init__(self, partner_id: str):
        self.partner_id = partner_id

    def prepare(self, calculation_id, start_date, license_plate, insurance_formula):
        return prepare_calculation(
            calculation_id=calculation_id,
            start_date=start_date,
            license_plate=license_plate,
            insurance_formula=insurance_formula,
            partner_id=self.partner_id
        )

    def calculate(self, calculation_id):
        return calculate(
            calculation_id=calculation_id,
            partner_id=self.partner_id
        )