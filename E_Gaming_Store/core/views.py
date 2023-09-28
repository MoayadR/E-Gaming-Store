from django.shortcuts import render
from .models import Cart , Cart_Item , Payment , Product, Region
from django.db.models import Count

def getBestSellingProducts():
    featured = Payment.objects.values('product').annotate(numOfSold = Count('product')).order_by("-numOfSold")[:6]
    bestSellingItems = []
    for item in featured:
        product = Product.objects.get(id = item['product'])
        bestSellingItems.append(product)

    return bestSellingItems

def index(request):
    bestSellingProducts = getBestSellingProducts()
    
    if request.user.is_authenticated:
        userCart = Cart.objects.get(user = request.user)
        userCartItems = Cart_Item.objects.filter(cart = userCart)
        numberOfItems = userCartItems.count()
        return render(request , 'core/index.html' , {"numberOfItems" : numberOfItems , 'userCartItems': userCartItems , 'bestSellingProducts': bestSellingProducts})
    return render(request , 'core/index.html' , {'bestSellingProducts': bestSellingProducts})

def steamRegionPage(request):
    regions = set(Region.objects.filter(product__category__name = 'Steam'))
    if request.user.is_authenticated:
        userCart = Cart.objects.get(user = request.user)
        userCartItems = Cart_Item.objects.filter(cart = userCart)
        numberOfItems = userCartItems.count()
        return render(request , 'core/steamRegion.html' , {"numberOfItems" : numberOfItems , 'userCartItems': userCartItems , 'regions' : regions })
    return render(request , 'core/index.html' , {'regions' : regions})


def steamCardsPage(request, region_name):
    steamCards = Product.objects.filter(region__name = region_name)
    print(steamCards)
    if request.user.is_authenticated:
        userCart = Cart.objects.get(user = request.user)
        userCartItems = Cart_Item.objects.filter(cart = userCart)
        numberOfItems = userCartItems.count()
        return render(request , 'core/steamCards.html' , {"numberOfItems" : numberOfItems , 'userCartItems': userCartItems , 'steamCards' : steamCards })
    return render(request , 'core/index.html' , {'steamCards' : steamCards})
