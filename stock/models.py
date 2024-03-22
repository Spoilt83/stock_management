from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, verbose_name="Name")
    product_description = models.TextField(verbose_name="Description")
    product_quantity = models.IntegerField(verbose_name="Quantity")
    product_expiration_date = models.DateField(verbose_name="Date of Expiration") 

    class Meta:
        indexes = [
            models.Index(fields=['product_expiration_date']),
        ]  

    def __str__(self):
        return str(self.product_name)
