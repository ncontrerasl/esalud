# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy

from django.contrib import messages
# Create your views here.

def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect("/")

	else:
		form = RegisterForm()

	return render(response, "register/register.html",{"form":form})

def PasssChangeView(request):
	if request.method == "POST":
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.info(request, "Contraseña modificada con exito.")
			return redirect("/")
	else:
		form = PasswordChangeForm(user=request.user)
	return render(request, "registration/password_change.html",{"form":form})


