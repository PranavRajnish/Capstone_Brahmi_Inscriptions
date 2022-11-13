from django.urls import path
from . import views


app_name = "basic_app"

urlpatterns = [
	path('', views.index, name="home"),
	path('results/', views.results, name='results'),
    path('info/', views.info, name='info'),
    path('about/', views.about, name='about'),
	]


    