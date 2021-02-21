from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import formu as formuform
from .models import formu
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.models import User
def index(response):
	return render(response, "main/home.html", {})


def info(response):
	return render(response, "main/contacto.html", {})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out")
	return redirect("/")

@allowed_users(allowed_roles=['admin','paciente'])
def form(request):
    if request.method == "POST":
        form = formuform(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.Nombre_Paciente = request.user.first_name
            messages.info(request, "Su reporte se envio correctamente.")
            instance.save()
    else:
        form = formuform()
    return render(request, "main/form.html", {"form":form})

@allowed_users(allowed_roles=['admin','personal'])
def showresults(request):
    nombres=User.objects.all()
    if request.method=="POST":     
        namep=request.POST.get("nombrep")
        fromd=request.POST.get("fromdate")
        tod=request.POST.get("todate")
        searchresults= formu.objects.raw('select id, Sintoma_1, Sintoma_2, Sintoma_3, Sintoma_4, Nombre_Paciente from main_formu where Nombre_Paciente LIKE "%'+str(namep)+'%" AND fecha_de_reporte between "'+fromd+'" and "'+tod+'"' )
        return render(request, "main/showresults.html", {"data":searchresults, "data2":nombres})
    else:
        displaydata=formu.objects.all()
        return render(request, "main/showresults.html", {"data":displaydata, "data2":nombres})

@allowed_users(allowed_roles=['admin','paciente'])
def historial(request):
    nombres=User.objects.all()
    if request.method=="POST":     
        namep=request.user.first_name
        fromd=request.POST.get("fromdate")
        tod=request.POST.get("todate")
        searchresults= formu.objects.raw('select id, Sintoma_1, Sintoma_2, Sintoma_3, Sintoma_4, Nombre_Paciente from main_formu where Nombre_Paciente LIKE "%'+str(namep)+'%" AND fecha_de_reporte between "'+fromd+'" and "'+tod+'"' )
        return render(request, "main/historial.html", {"data":searchresults, "data2":nombres})
    else:
        displaydata=formu.objects.all()
        return render(request, "main/historial.html", {"data":displaydata, "data2":nombres})

# GRAFICOS
def chart(request):
    labels = []
    data = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    data7 = []
    data8 = []
    data9 = []
    data10 = []
    nombres=User.objects.all()

    if request.method=="POST":
        tod=request.POST.get("todatechart")
        fromd=request.POST.get("fromdatechart")
        namep=request.POST.get("nombrepchart")
        queryset = formu.objects.order_by('-id')[:5]
        searchresults= formu.objects.raw('select id, Sintoma_1, Sintoma_2, Sintoma_3, Sintoma_4, Sintoma_5, Sintoma_6, Sintoma_7, Sintoma_8, Sintoma_9, Sintoma_10, Nombre_Paciente from main_formu where Nombre_Paciente LIKE "%'+str(namep)+'%" AND fecha_de_reporte between "'+fromd+'" and "'+tod+'"' )
		
        for i in searchresults:
            timestampStr = i.fecha_de_reporte.strftime("%d-%b-%Y")
            labels.append(timestampStr)
            data.append(i.Sintoma_1)
            data2.append(i.Sintoma_2)
            data3.append(i.Sintoma_3)
            data4.append(i.Sintoma_4)
            data5.append(i.Sintoma_5)
            data6.append(i.Sintoma_6)
            data7.append(i.Sintoma_7)
            data8.append(i.Sintoma_8)
            data9.append(i.Sintoma_9)
            data10.append(i.Sintoma_10)

    return render(request, 'main/chart.html', {
            'labels': labels,
            'data': data,
            'data2': data2,
            'data3': data3,
            'data4': data4,
            'data5': data5,
            'data6': data6,
            'data7': data7,
            'data8': data8,
            'data9': data9,
            'data10': data10,
            'nombres':nombres
        })
    
def reporte(response):
	return render(response, "main/reporte.html", {})
