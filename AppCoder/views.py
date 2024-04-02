from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

def curso(self):

    curso = Curso(nombre="desarrollo web", camada = "19881")
    curso.save()
    
    documentoDeTexto = f"----->Curso: {curso.nombre} Camada: {curso.camada}"
    
    return HttpResponse(documentoDeTexto)