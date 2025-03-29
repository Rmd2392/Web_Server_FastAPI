# Web_Server_FastAPI
Proyecto desarrollado en Python que implementa un servidor web utilizando FastAPI para la gestión de alumnos de una escuela.

Este proyecto contiene dos partes diferenciadas:

- Una aplicación **interactiva por consola** para gestionar alumnos (añadir, ver, borrar, guardar, cargar).
- Una **API REST** desarrollada con **FastAPI**, que permite gestionar alumnos mediante peticiones HTTP (GET, POST, DELETE).

##  Estructura del proyecto

```
API/
├── alumnes.json          # Archivo donde se guardan los alumnos
├── esquelet.py           # Aplicación de consola (Parte 1)
└── README.md             # Este documento
```

---

##  Parte 1: Aplicación de consola (`esquelet.py`)

### Funcionalidades:

- Mostrar alumnos
- Añadir nuevo alumno (con ID automático)
- Ver alumno por ID
- Borrar alumno por ID
- Guardar alumnos en `alumnes.json`
- Cargar alumnos desde `alumnes.json`

### Formato de los alumnos:

```json
{
  "id": 1,
  "nom": "Anna",
  "cognom": "Martínez",
  "data": { "dia": 12, "mes": 5, "any": 2004 },
  "email": "2024_anna.martinez@iticbcn.cat",
  "feina": false,
  "curs": "DAW1"
}
```
---

## 📚 Objetivo de la práctica

- Trabajar con estructuras de datos (listas, diccionarios).
- Practicar lectura/escritura de archivos JSON.
- Crear una API REST básica.
- Relacionar una aplicación por consola y un servidor web usando el mismo archivo de datos.

---

##  Autor

Práctica realizada por Ricardo Martín Díaz  DAW 1A (CURSO 24/25)

---

##  Notas para el profesor

- El archivo `alumnes.json` contiene datos iniciales con 10 alumnos.
- Todos los campos están generados según el curso (2023/2024).
- El ID no se repite.
- El código está comentado para facilitar su corrección y comprensión.
