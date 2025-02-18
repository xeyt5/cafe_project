from django.shortcuts import render, redirect
from django.core.mail import send_mail
import requests
from django.http import JsonResponse
from django.contrib import messages

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

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def enviar_mensaje(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        email = request.POST.get('email', '')
        mensaje = request.POST.get('mensaje', '')

        try:
            send_mail(
                f"Mensaje de {nombre}",
                mensaje,
                email, 
                ['eldelaguaciel@gmail.com'],  
                fail_silently=False,
            )
            messages.success(request, "Tu mensaje ha sido enviado con éxito.")
        except Exception as e:
            messages.error(request, f"Error al enviar el mensaje: {str(e)}")

        return redirect('index')

    return render(request, 'index.html')

