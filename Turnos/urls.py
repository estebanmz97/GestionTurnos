from django.urls import path

from Turnos import views

urlpatterns = [ 
    path('Inicio', views.Inicio, name="Inicio"), 
    path('Tusturnos', views.Tusturnos, name="Tusturnos"),
    path('Contacto', views.Contacto,name="Contacto"),

]
