from rest_framework import serializers
from datetime import datetime
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    days_to_expiration = serializers.SerializerMethodField(method_name='get_days_to_expiration') 

    def validate(self, attrs):
        if(attrs['product_quantity']<=0):
            raise serializers.ValidationError('Stock should not be less than or iqual 0')
        if(attrs['product_expiration_date']==datetime.now().date()):
            raise serializers.ValidationError('Due date cannot be the current date')
        return super().validate(attrs)
    
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'product_description', 'product_quantity', 'product_expiration_date', 'days_to_expiration']

    def get_days_to_expiration(self, product):
        current_date = datetime.now().date()
        
        calculate_expiration = (product.product_expiration_date - current_date).days

        return calculate_expiration