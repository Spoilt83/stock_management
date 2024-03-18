"""
This module contains the viewsets for the Product model.
"""

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes

from django.shortcuts import render
from .models import Product
from .serializer import ProductSerializer


@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def home(request):
    """
     Return the home page.
    """
    return render(request, template_name='pages/index.html')

@api_view() 
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
def create(request):
    """
    Create a new product.
    """
    return render(request, template_name='products/create.html')
       
@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def update(request):
    """
    Update a product.
    """
    return render(request, template_name='products/update.html')

@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def delete(request):
    """
    Delete a product.
    """
    return render(request, 'products/delete.html')





# def home(request):
#     """
#     Return the home page.
#     """
#     return render(request, 'pages/index.html')

# def list(request):
#     """
#     Return a list of all products.
#     """
#     # queryset = self.get_queryset()
#     # return render(request, 'pages/product_list.html', {'queryset': queryset})
#     return render(request, 'products/list.html')
