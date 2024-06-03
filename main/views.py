from functools import wraps
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.forms import ReviewForm
from django.utils.timezone import now
from datetime import timedelta
from main.models import Profile
from main.models import Product
from main.models import Vacancy
from main.models import Coupons
from main.models import Contacts
from main.models import Review, News, FAQ, Cart, CartItem, Order, OrderItem
from django.shortcuts import render
from django.db.models import Count, Sum, Q
from django.contrib.auth.decorators import user_passes_test

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_product, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_product.quantity += 1
        cart_product.save()
    return redirect('/')

@login_required
def complete_order(request):
    if request.method == 'POST':
        # Получение стоимости заказа из корзины
        cart = Cart.objects.get(user=request.user)
        cartproduct_set = CartItem.objects.filter(cart=cart)
        total_price = 0
        for cart_product in cartproduct_set:
            total_price += cart_product.product.price * cart_product.quantity
        
        # Создание объекта заказа и сохранение в базу данных
        order = Order.objects.create(user=request.user, total_price=total_price, address=request.POST.get('address'))
        
        # Создание объектов OrderItem и их связь с заказом
        for cart_product in cartproduct_set:
            order_item = OrderItem.objects.create(order=order, product=cart_product.product, quantity=cart_product.quantity)
        
        # Очистка корзины после совершения заказа
        cartproduct_set.delete()
        
        return redirect('/')
    else:
        return redirect('/')

def role_required(roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.profile.role in roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('')  
        return _wrapped_view
    return decorator


@login_required
def view_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'view_orders.html', {'orders': orders})

@login_required
def my_orders(request):
    user_role = request.user.profile.role  # Получаем роль текущего пользователя
    if user_role in ['admin', 'worker']:   # Если роль админа или работника
        orders = Order.objects.all()       # Получаем все заказы
    else:
        orders = Order.objects.filter(user=request.user)  # Получаем заказы текущего пользователя

    return render(request, 'view_orders.html', {'orders': orders, 'user_role': user_role})

@login_required
def view_orders(request):
    user_profile = Profile.objects.get(user=request.user)
    orders = Order.objects.all()

    user_role = user_profile.role

    context = {
        'orders': orders,
        'user_role': user_role
    }

    return render(request, 'view_orders.html', context)

@login_required
def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    cartproduct_set = CartItem.objects.filter(cart=cart)
    total_price = 0
    for cart_product in cartproduct_set:
        total_price += cart_product.product.price * cart_product.quantity
    return render(request, 'cart.html', {'cartproduct_set': cartproduct_set, 'total_price': total_price})

@login_required
def index(request):
    api_url = "https://catfact.ninja/fact"
    response = requests.get(api_url)

    if response.status_code == 200:
        cat_fact = response.json()['fact']

    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        joke_setup = data["setup"]
        joke_punchline = data["punchline"]
    context = {
        'cat_fact':cat_fact,
        'joke_setup':joke_setup,
        'joke_punchline':joke_punchline
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def news(request):
    news = News.objects.all
    return render(request, 'news.html',{'news':news})

def faq(request):
    faq = FAQ.objects.all
    return render(request, 'faq.html',{'faq':faq})

def contacts(request):
    contacts = Contacts.objects.all
    return render(request, 'contacts.html', {'contacts':contacts})

def policy(request):
    return render(request, 'policy.html')

@login_required
def cataloge(request,category=None):
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    # Фильтрация по цене
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    return render(request, 'cataloge.html', {'products':products})

def vacancy(request):
    vacancies = Vacancy.objects.all
    return render(request, 'vacancy.html', {'vacancies':vacancies})
    
@login_required
def review_list(request):
    reviews = Review.objects.all()
    return render(request, "review_list.html", {'reviews': reviews})

@login_required
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, "create_review.html", {'form': form})

def coupons(request):
    coupons = Coupons.objects.all   
    return render(request, 'coupons.html',{'coupons':coupons})

def login(request):   
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, ' Invalid Input')
            return redirect('login')
    else:
        return render(request, 'login.html')
        

def register(request):   
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        age = request.POST['age']
        if int(age) < 18:
            messages.info(request, "User must be at least 18 years old.")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already Taken")
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, "Username already Taken")
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()

            user_login = auth.authenticate(username = username, password = password)
            auth.login(request,user_login)

            user_model=User.objects.get(username=username)
            new_profile=Profile.objects.create(user=user_model,id_user = user_model.id)
            new_profile.save()
            return redirect ('settings')
    else: 
        return render(request, 'register.html')
    
@login_required 
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method=='POST':
        address = request.POST['address']
        phone_number = request.POST['phone_number']

        user_profile.address=address
        user_profile.phone_number=phone_number
        user_profile.save()
        
    return render(request, 'settings.html',{'user_profile': user_profile})


@role_required(['worker', 'admin'])
def my_orders(request):
  
    current_user = request.user

    profile = Profile.objects.get(user=current_user)

    
    if profile.role in ['worker', 'admin']:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user=current_user)
    context = {
        'user_role': profile.role,
        'orders': orders
    }

    return render(request, 'view_orders.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def popular_products(request):
    # Получаем наиболее популярный товар
    most_popular_product = Product.objects.annotate(total_orders=Count('orderitem')).order_by('-total_orders').first()
    end_date = now()
    start_date = end_date - timedelta(days=30)
    # Получаем наименее популярный товар
    least_popular_product = Product.objects.annotate(total_orders=Count('orderitem')).order_by('total_orders').first()
    total_orders_sum = Profile.objects.aggregate(total=Sum('orders'))['total']
    monthly_volume = Product.objects.annotate(
        monthly_volume=Count('orderitem', filter=Q(orderitem__order__created_at__gte=start_date, orderitem__order__created_at__lte=end_date))
    )
    context = {
        'most_popular_product': most_popular_product,
        'least_popular_product': least_popular_product,
        'total_orders_sum': total_orders_sum,
        'monthly_volume': monthly_volume
        
    }

    return render(request, 'popular_products.html', context)