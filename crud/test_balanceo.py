import time
import requests
from multiprocessing import Pool

# Función que realiza la solicitud HTTP con manejo de excepciones y reintentos
def send_request(i):
    url = "http://localhost:10000"  # Dirección del servidor
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwNzY5MjUyLCJpYXQiOjE3NDA3NjU2NTIsImp0aSI6ImRjYzRiMDgyOWZkZTRkMDBhMjkwMTk3OTQ1ZDZhZGVjIiwidXNlcl9pZCI6MX0.C-9SXqfHHxduRvEv1DQ04ZwjjnLpHfF9YU1kGNs7dRc"}  # Reemplaza "your_token" con tu token real
    retries = 5# Número máximo de reintentos
    while retries > 0:
        try:
            response = requests.get(url, headers=headers)
            # Si la solicitud es exitosa, retornamos el código de estado
            if response.status_code == 200:
                print(f"Request {i}: Success")
                return response.status_code
            else:
                print(f"Request {i}: Failed with status code {response.status_code}")
                return None
        except requests.exceptions.ConnectionError:
            # Si ocurre un error de conexión, decrementamos los reintentos y esperamos
            retries -= 1
            print(f"Request {i}: Connection error, retrying {retries} more times...")
            time.sleep(1)  # Espera 1 segundo antes de intentar de nuevo
    print(f"Request {i}: Failed after multiple retries")
    return None  # Si falla después de los reintentos, retornamos None

if __name__ == "__main__":
    num_requests = 10000  # Número de solicitudes a realizar

    # Usando multiprocessing para enviar múltiples solicitudes
    with Pool(processes=4) as pool:  # Puedes ajustar el número de procesos según tus necesidades
        results = pool.map(send_request, range(num_requests))

    # Mostramos los resultados finales de las solicitudes
    print("Results:", results)
