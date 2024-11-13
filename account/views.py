from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from decimal import Decimal
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from about.models import About, Brands, Service
from account.forms import CheckoutForm, ContactForm, LoginForm, UserRegistrationForm
from account.models import User
from cart.cart import Cart
from contact.models import Contact, Title
from home.models import Home
from info.models import Info
from shop.models import Categories, Shop
from showcase.models import Category, Product
from django.contrib import messages

from django.core.paginator import Paginator

# Create your views here.


def accountView(request):
    user = User.objects.all()
    home = Home.objects.all()
    category = Category.objects.all()
    product = Product.objects.all()
    info = Info.objects.all()
    cart = Cart(request)
    shop = Shop.objects.all()
    categories = Categories.objects.all()

    return render(request, 'landing/index.html', context={
        'user': user,
        'home': home,
        'category': category,
        'product': product,
        'shop': shop,
        'categories': categories,
        'cart': cart,
        'info': info,

    })


def aboutView(request):
    user = User.objects.all()
    about = About.objects.all()
    service = Service.objects.all()
    brands = Brands.objects.all()
    info = Info.objects.all()
    product = Product.objects.all()
    shop = Shop.objects.all()
    categories = Categories.objects.all()
    cart = Cart(request)

    return render(request, 'landing/about.html', context={
        'user': user,
        'about': about,
        'service': service,
        'brands': brands,
        'cart': cart,
        'product': product,
        'shop': shop,
        'categories': categories,
        'info': info,

    })


def contactView(request):
    user = User.objects.all()
    title = Title.objects.all()
    contact = Contact.objects.all()
    info = Info.objects.all()
    cart = Cart(request)
    product = Product.objects.all()
    shop = Shop.objects.all()
    categories = Categories.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            form.save(commit=False)
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            form.save()
            messages.success(
                request, "Your message has been sent successfully!")
            return HttpResponseRedirect("#")

    else:
        form = ContactForm()

    return render(request, 'landing/contact.html', context={
        'user': user,
        'contact': contact,
        'title': title,
        'cart': cart,
        'product': product,
        'shop': shop,
        'categories': categories,
        'info': info,
        'form': form,


    })


def shopView(request):
    user = User.objects.all()
    about = About.objects.all()
    brands = Brands.objects.all()
    category = Category.objects.all()
    product = Product.objects.all()
    categories = Categories.objects.all()
    info = Info.objects.all()
    cart = Cart(request)

    # Get the category ID from request
    category_id = request.GET.get('categories')

    # Filter products based on category
    if category_id and category_id != 'all':
        products = Shop.objects.filter(categories__id=category_id)
    else:
        products = Shop.objects.all()

    # Paginate the filtered products
    paginator = Paginator(products, 9)  # Show 9 products per page
    page_number = request.GET.get('page')
    shop_list = paginator.get_page(page_number)

    return render(request, 'landing/shop.html', context={
        'user': user,
        'about': about,
        'category': category,
        'product': product,
        'brands': brands,
        'products': products,  # This can be used for displaying all products if needed
        'categories': categories,
        'shop': shop_list,  # This should now reflect the filtered products
        'cart': cart,
        'info': info,
        'shop_has_previous': shop_list.has_previous(),
        'shop_previous_page': shop_list.previous_page_number() if shop_list.has_previous() else None,
        'shop_has_next': shop_list.has_next(),
        'shop_next_page': shop_list.next_page_number() if shop_list.has_next() else None,
        'shop_number': shop_list.number,
        'shop_page_range': paginator.page_range,
    })


def checkoutView(request):
    user = User.objects.all()
    info = Info.objects.all()
    cart = Cart(request)
    count = Decimal('0.02')  # Convert the float to Decimal
    discount = Decimal(cart.get_total_price()) * count
    delivery = Decimal('0.05') * Decimal(cart.get_total_price())
    subtotal = cart.get_total_price()
    total_price = subtotal - discount + delivery

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            checkout_instance = form.save(commit=False)
            checkout_instance.total_price = total_price

            # Collect product names and quantities
            product_names = []
            quantities = []
            for item in cart:  # Iterate over items in the cart
                # Access the product's name attribute
                product_names.append(item['product'].name)
                # Access the stored quantity
                quantities.append(item['quantity'])

            # Assign the product names and quantities to the instance
            checkout_instance.product_names = ', '.join(product_names)
            checkout_instance.quantities = ', '.join(map(str, quantities))

            # Save the instance
            checkout_instance.save()
            messages.success(
                request, "Your order has been placed successfully!")

            # Clear the cart after saving the order
            cart.clear()  # Assuming you have a clear method in your Cart class
            return HttpResponseRedirect("/checkout.html")
    else:
        form = CheckoutForm(
            initial={'total_price': cart.get_total_price() + delivery - count})

    return render(request, 'landing/checkout.html', context={
        'user': user,
        'info': info,
        'cart': cart,
        'form': form,
        'discount': discount,
        'delivery': delivery,
        'total_price': total_price,


    })


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('account')  # Redirect to the index view
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()  # Initialize the form for a GET request

    return render(request, 'account/login.html', {'form': form})


def register(request):
    user = User.objects.all()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Save the new user
            new_user = user_form.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', context={
        'user_form': user_form,
        'user': user,
    })


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('password_change_done')


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'password_change_done.html'
