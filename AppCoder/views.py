from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario, UserCreationForm, UserRegisterForm, UserEditForm
from django.views.generic import ListView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView









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


def leerProfesores(request):

    profesores = Profesor.objects.all() #trae todos los profesores

    contexto= {"profesores":profesores} 

    return render(request, "AppCoder/leerProfesores.html",contexto)
  
  
def eliminarProfesor(request, profesor_nombre):

      profesor = Profesor.objects.get(nombre=profesor_nombre)
      profesor.delete()
      
      #vuelvo al menú
      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)
  

def editarProfesor(request, profesor_nombre):

      #Recibe el nombre del profesor que vamos a modificar
      profesor = Profesor.objects.get(nombre=profesor_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor.nombre = informacion['nombre']
                  profesor.apellido = informacion['apellido']
                  profesor.email = informacion['email']
                  profesor.profesion = informacion['profesion']

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido , 
            'email':profesor.email, 'profesion':profesor.profesion}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})


class CursoListView(ListView):

      model = Curso 
      context_object_name= "cursos"
      template_name = "AppCoder/curso_lista.html"
      
class CursoDetailView(DetailView):

      model = Curso
      template_name = "AppCoder/curso_detalle.html"
      

class CursoCreateView(CreateView):

      model = Curso
      template_name = "AppCoder/curso_crear.html"
      success_url=reverse_lazy('ListaCursos')
      fields = ['nombre', 'camada']


class CursoUpdateView(UpdateView):

      model = Curso
      template_name = "AppCoder/curso_editar.html"
      success_url=reverse_lazy('ListaCursos')
      fields = ['nombre', 'camada']

class CursoDeleteView(DeleteView):

      model = Curso
      template_name = "AppCoder/curso_borrar.html"
      success_url=reverse_lazy('ListaCursos')
      
      
def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"AppCoder/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"AppCoder/login.html", {'form':form} )
  
  
def register(request):
    mensaje = None

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            mensaje = "Usuario Creado :)"
    else:
        form = UserRegisterForm()

    return render(request, "AppCoder/registro.html", {"form": form, "mensaje": mensaje})


@login_required
def inicio(request):
    
    return render(request, "AppCoder/inicio.html")



@login_required
def editarPerfil(request):

      #Instancia del login
      usuario = request.user
     
      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
            
                  #Datos que se modificarán
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password1']
                  usuario.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={ 'email':usuario.email}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})
  
  
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name= 'AppCoder/cambiar_contrasenia.html'
    success_url = reverse_lazy('EditarPerfil')