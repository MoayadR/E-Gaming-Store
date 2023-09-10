from django.shortcuts import render , redirect
from core.models import Cart , Cart_Item , Product

# Create your views here.
def viewCart(request):
    userCartItems = Cart_Item.objects.filter(cart = Cart.objects.get(user = request.user))
    numberOfItems = userCartItems.count()
    totalPrice = 0
    for item in userCartItems:
        totalPrice += item.product.price
    
    return render(request , 'cart/view-cart.html' , {'userCartItems' : userCartItems , "numberOfItems" : numberOfItems , 'totalPrice': totalPrice} )

def addToCart(request , productID):
    Cart_Item.objects.create(cart = Cart.objects.get(user = request.user) , product = Product.objects.get(id = productID))
    return redirect('viewCart')

def deleteFromCart(request , cartItemID):
    Cart_Item.objects.get(id = cartItemID).delete()
    return redirect('viewCart')