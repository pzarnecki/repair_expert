# app/main.py
# demo, z obsługą html
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.api.link4 import router as link4_router

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