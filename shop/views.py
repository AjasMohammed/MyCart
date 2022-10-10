from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders
from math import ceil

# Create your views here.


def index(request):

    all_products = []
    cat_product = Product.objects.values('category', 'id')
    catagories = {item['category'] for item in cat_product}
    for category in catagories:
        product = Product.objects.filter(category=category)
        n = len(product)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        all_products.append([product, range(1, nSlides), nSlides])

    params = {'all_products': all_products}

    return render(request, 'shop/index.html', params)


def about(request):
    products = Product.objects.all()

    return render(request, 'shop/about.html', {'products': products})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, description=desc)
        contact.save()

    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def productView(request, myid):
    # Feching Product using id
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/productview.html', {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip_code', '')

        checkout = Orders(items_json=items_json, name=name, email=email, phone_number=phone, address1=address1, address2=address2,
                          state=state, city=city, zip_code=zip_code)
        checkout.save()
        thank = True
        id = checkout.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')