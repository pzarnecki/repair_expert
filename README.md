## 🔧 Krótki opis

- Projekt obsługuje kalkulację ubezpieczeń komunikacyjnych z wykorzystaniem zewnętrznego API (Link4).
- Zbudowany w FastAPI, gotowy do integracji z kolejnymi providerami.
- Przechowuje `calculation_id`, datę startu i wynik kalkulacji (składkę) w bazie danych.
- Gotowy do konteneryzacji, wdrożeń i rozbudowy o frontend (np. React).

## 🚀 Jak uruchomić

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

# 🚗 Insurance API – FastAPI (Link4 Integration)

## 📁 Struktura katalogów

Pierwotna struktura zaproponowana przez chata

insurance_api/
├── app/
│   ├── main.py                  # Punkt wejścia aplikacji FastAPI
│   ├── config.py                # Ustawienia projektu (np. base URL, partner ID)
│   ├── api/
│   │   ├── __init__.py
│   │   └── link4.py             # Router i logika endpointów Link4 (np. /calculate)
│   ├── core/
│   │   └── utils.py             # Uniwersalne narzędzia (np. UUID, daty)
│   ├── db/
│   │   └── database.py          # Inicjalizacja silnika i sesji bazy danych
│   ├── models/
│   │   └── calculation.py       # Modele ORM (np. SQLModel do przechowywania kalkulacji)
│   ├── schemas/
│   │   └── calculation.py       # Pydantic: wejście/wyjście dla API (używane w `api/link4.py`)
│   └── services/
│       └── link4/
│           ├── __init__.py
│           ├── client.py                # Główna klasa Link4Client (używana w api/)
│           ├── endpoints/
│           │   ├── prepare_calculation.py
│           │   ├── calculate.py
│           │   └── ...                  # inne metody API Link4
│           └── models/                 # Modele danych specyficzne dla Link4 API (opcjonalnie)
│               ├── request_models.py
│               └── response_models.py
├── requirements.txt             # fastapi, sqlmodel, httpx, uvicorn...
├── Dockerfile
├── docker-compose.yml
└── README.md
i już uszczegółowienie 
app/
├── api/                # Endpointy FastAPI (np. link4, pzu, warta)
├── core/               # Funkcje ogólne, np. utils, logika wspólna
├── db/                 # Połączenie z bazą danych (np. database.py)
├── models/             # Modele SQLModel (np. Calculation)
├── schemas/            # Modele Pydantic do walidacji danych (input/output)
├── services/           # Klienci zewnętrznych API (np. link4_client.py)
├── config.py           # Ustawienia aplikacji (base URL, partner ID itp.)
├── main.py             # Główna aplikacja FastAPI (punkt wejścia)

💡 Do dodania później:
- ✍️ dodam informację, jak uruchomić   `Dockerfile` i `docker-compose.yml`,
- 📘 dokumentację API (FastAPI generuje ją automatycznie pod `/docs`), to się nam przyda jak projekt będzie się rozwijał

client.py
jeden punkt wejścia z poziomu API (client.prepare(...), client.calculate(...))
endpoints/prepare_x.py
czytelność i testowalność każdej metody osobno
models/ (opcjonalnie)
lokalne modele odpowiedzi (np. CalculationResult, Consent, Cover)
services/ z podfolderami
gotowe do skalowania na wielu providerów
