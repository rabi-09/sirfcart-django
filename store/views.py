from django.shortcuts import get_object_or_404, render
from category.models import Category
from cart.views import _cart_id
from .models import Products
from cart.models import CartItem

# Create your views here.
def index(request, slug=None):
    category = None
    products = None

    if slug != None:
        category = get_object_or_404(Category, category_slug=slug)
        products = Products.objects.all().filter(category=category)
        count = products.count()
    else:
        products = Products.objects.all().filter(is_availabel=True)
        count = products.count()

    context = {
        'title':'Sirf Cart | Shop Now',
        'products': products ,
        'count':count,
    }
    return render(request, 'store/shop.html', context)

def product_details(request, category_slug, product_slug):
    try:
        category = get_object_or_404(Category, category_slug=category_slug)
        product = Products.objects.get(category__category_slug = category_slug,product_slug = product_slug)
        related_products = Products.objects.filter(category=category)[:5]
        is_exists = CartItem.objects.filter(cart_id__cart_id = _cart_id(request), product=product).exists()
    except Exception as e:
        raise e
    context = {
        'title': product.product_name,
        'product': product ,
        'related_products':related_products,
        'is_exists': is_exists,
    }
    return render(request, 'store/product_details.html', context)