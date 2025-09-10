import httpx

def calculate(calculation_id: str, partner_id: str):
    url = "https://api.link4.pl/calculate"
    payload = {
        "calculationRequest": {
            "calculation": {
                "calculationIdentifier": calculation_id
            }
        },
        "partner": partner_id
    }
    headers = {"Content-Type": "application/json"}
    response = httpx.post(url, json=payload, timeout=10)
    return response.json()