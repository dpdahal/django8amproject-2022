from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def index(request):
    data = {
        'bannerData': Banner.objects.all(),
        'categoryData': Category.objects.all(),
        'productData': Product.objects.order_by('-id'),
    }
    return render(request, 'pages/home/index.html', data)


def contact(request):
    return render(request, 'pages/contact/contact.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_data = authenticate(username=username, password=password)
        if user_data:
            login(request, user_data)
            return redirect('index')
        else:
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'pages/user/login.html')


def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user_data = User.objects.create(username=username, email=email, password=password)
        login(request, user_data)
        return redirect('index')
    else:
        return render(request, 'pages/user/register.html')


def category_list(request):
    data = {
        'categoryData': Category.objects.all(),
    }
    return render(request, 'pages/category/category.html', data)


def product_list(request):
    data = {
        'productData': Product.objects.all(),
    }
    return render(request, 'pages/product/product.html', data)


def banner_details(request, slug):
    data = {
        'bannerData': Banner.objects.get(slug=slug),
    }
    return render(request, 'pages/banner/banner-details.html', data)


@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'pages/cart/index.html')
