from django import forms
# from django.contrib.auth.models import User
from user.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	phone = forms.CharField(max_length = 10)
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	username = forms.CharField(max_length = 20)
	password1 = forms.CharField(max_length = 20)
	password2 = forms.CharField(max_length = 20)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
