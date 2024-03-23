"""
This module contains the viewsets for the Product model.
"""
from django.db.models import Case, When, F, Value, IntegerField
from datetime import datetime, timedelta, date
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .serializer import ProductSerializer, UserSerializer
from .forms import ProductForm


@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def login(request):
    """
    Login for user.
    """
    return render(request, 'pages/login.html')




@api_view(['GET', 'POST'])
def user_authentication(request):
    """
    Validate credentials for user.
    """
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return render(request, 'pages/login.html')
        #return redirect('login')

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return render(request, 'pages/home.html', {'user': serializer.data, 'token': token.key})


@api_view(['GET', 'POST']) 
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@renderer_classes ([TemplateHTMLRenderer])
def home(request):
    """
     Home page.
    """
    return render(request, template_name='pages/home.html')

@api_view(['GET', 'POST']) 
@renderer_classes ([TemplateHTMLRenderer])
def list(request):
    """
    Return a list of all products.
    """
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return render(request, 'products/list.html', {'products': serializer.data})


@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def date_range(request):
    """
    Return a list of all products close to expiration.
    """
    start_date = request.GET.get('start_date')
    start_date = datetime.strptime(start_date, '%Y-%m-%d')    
    end_date = request.GET.get('end_date')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    products = Product.objects.filter(product_expiration_date__range=(start_date, end_date))
    serializer = ProductSerializer(products, many=True)
    filtered_products = [product for product in serializer.data if product['days_to_expiration'] <= 10]
    if filtered_products:
        return render(request, 'products/date_range.html', context={'products': filtered_products, 'start_date':start_date, 'end_date':end_date})
    else:
        return render(request, 'products/date_range.html', context={'message': 'No products close to expiration.'})
    

@api_view(['GET', 'POST']) 
@renderer_classes ([TemplateHTMLRenderer])
def create(request):
    """
    Create a new product.
    """
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, template_name='products/create.html', context={'form': form}, status=status.HTTP_201_CREATED)
       
@api_view(['GET', 'POST', 'PUT', 'PATCH']) 
@renderer_classes ([TemplateHTMLRenderer])
def update(request, id):
    """
    Update a product.
    """
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, template_name='products/update.html', context={'form': form}, status=status.HTTP_200_OK)

@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def delete(request, id):
    """
    Delete a product.
    """
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('list')
