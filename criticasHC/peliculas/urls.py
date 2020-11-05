from django.urls import path
from . import views 
urlpatterns=[
	path('',views.index,name='index'),
	path('criticas/',views.peliculas,name='pelis'),
	path('quienes/',views.quienes,name='quienes'),
	path('inicio/',views.inicio,name='inicio'),
	path('registro/',views.registro,name='registro')
	] 