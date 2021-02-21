from django.forms import ModelForm
from .models import formu
from django import forms
from django.forms.widgets import NumberInput
class RangeInput(NumberInput):
    input_type = 'range'

class formu(ModelForm):

	class Meta:
		model = formu
		fields = ["Sintoma_1", "Sintoma_2", "Sintoma_3", "Sintoma_4", "Sintoma_5", "Sintoma_6", "Sintoma_7", "Sintoma_8","Sintoma_9", "Sintoma_10",  ]

		widgets = {
			'Sintoma_1' : RangeInput(attrs={'max': 10,'min':1,'step':1,'value':1,'class':'form-control'}),
			'Sintoma_2' : RangeInput(attrs={'max': 10,'min':1,'step':1,'value':1,'class':'form-control'}),
			'Sintoma_3' : RangeInput(attrs={'max': 10,'min':1,'step':1,'value':1,'class':'form-control'}),
			'Sintoma_4' : RangeInput(attrs={'max': 10,'min':1,'step':1,'value':1,'class':'form-control'}),
			'Sintoma_5' : RangeInput(attrs={'max': 10,'min':1,'step':1,'value':1,'class':'form-control'}),
			'Sintoma_6' : RangeInput(attrs={'max': 10,'min':1,'step':1,'value':1,'class':'form-control'}),
			'Sintoma_7' : RangeInput(attrs={'max': 10,'min':1,'step':1,'value':1,'class':'form-control'}),
			'Sintoma_8' : RangeInput(attrs={'max': 10,'min':1,'step':1,'value':1,'class':'form-control'}),
			'Sintoma_9' : RangeInput(attrs={'max': 10,'min':1,'step':1,'value':1,'class':'form-control'}),
			'Sintoma_10' : RangeInput(attrs={'max': 10,'min':1,'step':1,'value':1,'class':'form-control'}),
		
		}
		labels = {
			'Sintoma_1' : "Dolor ",
			'Sintoma_2' : "Cansancio ",
			'Sintoma_3' : "Nausea ",
			'Sintoma_4' : "Depresion ",
			'Sintoma_5' : "Ansiedad ",
			'Sintoma_6' : "Somnolencia ",
			'Sintoma_7' : "Apetito ",
			'Sintoma_8' : "Maximo bienestar | Maximo malestar ",
			'Sintoma_9' : "Falta de aire ",
			'Sintoma_10' : "Dificultad para dormir ",
   		}