from django.urls import path
from . import views

app_name = 'app_gym'

urlpatterns = [
    path('', views.listar_miembros, name='listar_miembros'),
    path('miembro/<int:id_miembro>/', views.detalle_miembro, name='detalle_miembro'),
    path('crear/', views.crear_miembro, name='crear_miembro'),
    path('editar/<int:id_miembro>/', views.editar_miembro, name='editar_miembro'),
    path('borrar/<int:id_miembro>/', views.borrar_miembro, name='borrar_miembro'),
]