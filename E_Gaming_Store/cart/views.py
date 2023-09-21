from django.shortcuts import render , redirect
from core.models import Cart , Cart_Item , Product
from django.http import JsonResponse
import json

# Create your views here.
def viewCart(request):
    userCartItems = Cart_Item.objects.filter(cart = Cart.objects.get(user = request.user))
    numberOfItems = userCartItems.count()
    totalPrice = 0
    for item in userCartItems:
        totalPrice += item.product.price
    
    return render(request , 'cart/view-cart.html' , {'userCartItems' : userCartItems , "numberOfItems" : numberOfItems , 'totalPrice': totalPrice} )


def updateCart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product = data['product']
        cartItem = Cart_Item.objects.create(cart = Cart.objects.get(user = request.user) , product = Product.objects.get(id = product))
        dict = {'productID' : cartItem.id , 'productName' : cartItem.product.name , 'price': cartItem.product.price , 'image' : cartItem.product.image.url}
        return JsonResponse(dict, safe=False)
    
    if request.method == 'DELETE':
        data = json.loads(request.body)
        cartItem = data['cartItem']
        item = Cart_Item.objects.get(id = cartItem)
        price = item.product.price
        item.delete()
        return JsonResponse({'price':price} , safe=False)