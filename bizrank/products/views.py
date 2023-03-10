from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import ProductRegisterForm
from .models import Product

def index(request):
    return HttpResponse("Hello, world. You're at the user index.")

def detail(request, product_id):
    try:
        prod = Product.objects.get(id=product_id)
        context = {
            'product': prod,
            'title': prod.name
        }
        return render(request, 'product_detail.html', context)
    except:
        return HttpResponse("Product does not exist.")



def create_product(request):
    if request.method == 'POST':
        form = ProductRegisterForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            print('product saved')
            messages.success(request, f'Congrats! Your product has been created.')
    else:
        print('form is not valid')
        form = ProductRegisterForm()

    return render(request, 'add_product.html')


def delete_product(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        Product.objects.filter(id=id).delete()   
        messages.success(request, f'Product has been deleted.')
    return render(request, 'delete_product.html')