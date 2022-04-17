import datetime
from django.db import models
from django.utils import timezone

# represents a product manager
class ProductManager(models.Manager):
    def get_by_id_or_null(self, product_id):
        return Product.objects.filter(id=product_id).first()

# represents a product
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    # although our technical requirenment says that a price value should not be restricted
    # we know that MySQL has some restrictions for such a field type
    # Anyway I guess  65 digits is more that enough for any price
    price = models.DecimalField(default=0, max_digits=65, decimal_places=2)
    objects = ProductManager()
    def uppdate_price(self, price):
        self.price = price
        self.save()
        pricelog = PriceLog(product=self, price=self.price, updated_date=timezone.now())
        pricelog.save()
        return self


# represents a pricelog manager
class PricelogManager(models.Manager):
    def get_by_product_id(self, product_id):
        return PriceLog.objects.filter(product_id=product_id).order_by('-updated_date')

# represents a price log item
class PriceLog(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # although our technical requirenment says that a price value should not be restricted
    # we know that MySQL has some restrictions for such a field type
    # Anyway I guess  65 digits is more that enough for any price
    price = models.DecimalField(default=0, max_digits=65, decimal_places=2)
    updated_date = models.DateTimeField()
    objects = PricelogManager()