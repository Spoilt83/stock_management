from celery import shared_task
from django.core.mail import send_mail
from .models import Product
from .serializer import ProductSerializer


@shared_task
def verify_product_expiry():
    """
    Send notification when a product is close to expiration.
    """
    print('Task running')
    products = Product.objects.all()
    print(products)
    serializer = ProductSerializer(products, many=True)
    for product in serializer.data:
        days_to_expiration = product['days_to_expiration']  # Asegúrate de usar el campo correcto
        if days_to_expiration <= 10:
            print(f'Product {product["product_name"]} expires in {days_to_expiration} days.')
            send_mail(
                'Expiration Alert',
                f'Your product {product["product_name"]} expires in {days_to_expiration} days.',
                'marvinsolano83@gmail.com',
                ['marvinsolano83@hotmail.com'],  
                fail_silently=False,
            )