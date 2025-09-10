import httpx

def prepare_calculation(calculation_id: str, start_date: str, license_plate: str, insurance_formula: int, partner_id: str):
    url = "https://api.link4.pl/prepareCalculation"
    payload = {
        "partner": partner_id,
        "calculationInit": {
            "calculationIdentifier": calculation_id,
            "startDate": start_date,
            "params": [
                {"name": "vehicle.licensePlate", "value": license_plate},
                {"name": "insuranceFormula", "value": insurance_formula}
            ]
        }
    }
    headers = {"Content-Type": "application/json"}
    response = httpx.post(url, json=payload, timeout=10)
    return response.json()