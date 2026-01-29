import json
import os
from datetime import datetime

def guardar_json(carpeta: str, data: dict):
    os.makedirs(carpeta, exist_ok=True)

    nombre_archivo = datetime.now().strftime("%Y%m%d_%H%M%S_%f") + ".json"
    ruta = os.path.join(carpeta, nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
