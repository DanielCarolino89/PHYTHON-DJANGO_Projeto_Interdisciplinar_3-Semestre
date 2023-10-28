from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def junte(request):
    return render(request, 'junte.html')

def apoio(request):
    return render(request, 'apoio.html')

def parceiros(request):
    return render(request, 'parceiros.html')

def sobre(request):
    return render(request, 'sobre.html')