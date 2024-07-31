import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

# Rango de cédulas
start_cedula = 11000000
end_cedula = 12000000

# URL base
base_url = "https://tvtcrhau2vo336qa5r66p3bygy0hazyk.lambda-url.us-east-1.on.aws/?cedula=V{}"

# Crear la carpeta 'actas' si no existe
if not os.path.exists("actas"):
    os.makedirs("actas")

# Lista para almacenar los resultados
results = []
found_acts = set()


def fetch_data(cedula):
    url = base_url.format(cedula)
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if "url" in data:
                image_url = data["url"]
                image_response = requests.get(image_url)
                image_name = image_url.split("/")[-1]
                if image_response.status_code == 200:
                    if image_name in found_acts:
                        return {"cedula": cedula, "url": image_url, "status": "Already downloaded"}
                    image_path = os.path.join("actas", image_name)
                    found_acts.add(image_name)
                    with open(image_path, "wb") as f:
                        f.write(image_response.content)
                    return {"cedula": cedula, "url": image_url, "status": "Downloaded"}
                else:
                    return {
                        "cedula": cedula,
                        "url": image_url,
                        "status": f"Image download failed: HTTP {image_response.status_code}",
                    }
        except json.JSONDecodeError:
            return {"cedula": cedula, "error": "Invalid JSON response"}
    else:
        return {"cedula": cedula, "error": f"HTTP {response.status_code}"}


if __name__ == "__main__":
    # Usar ThreadPoolExecutor para realizar solicitudes en paralelo
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(fetch_data, cedula) for cedula in range(start_cedula, end_cedula + 1)
        ]

        for future in as_completed(futures):
            result = future.result()
            print(result)
            if result:
                results.append(result)

    # Guardar los resultados en un archivo JSON
    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)
