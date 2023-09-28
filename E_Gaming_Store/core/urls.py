from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index') , 
    path('categories/steam/', views.steamRegionPage , name='steamCards') , 
    path('categories/steam/<region_name>', views.steamCardsPage , name='viewRegion') , 
]