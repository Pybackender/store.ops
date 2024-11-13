from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from shop.models import Categories, Shop


def product_list(request, category_slug=None):
    category = None
    categories = Categories.objects.all()
    products = Shop.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Categories, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})



from django.shortcuts import render, get_object_or_404
from .models import Shop

def product_detail(request, id, slug):
    shop = get_object_or_404(Shop, id=id, slug=slug)
    cart_product_form = CartAddProductForm()

    context = {
        'shop': shop,
        'cart_product_form': cart_product_form,  # Ensure this is defined
    }
    return render(request, 'shop/product/detail.html', context)
