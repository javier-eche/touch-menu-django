from django.db import models

# Create your models here.

TYPES_PRODUCT = (
    ("Desayuno", "Desayuno"),
    ("Almuerzo", "Almuerzo"),
    ("Cena", "Cena"),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    image = models.CharField(max_length=100, null=False, blank=False)
    type_product = models.CharField(max_length=15, choices=TYPES_PRODUCT)

    class Meta:
        ordering = ['type_product']

    def __str__(self):
        return '%s %s' % (self.type_product, self.name)