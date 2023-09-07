from django.shortcuts import render
from .models import Cart , Cart_Item

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        userCart = Cart.objects.get(user = request.user)
        userCartItems = Cart_Item.objects.filter(cart = userCart)
        numberOfItems = userCartItems.count()
        return render(request , 'core/index.html' , {"numberOfItems" : numberOfItems , 'userCartItems': userCartItems})
    return render(request , 'core/index.html')
    