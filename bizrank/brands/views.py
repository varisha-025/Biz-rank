from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from rating.models import Rating
from user.models import User

from .forms import BrandRegisterForm
from .models import Brand, BrandOwnership


def get_all_brands():
    all_brands = Brand.objects.all()
    context = {
        'all_brands': all_brands
    }
    return context


def home(request):
    context = get_all_brands()
    return render(request, 'dashboard.html', context)


def create_brand_ownership(user, brand):
    user = User.objects.get(id=user)
    brand_ownership = BrandOwnership.objects.create(user=user, brand=brand)
    brand_ownership.save()

@login_required
def create_brand(request):
    if request.method == 'POST':
        form = BrandRegisterForm(request.POST)
        if form.is_valid():
            print('form is valid')
            brand = form.save()
            print('brand saved')
            user = request.user.id
            create_brand_ownership(user, brand)
            messages.success(request, f'Congrats! Your brand has been created.')
    else:
        form = BrandRegisterForm()

    return render(request, 'add_brand.html')

@login_required
def delete_brand(request):
    if request.method == 'POST':
        brand_id = request.POST.get('brand_id')
        user_id = request.user.id
        brand = BrandOwnership.objects.filter(brand=brand_id)
        if brand.user.id == user_id:
            Brand.objects.get(id=brand_id).delete()
            messages.success(request, f'Your brand has been deleted.')
        else:
            messages.error(request, f'You do not have permission to delete this brand.')
    
    return render(request, 'delete_brand.html')


@login_required
def detail(request, brand_id):
    try:
        brand = Brand.objects.get(id=brand_id)
        context = {
            'brand': brand,
            'title': brand.name
        }
        return render(request, 'brand_detail.html', context)
    except:
        return HttpResponse("Brand does not exist.")
    

@login_required
def rate_brand(request):
    if request.method == 'POST':
        brand_id = request.POST.get('brand_id')
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        rating = request.POST.get('rating')
        brand = Brand.objects.get(id=brand_id)

        try:
            rate = Rating.objects.create(user=user, brand=brand, rating=rating)
            rate.save()
            messages.success(request, f'Your rating has been saved.')
        except:
            messages.error(request, f'Some error occured. Please try again later.')     

    
    return render(request, 'delete_brand.html')