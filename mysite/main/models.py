from django.db import models

from datetime import datetime, date
class formu(models.Model):
        Sintoma_1 = models.IntegerField()
        Sintoma_2 = models.IntegerField()
        Sintoma_3 = models.IntegerField()
        Sintoma_4 = models.IntegerField()
        Sintoma_5 = models.IntegerField()
        Sintoma_6 = models.IntegerField()
        Sintoma_7 = models.IntegerField()
        Sintoma_8 = models.IntegerField()
        Sintoma_9 = models.IntegerField()
        Sintoma_10 = models.IntegerField()
        Nombre_Paciente = models.CharField(max_length = 100)
        fecha_de_reporte= models.DateTimeField(default=datetime.now)

