from django.contrib import admin
from .models import Medico, Exame, Consulta, Resultado


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'telefone')
	search_fields = ('nome', 'telefone')

@admin.register(Exame)
class ExameAdmin(admin.ModelAdmin):
	list_display = ('nome', 'descricao')
	search_fields = ('nome', 'descricao')

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
	list_display = ('cliente', 'medico', 'exame', 'data', 'hora', 'status')
	search_fields = ('cliente', 'medico', 'exame', 'data', 'hora', 'status')

@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
	list_display = ('consulta', 'resultado', 'laudo')
	search_fields = ('consulta', 'resultado', 'laudo')	