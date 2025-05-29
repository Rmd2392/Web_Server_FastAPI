from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

# Inicializamos la aplicación FastAPI
app = FastAPI()

# Ruta del archivo donde se guardan los alumnos
nom_fitxer = "alumnes.json"

# -------------------------------
# Definimos el modelo de dataNaixement y Alumne con Pydantic (BaseModel)
# -------------------------------
class DataNaixement(BaseModel):
    dia: int
    mes: int
    any: int
class Alumne(BaseModel):
    nom: str
    cognom: str
    data: DataNaixement
    email: str
    feina: bool
    curs: str

# -------------------------------
# Funciones de utilitad
# -------------------------------

# Leer alumnos desde el fichero
def llegir_alumnes():
    if os.path.exists(nom_fitxer):
        with open(nom_fitxer, "r", encoding="utf-8") as f:
            alumnes.clear()
            alumnes.extend(json.load(f))
    return alumnes

# Guardar alumnos en el fichero
def guardar_alumnes(alumnes):
    with open(nom_fitxer, "w", encoding="utf-8") as f:
        json.dump(alumnes, f, indent=4, ensure_ascii=False)

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
    alumnes = llegir_alumnes()
    return {"total": len(alumnes)}

# 3. GET /id/{id}  Ver un alumno por ID
@app.get("/id/{id_alumne}")
def veure_alumne(id_alumne: int):
    alumnes = llegir_alumnes()
    for alumne in alumnes:
        if alumne["id"] == id_alumne:
            return alumne
    raise HTTPException(status_code=404, detail="Alumne no trobat")

# 4. DELETE /del/{id}  Eliminar un alumno por ID
@app.delete("/del/{id_alumne}")
def esborrar_alumne(id_alumne: int):
    alumnes = llegir_alumnes()
    for i in range(len(alumnes)):
        if alumnes[i]["id"] == id_alumne:
            alumnes.pop(i)
            guardar_alumnes(alumnes)
            return {"missatge": "Alumne esborrat correctament"}
    raise HTTPException(status_code=404, detail="Alumne no trobat")

# 5. POST /alumne/  Añadir un nuevo alumno
@app.post("/alumne/")
def afegir_alumne(nou_alumne: Alumne):  # Usamos BaseModel aquí
    alumnes = llegir_alumnes()
    if alumnes:
        nou_id = max(alumne["id"] for alumne in alumnes) + 1
    else:
        nou_id = 1
    alumne_dict = nou_alumne.dict()  # Convertimos el modelo a dict
    alumne_dict["id"] = nou_id
    alumnes.append(alumne_dict)
    guardar_alumnes(alumnes)
    return {"missatge": "Alumne afegit correctament", "id": nou_id}