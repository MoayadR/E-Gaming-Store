from django.urls import path
from . import views

urlpatterns = [
    path('' , views.viewCart , name='viewCart' ),
    path('update-cart/' , views.updateCart , name='updateCart' ),
]