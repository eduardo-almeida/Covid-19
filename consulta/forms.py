from django import forms

from .models import Consulta, Resultado

class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        #fields = ('cliente', 'medico', 'exame', 'data', 'hora', 'status')
        fields = ('medico', 'exame', 'data', 'hora', 'status')

class ResultadoForm(forms.ModelForm):

    class Meta:
        model = Resultado
        #fields = ('cliente', 'medico', 'exame', 'data', 'hora', 'status')
        fields = ('consulta', 'resultado', 'laudo')