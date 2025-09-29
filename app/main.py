# app/main.py
# demo, z obsługą html
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
#from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse, RedirectResponse
from app.api.link4 import router as link4_router
from pathlib import Path

app = FastAPI(title="Aplikacja ubezpieczeniowa - wersja rozwojowa")

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # można wpisać konkretną domenę jak ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# # Montowanie całego katalogu `frontend`
# app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")


# Główna strona
@app.get("/", response_class=HTMLResponse)
async def serve_index():
    html_path = Path("frontend/index.html")
    return HTMLResponse(content=html_path.read_text(encoding="utf-8"))

# Strona wyników kalkulacji

@app.post("/oferta")
async def handle_oferta(
    ac: str = Form(None),
    assist: str = Form(None),
    c1: str = Form(None),
    c2: str = Form(None),
    c3: str = Form(None),
    dob: str = Form(...),  # np. data urodzenia
    email: str = Form(...),
    first_reg: str = Form(...),
    leasing: str = Form(None),
    mileage: str = Form(...),
    more_offers: str = Form(None),
    nnw: str = Form(None),
    oc: str = Form(None),
    owners_count: str = Form(...),
    phone: str = Form(...),
    plate: str = Form(...),
    reg_place: str = Form(...),
    start_date: str = Form(...),
    use: str = Form(...),
    vehicle: str = Form(...),
    vehicle_catalog: str = Form(None),
    young_drivers: str = Form(None)
):


    # first_name: str = Form(...),
    # last_name: str = Form(...),
    # license_plate: str = Form(...),
    # car_make: str = Form(...),
    # car_model: str = Form(...),
    # car_year: int = Form(...),
    # start_date: str = Form(...),
    # insurance_formula: int = Form(...)

    # na razie ignorujemy dane z formularza (demo)
    return RedirectResponse(
        url="/oferty-ubezpieczeniowe/index.html",  # <-- wybierz właściwy katalog
        status_code=303
    )

# UWAGA: mount na końcu, żeby nie przykrył /oferta
#app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")



# Nowa strona kalkulatora - formularza (formularz_do pracy.html)
@app.get("/formularz", response_class=HTMLResponse)
async def serve_formularz():
    html_path = Path("frontend/formularz.html")
    return HTMLResponse(content=html_path.read_text(), status_code=200)

#
#Montowanie całego katalogu `frontend`
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
#Routing API
app.include_router(link4_router, prefix="/api/link4", tags=["Link4"])




