from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index') , 
    path('categories/steam/', views.steamRegionPage , name='steamCards') , 
    path('categories/steam/<category_name>', views.steamCardsPage , name='viewRegion') , 
    path('categories/valorant/', views.valorantRegionPage , name='valorantRegions') , 
    path('categories/valorant/<category_name>', views.valorantCurrency , name='valorantCurrency') , 
    path('categories/VPN/', views.categoryVPNPage , name='vpnCategories') , 
    path('categories/VPN/<category_name>', views.VPNPage , name='vpnPage') , 
]