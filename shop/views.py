from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order
from math import ceil

# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('product_name')
    cats = {item['product_name'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(product_name=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides ), nSlides])
    #params = {'no_of_slides':nSlides,'range':range(1,nSlides),'product': products}
   # allProds = [[products, range(1 , nSlides), nSlides],
       #         [products, range(1 , nSlides), nSlides]]
    params = {'allProds': allProds}
    return render(request,'shop/index.html',params)

def about(request):
   return render(request,'shop/about.html') 

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name , email=email , phone=phone , desc=desc)
        contact.save()
    return render(request,'shop/contact.html') 

def search(request):
    return render(request,'shop/search.html') 

def productView(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/prodview.html',{'product':product[0]}) 

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address_1 = request.POST.get('address_1','')
        address_2 = request.POST.get('address_2','')
        phone = request.POST.get('phone','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        order = Order(items_json=items_json,name=name , email=email , address_1=address_1, address_2=address_2, phone=phone , city=city, state=state, zip_code=zip_code)
        order.save() 
        thank = True
        return render(request,'shop/checkout.html',{'thank':thank})
    return render(request,'shop/checkout.html') 