from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

# Inicializamos la aplicación FastAPI
app = FastAPI()

# Ruta del archivo donde se guardan los alumnos
nom_fitxer = "alumnes.json"

# Lista que mantiene los alumnos en memoria
alumnes = []

# ID incremental para nuevos alumnos
id_seguent = 1

# -------------------------------
# Definimos el modelo de Alumne con Pydantic
# -------------------------------
class Alumne(BaseModel):
    nom: str
    cognom: str
    data: dict  # Cambiado a dict para simplificar
    email: str
    feina: bool
    curs: str

# -------------------------------
# Funciones de utilitad
# -------------------------------

# Leer alumnos desde el fichero
def carregar_dades():
    global alumnes, id_seguent
    if os.path.exists(nom_fitxer):
        with open(nom_fitxer, "r", encoding="utf-8") as f:
            alumnes.clear()
            alumnes.extend(json.load(f))
            if alumnes:
                id_seguent = max(a["id"] for a in alumnes) + 1
            else:
                id_seguent = 1

# Guardar alumnos en el fichero
def desar_dades():
    with open(nom_fitxer, "w", encoding="utf-8") as f:
        json.dump(alumnes, f, indent=4, ensure_ascii=False)

# Cargar datos al iniciar la aplicación
carregar_dades()

# -------------------------------
# ENDPOINTS API
# -------------------------------

# 1. Mensaje inicial (raíz)
@app.get("/")
def read_root():
    return "Institut TIC de Barcelona"

# 2. GET /alumnes/  Número total de alumnos
@app.get("/alumnes/")
def total_alumnes():
    return {"total_alumnes": len(alumnes)}

# 3. GET /id/{id}  Ver un alumno por ID
@app.get("/id/{id_alumne}")
def veure_alumne(id_alumne: int):
    for alumne in alumnes:
        if alumne["id"] == id_alumne:
            return alumne
    raise HTTPException(status_code=404, detail="Alumne no trobat")

# 4. DELETE /del/{id}  Eliminar un alumno por ID
@app.delete("/del/{id_alumne}")
def esborrar_alumne(id_alumne: int):
    for i in range(len(alumnes)):
        if alumnes[i]["id"] == id_alumne:
            alumnes.pop(i)
            desar_dades()
            return {"missatge": "Alumne esborrat correctament"}
    raise HTTPException(status_code=404, detail="Alumne no trobat")

# 5. POST /alumne/  Añadir un nuevo alumno
@app.post("/alumne/")
def afegir_alumne(nou_alumne: Alumne):  # Usamos BaseModel aquí
    global id_seguent
    alumne_dict = nou_alumne.dict()  # Convertimos el modelo a dict
    alumne_dict["id"] = id_seguent
    id_seguent += 1
    alumnes.append(alumne_dict)
    desar_dades()
    return {"missatge": "Alumne afegit correctament", "id": alumne_dict["id"]}