from django.db import models
from product.models import Product

# Create your models here.
class Order(models.Model):
    name_client = models.CharField(max_length = 100 , null = False, blank = False)
    products = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default = False)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)

    class Meta:
        ordering = ['name_client']

    def __str__(self):
        return '%s %s' % (self.name_client, self.status)
