
from django.shortcuts import redirect, render, get_object_or_404
from .models import Cart, CartItem
from store.models import Products

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product  = Products.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product = product, cart_id=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart_id = cart,
        )
        cart_item.save()
    return redirect('cart')

def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Products, id=product_id)
    cart_item = CartItem.objects.get(cart_id=cart, product=product)
    cart_item.delete()
    return redirect('cart')

def decrease_cart(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Products, id=product_id)
    cart_item = CartItem.objects.get(cart_id=cart, product=product)
    if(cart_item.quantity>1):
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items = None):
    
    cart = Cart.objects.filter(cart_id = _cart_id(request))
    cart_items = CartItem.objects.filter(cart_id =cart.first(), is_active=True) if cart else []
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)+0.0
        quantity = cart_item.quantity
    tax = (18*total)/100
    grand_total = total+tax
    context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items' : cart_items,
        'tax':tax,
        'grand_total':grand_total,
    }
    return render(request, 'cart/cart.html', context)