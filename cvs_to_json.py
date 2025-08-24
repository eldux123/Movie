import csv
import json
import re
from datetime import datetime

# Archivos
csv_file = 'movies_initial.csv'
json_file = 'Peliculas/management/commands/movies.json'

# Nombre de tu app y modelo (ajusta si tu app no se llama "Peliculas")
app_name = 'Peliculas'
model_name = 'peliculas'  # en minúscula

data = []

def convertir_runtime(runtime):
    """Convierte '120 min' en 120 (entero)"""
    if isinstance(runtime, str):
        match = re.search(r'(\d+)', runtime)
        if match:
            return int(match.group(1))
    return 0

def convertir_fecha(fecha):
    """Convierte la fecha del CSV (YYYY-MM-DD) a formato compatible con Django"""
    if isinstance(fecha, str) and fecha.strip():
        try:
            return datetime.strptime(fecha, "%Y-%m-%d").date().isoformat()
        except:
            return None
    return None

with open(csv_file, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader, start=1):
        data.append({
            "model": f"{app_name}.{model_name}",
            "pk": i,
            "fields": {
                "titulo": row.get("title", ""),
                "descripcion": row.get("plot", "") or row.get("fullplot", ""),
                "fecha_lanzamiento": convertir_fecha(row.get("released")),
                "genero": row.get("genre", ""),
                "year": int(row.get("year")) if row.get("year") and row.get("year").isdigit() else None,
                "duracion": convertir_runtime(row.get("runtime", "")),
                "calificacion": float(row.get("imdbRating", 0) or 0),
                "image": row.get("poster", ""),
                "url": "",  # No existe en CSV, lo dejamos vacío
            }
        })

# Guardar JSON
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ Archivo {json_file} generado con éxito")
