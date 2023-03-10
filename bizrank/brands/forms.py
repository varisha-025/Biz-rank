
from django import forms
# from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from .models import Brand

class BrandRegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=200)
    # description = forms.CharField(widget=forms.Textarea)
    website = forms.URLField(required=False)
    email = forms.EmailField()
    # phone = forms.CharField(max_length=20)
    # address = forms.CharField(max_length=200)
    # city = forms.CharField(max_length=200)
    # state = forms.CharField(max_length=200)
    # zip_code = forms.CharField(max_length=200)
    # country = forms.CharField(max_length=200)
    # payment_options = ArrayField(forms.CharField(max_length=64))
    # social_media = forms.JSONField(required=False)
    # delivery_time = forms.CharField(max_length=200)
    # delivery_fee = forms.CharField(max_length=200, required=False)
    # product_categories = forms.CharField(max_length=200, required=False)
    # FAQs = forms.JSONField(required=False)

    class Meta:
        model = Brand
        fields = ['name','email',]





