from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index') , 
    path('categories/steam/', views.steamCardsPage , name='steamCards') , 
]