from django.shortcuts import render
from .models import Cart , Cart_Item , Payment , Product, Region , Category
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
    category = set(Category.objects.filter(name__contains = 'Steam'))
    if request.user.is_authenticated:
        userCart = Cart.objects.get(user = request.user)
        userCartItems = Cart_Item.objects.filter(cart = userCart)
        numberOfItems = userCartItems.count()
        return render(request , 'core/steamRegion.html' , {"numberOfItems" : numberOfItems , 'userCartItems': userCartItems , 'category' : category })
    return render(request , 'core/steamRegion.html' , {'regions' : category})


def steamCardsPage(request, category_name):
    steamCards = Product.objects.filter(category__name = category_name)
    if request.user.is_authenticated:
        userCart = Cart.objects.get(user = request.user)
        userCartItems = Cart_Item.objects.filter(cart = userCart)
        numberOfItems = userCartItems.count()
        return render(request , 'core/steamCards.html' , {"numberOfItems" : numberOfItems , 'userCartItems': userCartItems , 'steamCards' : steamCards })
    return render(request , 'core/steamCards.html' , {'steamCards' : steamCards})



def valorantRegionPage(request):
    category = set(Category.objects.filter(name__contains = "VP "))
    if request.user.is_authenticated:
        userCart = Cart.objects.get(user = request.user)
        userCartItems = Cart_Item.objects.filter(cart = userCart)
        numberOfItems = userCartItems.count()
        return render(request , 'core/valorantRegions.html' , {"numberOfItems" : numberOfItems , 'userCartItems': userCartItems, 'category':category  })
    return render(request , 'core/valorantRegions.html' , {'regions' : category})

def valorantCurrency(request , category_name):
    valorantVP = Product.objects.filter(category__name = category_name)
    if request.user.is_authenticated:
        userCart = Cart.objects.get(user = request.user)
        userCartItems = Cart_Item.objects.filter(cart = userCart)
        numberOfItems = userCartItems.count()
        return render(request , 'core/valorantCurrency.html' , {"numberOfItems" : numberOfItems , 'userCartItems': userCartItems , 'valorantVP' : valorantVP  })
    return render(request , 'core/valorantCurrency.html' , {'valorantVP' : valorantVP})
    
def categoryVPNPage(request):
    categories = Category.objects.filter(name__contains = 'VPN')
    if request.user.is_authenticated:
        userCart = Cart.objects.get(user = request.user)
        userCartItems = Cart_Item.objects.filter(cart = userCart)
        numberOfItems = userCartItems.count()
        return render(request , 'core/vpnsCategories.html' , {"numberOfItems" : numberOfItems , 'userCartItems': userCartItems , 'categories' : categories })
    return render(request , 'core/vpnsCategories.html' , {'categories' : categories})

def VPNPage(request, category_name):
    products = Product.objects.filter(category__name =category_name)
    if request.user.is_authenticated:
        userCart = Cart.objects.get(user = request.user)
        userCartItems = Cart_Item.objects.filter(cart = userCart)
        numberOfItems = userCartItems.count()
        return render(request , 'core/vpnPage.html' , {"numberOfItems" : numberOfItems , 'userCartItems': userCartItems , 'products' : products })
    return render(request , 'core/vpnPage.html' , {'products' : products})
    