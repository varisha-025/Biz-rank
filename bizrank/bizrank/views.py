from django.shortcuts import redirect, render



def about_us(request):
    return render(request, 'about_us.html')