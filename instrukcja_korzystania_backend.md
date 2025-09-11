🧪 Jak możemy testować backend przez /docs

Na przykład dla endpointu POST /api/link4/calculate:
	1.	Wejdź w http://localhost:8000/docs (czy jak będzie prawdziwy adres - chociaż docelowo będziemy to oczywiście blokować)
	2.	Znajdź sekcję Link4 → POST /api/link4/calculate
	3.	Kliknij przycisk „Try it out”
	4.	Wypełnij dane (np.):

{
  "first_name": "Jan",
  "last_name": "Kowalski",
  "start_date": "2025-09-15",
  "license_plate": "WX12345",
  "car_make": "Toyota",
  "car_model": "Yaris",
  "car_year": 2018,
  "insurance_formula": 11
}


5. Kliknij EXECUTE
Będzie odpowiedź API na żywo:
{
  "calculation_id": "1cbf8f02-8852-4d60-b250-12a6e370bca6",
  "premium": 1378.45
}