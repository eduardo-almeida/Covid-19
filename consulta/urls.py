from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaConsultas),
    
    path('consulta/<int:id>', views.consultaView, name='consulta-view'),
    path('novaConsulta/', views.novaConsulta, name='nova-consulta'),
    path('editaConsulta/<int:id>', views.editaConsulta, name='edita-consulta'),
    path('deletaConsulta/<int:id>', views.deletaConsulta, name='deleta-consulta'),
    path('sendJson/<int:id>', views.sendJson, name='send-json'),
]
