# urls.py
from django.urls import path

from . import views

urlpatterns = [
path("", views.index, name="index"),
path("form/", views.form, name="form"),
path("reporte/", views.reporte, name="info"),
path("info/", views.info, name="info"),
path("logout/", views.logout_request, name="logout"),
path('buscar/',views.showresults, name="buscar"),
path('historial/',views.historial, name="historial"),
path('chart/', views.chart, name='chart'),
]