from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.Lista_Posteos, name='lista'),
    path('Detalle/<int:pk>', views.Detalle_Posteos, name='detalle'),
    path('Comentario/', views.Agregar_Comentario, name = 'comentar'),
]