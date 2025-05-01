from django.shortcuts import render
from store.models import Products

# basic Views start 
def index(request):
    products = Products.objects.all().filter(is_availabel=True)[:3]
    context = {
        'title':'Sirf Cart | Your Online Shop',
        'products': products ,
    }
    return render(request, 'sirfcart/index.html', context)


def about(request):
    context = {'title': 'Sirf Cart | About us'}
    return render(request, 'sirfcart/about.html', context)

def services(request):
    products = Products.objects.all().filter(is_availabel=True)[:3]
    context = {
        'title':'Sirf Cart | Services',
        'products': products ,
    }
    return render(request, 'sirfcart/services.html', context)

def blog(request):
    context = {
        'title': 'Sirf Cart | Blog page'
    }
    return render(request, 'sirfcart/blog.html', context)

def contact(request):
    context = {
        'title': 'Sirf Cart | Contact page'
    }
    return render(request, 'sirfcart/contact.html', context)

def login(request):
    context = {
        'title': 'Sirf Cart | Register page'
    }
    return render(request, 'sirfcart/login.html', context)

def cart(request):
    context = {
        'title': 'Sirf Cart | Cart page'
    }
    return render(request, 'sirfcart/cart.html', context)

def checkout(request):
    context = {
        'title': 'Sirf Cart | Checkout page'
    }
    return render(request, 'sirfcart/checkout.html', context)


# basic views end 