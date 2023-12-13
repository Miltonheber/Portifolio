from django.shortcuts import render, redirect, get_list_or_404

def home(request):
    contexto = {}
    return render(request, 'home.html', contexto)

def projectos(request):
    
    contexto = {}
    return render(request, 'projectos.html', contexto)
