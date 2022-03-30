from django.shortcuts import render, HttpResponse
from django.http import HttpResponse


def Inicio(request):
    return render (request,"Inicio.html")

def Tusturnos(request):
    return render (request,"Tusturnos.html")

def Contacto(request):
    return render (request,"Contacto.html")
