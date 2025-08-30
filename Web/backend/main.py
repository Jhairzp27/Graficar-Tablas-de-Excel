from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import upload, graph, export
import os

app = FastAPI()

# Obtiene la URL del frontend desde las variables de entorno para producción.
# Si no la encuentra, usa la de localhost para desarrollo.
frontend_url = os.environ.get('FRONTEND_URL', 'http://localhost:3000')

origins = [
    frontend_url,
]

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir las rutas del backend
app.include_router(upload.router)
app.include_router(graph.router)
app.include_router(export.router)

@app.get("/")
def root():
    return {"message": "API del Graficador de Excel en funcionamiento 🚀"}
