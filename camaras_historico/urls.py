
from django.conf.urls import url, include
from django.urls import path, re_path
from camaras_historico import views
view = views
urlpatterns = [
    
    path('insertar', views.insertar),
    path('todos', views.todos),
    path('editar/<str:id>/', views.editar),
    path('actualizar/<str:id>/', views.actualizar),
    path('eliminar/<str:id>/', views.eliminar)


]
