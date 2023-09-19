from django.urls import path
from . import views

urlpatterns = [
    path('' , views.viewCart , name='viewCart' ),
    path('add/<productID>/' , views.addToCart , name='addToCart' ),
    path('del/<cartItemID>/' , views.deleteFromCart , name='deleteFromCart' ),
    path('update_cart/' , views.updateCart , name='updateCart' ),
]