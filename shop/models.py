from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    flavour = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=800)
    date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")
    def __str__(self):
        return self.product_name
    

class Contact(models.Model):
    msgid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")
    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    address_1 = models.CharField(max_length=500)
    address_2 = models.CharField(max_length=500)
    phone = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=500, default="")
    state = models.CharField(max_length=500)
    zip_code = models.CharField(max_length=500)
    def __str__(self):
        return self.name

  