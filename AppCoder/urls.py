from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
    path('leerProfesores', views.leerProfesores, name ="LeerProfesores"),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
    
    
    path('cursos/lista', views.CursoListView.as_view(), name='ListaCursos'),
    path('cursos/nuevo', views.CursoCreateView.as_view(), name='NuevoCurso'),
    path('cursos/<pk>', views.CursoDetailView.as_view(), name='DetalleCurso'),
    path('cursos/<pk>/editar', views.CursoUpdateView.as_view(), name='EditarCurso'),
    path('cursos/<pk>/borrar', views.CursoDeleteView.as_view(), name='BorrarCurso'),
    
    
    path('login', views.login_request, name="Login"),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'Logout'),
    path('editarPerfil',views.editarPerfil, name = 'EditarPerfil'),
    path('cambiarContrasenia', views.CambiarContrasenia.as_view(), name="CambiarContrasenia"),
    
   
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)