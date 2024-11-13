from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()  # Fetch all categories
    products = Product.objects.filter(available=True)  # Fetch all available products

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)  # Get the category by slug
        products = products.filter(category=category)  # Filter products by the selected category

    return render(request, 'showcase/product/list.html', {
        'categories': categories,
        'products': products  # Pass the products to the template
    })



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)  # Fetch the product
    return render(request, 'showcase/product/detail.html', {'product': product})  # Render the detail template
