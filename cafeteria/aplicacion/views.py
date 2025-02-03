from django.shortcuts import render
import requests
from django.http import JsonResponse

# Create your views here.
def index(request):
    url = "https://fake-coffee-api.vercel.app/api"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si el código de estado no es 200
        productos = response.json()
    except requests.exceptions.RequestException as e:
        productos = []
        print(f"Error al obtener los productos: {e}")

    return render(request, 'index.html', {"productos": productos})

