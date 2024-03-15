from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    product_quantity = models.IntegerField()
    product_expiration_date = models.DateField()   

    def __str__(self):
        return str(self.product_name)
