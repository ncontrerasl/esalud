from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "first_name", "email", "password1", "password2"]
		labels = {
			'first_name': 'Nombre completo ( Nombre Nombre2 Apellido Apellido2 )',
		}
