from django import forms
from .models import Product
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    # Date widget customization
    product_expiration_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
     
    class Meta:
        model = Product
        fields = '__all__'


