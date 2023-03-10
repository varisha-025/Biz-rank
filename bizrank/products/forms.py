
from django import forms
from .models import Product, ProductCategory
from brands.models import Brand

class ProductRegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()
    # brand = forms.ForeignKey(Brand, on_delete=forms.CASCADE, related_name='products')

    class Meta:
        model = Product
        fields = ['name','price','description']





