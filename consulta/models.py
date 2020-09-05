from django.db import models
from django.contrib.auth import get_user_model

#cliente = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Medico(models.Model):
	nome = models.CharField( max_length=100)
	telefone = models.CharField(max_length=9,blank=True)

	class Meta:
		verbose_name = 'Médico'
		verbose_name_plural = 'Médicos'

	def __str__(self):
		return self.nome

class Exame(models.Model):
    nome = models.CharField( max_length=100)
    descricao = models.TextField(null=True,blank=True)
    
    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'

    def __str__(self):
        return self.nome


class Consulta(models.Model):
    cliente = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    exame = models.ForeignKey(Exame, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=False, null=True)
    hora = models.TimeField(auto_now_add=False, null=True)
    statu = (
		('A', 'Agendado'),
		('E', 'Andamento'),
		('C', 'Concluido'),
		)
    status = models.CharField('Status', max_length=1, choices=statu, null=True,blank=True)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
    

class Resultado(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=100,null=True, blank=True)
    laudo = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Resultado'
        verbose_name_plural = 'Resultados'

    def __str__(self):
        return self.resultado