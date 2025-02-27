from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import upload, graph, export

app = FastAPI()

# 🔹 Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir solo React en local
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

# Incluir las rutas del backend
app.include_router(upload.router)
app.include_router(graph.router)
app.include_router(export.router)

@app.get("/")
def root():
    return {"message": "API del Graficador de Excel en funcionamiento 🚀"}
