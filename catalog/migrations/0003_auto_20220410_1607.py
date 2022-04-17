# Generated by Django 4.0.3 on 2022-04-10 13:07

from django.db import migrations
from django.utils import timezone

def sample_data(apps, schema_editor):
    # get models
    Product = apps.get_model('catalog', 'Product')
    PriceLog = apps.get_model('catalog', 'PriceLog')

    # product 1
    product1 = Product(name='adidas Consortium Campus 80s Running Shoes', price=27.56)
    product1.save()

    priceLog1 = PriceLog(product=product1,price=product1.price,updated_date=timezone.now())
    priceLog1.save()

    # product 2
    product2 = Product(name='Nike Floral Roshe Running Shoes', price=40.00)
    product2.save()

    priceLog2 = PriceLog(product=product2,price=product2.price,updated_date=timezone.now())
    priceLog2.save()

    # product 3
    product3 = Product(name='Nike SB Zoom Stefan Janoski "Medium Mint"', price=30.00)
    product3.save()

    priceLog3 = PriceLog(product=product3,price=product3.price,updated_date=timezone.now())
    priceLog3.save()

class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_pricelog_id_alter_product_id'),
    ]

    operations = [
        migrations.RunPython(sample_data),
    ]
