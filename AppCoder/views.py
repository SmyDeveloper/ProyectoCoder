from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario





def curso(self):

    curso = Curso(nombre="desarrollo web", camada = "19881")
    curso.save()
    
    documentoDeTexto = f"----->Curso: {curso.nombre} Camada: {curso.camada}"
    
    return HttpResponse(documentoDeTexto)

def inicio(request):

    return render(request, "AppCoder/inicio.html")

def cursos(request):

    return render(request, "AppCoder/cursos.html")

def profesores(request):

    return render(request, "AppCoder/profesores.html")

def estudiantes(request):

    return render(request, "AppCoder/estudiantes.html")

def entregables(request):

    return render(request, "AppCoder/entregables.html")

def cursos(request):
    
    if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  curso = Curso (nombre=informacion['curso'], camada=informacion['camada']) 

                  curso.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

    else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

    return render(request, "AppCoder/cursos.html", {"miFormulario":miFormulario})


def profesorFormulario(request):
    
    if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion = informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

    else: 

            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

    return render(request, "AppCoder/profesorFormulario.html", {"miFormulario":miFormulario})


def busquedaCamada(request):
    
    return render(request, "AppCoder/busquedaCamada.html")

def buscar (request):
    
    if request.GET['camada']:
    
    
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada_icontains=camada)
         
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos, "camada": camada} )
    
    else:
    
        respuesta= "no enviaste datos"
    
    return HttpResponse(respuesta)



