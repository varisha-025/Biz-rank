"""bizrank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from user import views as user_view
from django.contrib.auth import views as auth
from . import views

urlpatterns = [
    # path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    # Project URLs
    path('aboutus/', views.about_us, name='aboutus'),
    path('admin/', admin.site.urls),
    path('brands/', include('brands.urls')),
    path('user/', include('user.urls')),
    path('products/', include('products.urls')),
    # path('contactus/', views.contact_us, name='contactus'),
    # path('rate/', include('rating.urls')),

    path('login_user/', user_view.login_user, name ='login_user'),
    path('logout/', auth.LogoutView.as_view(template_name ='index.html'), name ='logout'),
    path('register/', user_view.register, name ='register'),
]

