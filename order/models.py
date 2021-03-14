from django.db import models
from product.models import Product


# Create your models here.
class Order(models.Model):
    name_client = models.CharField(max_length=100, null=False, blank=False)
    products = models.ManyToManyField(Product)
    status = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name_client']

    def __str__(self):
        return '%s %s' % (self.name_client, self.status)
