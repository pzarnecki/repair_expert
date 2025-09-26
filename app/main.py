# app/main.py
# demo, z obsługą html
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
#from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
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

# Montowanie całego katalogu `frontend`
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")


# Główna strona
@app.get("/", response_class=HTMLResponse)
async def serve_index():
    html_path = Path("frontend/index.html")
    return HTMLResponse(content=html_path.read_text(encoding="utf-8"))

# Strona wyników kalkulacji
@app.post("/kalkulacja", response_class=HTMLResponse)
async def handle_kalkulacja(
    first_name: str = Form(...),
    last_name: str = Form(...),
    license_plate: str = Form(...),
    car_make: str = Form(...),
    car_model: str = Form(...),
    car_year: int = Form(...),
    start_date: str = Form(...),
    insurance_formula: int = Form(...)
):
    html_path = Path("frontend/kalkulacja.html")
    return HTMLResponse(content=html_path.read_text(encoding="utf-8"))

# Nowa strona kalkulatora - formularza (formularz_do pracy.html)
@app.get("/formularz", response_class=HTMLResponse)
async def serve_formularz():
    html_path = Path("frontend/formularz.html")
    return HTMLResponse(content=html_path.read_text(), status_code=200)

# Routing API
app.include_router(link4_router, prefix="/api/link4", tags=["Link4"])




'''
app = FastAPI(title="Insurance API")

# ✅ Tu dodaj CORS (dla działania formularza HTML lokalnie)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # możesz podać konkretną domenę np. ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mountowanie frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/", response_class=HTMLResponse)
def serve_form():
    html_path = Path(__file__).parent.parent / "frontend" / "index.html"
    return HTMLResponse(content=html_path.read_text(), status_code=200)

# API
app.include_router(link4_router, prefix="/api/link4", tags=["Link4"])
'''
'''
#wersja pierwotna sprzed dema

#from fastapi.middleware.cors import CORSMiddleware - potrzebne jakby w osobnym miejscu stała strona a w osobnym backendf
from fastapi import FastAPI
from app.api.link4 import router as link4_router

app = FastAPI(title="Insurance API")

app.include_router(link4_router, prefix="/api/link4", tags=["Link4"])

@app.get("/")
def root():
    return {"Hey hey": "API dziala "}

'''