from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import loginForm,  signupfinalForm, signupForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Seller, Product, order, orderitem, Buyer, ProductCategory, StoreType, Transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    try:
        custom = User.objects.get(id=request.user.id)
        buyer = Buyer.objects.get(user=custom)
    except Buyer.DoesNotExist:
        return redirect("shop:signupfinal")    

    page = 'home'
    categories = ProductCategory.objects.all()[:5]
    shoptypes = StoreType.objects.all()[:5]
    context = {
        'categories': categories,
        'shoptypes':shoptypes,
        'page':page
    }
    return render(request, 'shop/index.html', context)


def stores(request):
    sellers = Seller.objects.all()
    context = {
        'sellers':sellers,
    }
    return render(request, "shop/stores.html", context)



def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect("shop:index")
   
   # form = loginForm()
   # context = {'form':form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop:index')
        messages.error(request, 'incorrect username or password')
       
    return render(request, 'shop/login.html')



def signup(request):
    if request.user.is_authenticated:
        return redirect("shop:index")
    
    form = signupForm()
    context = {
        'form':form,
    }
    if request.method == "POST":
       user = User.objects.filter(username = request.POST.get('username'))
       pass2 = request.POST.get('pass2')
       password = request.POST.get('password')
       if user:
           messages.error(request, 'username not available')
           return render(request ,'shop/signup.html')
       else:
           form = signupForm(request.POST)
           if form.is_valid() & (pass2==password):
               user = form.save(commit=False)
               user.username = user.username.lower()
               user.save()
               login(request, user)
               return redirect('shop:signupfinal')
    return render(request, 'shop/signup.html', context)



def signupfinal(request):
    custom = User.objects.get(id=request.user.id)
   
    form = signupfinalForm()
    context = {
        'form':form,
    }
    if request.method == 'POST':
        form = signupfinalForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)

            user.user = custom
            user.save()
            return redirect("shop:index")
        else:
            messages.error(request, 'Enter valid credentials')
            return render(request, 'shop/signupfinal.html', context)

    return render(request, 'shop/signupfinal.html', context)


def logoutPage(request):
    logout(request)
    return redirect('shop:login')


def sellerDetail(request, pk):
    seller = Seller.objects.get(id=pk)
    products = seller.products.all()
    context = {'seller':seller, 'products':products}
    return render(request, 'shop/sellerDetail.html', context)



@login_required(login_url='/login/')
def cart(request):
    page = 'cart'
    if request.user:
        custom = User.objects.get(id=request.user.id)
    
        buyer = Buyer.objects.get(user=custom)
        Order, created= order.objects.get_or_create(buyer=buyer)
        try:
            Order_items = Order.orderitem_set.all()
        except order.DoesNotExist:
            Order_items = None
        context = {
         'order':Order, 
         'order_items':Order_items, 
         'page':page
        }    
    else:
        context = {
            'order':'',
            'orderitems':'', 
            'page':page
        }        

   
    return render(request, 'shop/cart.html', context)
                
def profile(request):
    page = 'profile'
    custom = User.objects.get(id=request.user.id)
    buyer  = Buyer.objects.get(user=custom)
    context = {'buyer':buyer, 'page':page}
    return render(request, 'shop/profile.html', context)      

@csrf_exempt
def updatecart(request):
    custom= User.objects.get(id=request.user.id)
    data = json.loads(request.body)
    productID  = Product.objects.get(id=data['item_id'])
    buyer  = Buyer.objects.get(user=custom)
    Order, created = order.objects.get_or_create(buyer=buyer)
    Order_items , created = orderitem.objects.get_or_create(order=Order, product=productID)
    if created == False:
        Order_items.quantity += 1
        Order_items.save()
    
    return  JsonResponse('Addedm to cart', safe=False)



@csrf_exempt
def upcart(request):
    data = json.loads(request.body)
    item = orderitem.objects.get(id=data['item_id'])
    if data['action'] == 'cart-up':
        item.quantity = item.quantity + 1
        item.save()
    elif data['action'] == 'cart-down':
        item.quantity = item.quantity - 1
        item.save()    

    return JsonResponse("action received", safe=False)    


@csrf_exempt
def closecart(request):
    data = json.loads(request.body)
    order_item = orderitem.objects.get(id=data['item_id'])
    order_item.delete()
    return JsonResponse("done mate", safe=False)



def checkout(request):
    custom = User.objects.get(id=request.user.id)
    buyerr = Buyer.objects.get(user=custom)
    Order = order.objects.get(buyer=buyerr)
    orderitems = Order.orderitem_set.all()

    context = {'order_items':orderitems, 'order':Order}

    return render(request, 'shop/checkout.html', context)

@csrf_exempt
def checkoutBackend(request):
    custom = User.objects.get(id=request.user.id)
    buyerr = Buyer.objects.get(user=custom)

    data = json.loads(request.body)
    Order = order.objects.get(id=data['order_id'])
    total = Order.get_cart_total
    transaction = Transaction.objects.create(sender=buyerr, amount=total, Order=Order)
    transaction.save()
    orderitems = Order.orderitem_set.all()
    for item in orderitems:
        amount = item.quantity
        product = Product.objects.get(id=item.product.id)
        product.amount = product.amount - amount
        product.save()
    Order.delete()
    return JsonResponse("done", safe=False)

def mpesa(request):
    print(request.body)

header = {
    "Authorization":"Basic cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ=="
}

payload = {

}
parameter = {
    "grant_type":"client_credentials"
}
response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': 'Basic cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ==' })
data = response.text.encode('utf8')
data = json.loads(data)
access_token = data['access_token']
print(access_token)