from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=100,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY=(('indoor','indoor'),
                ('outdoor','outdoor'),
                )
    name=models.CharField(max_length=100,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=100,null=True,choices=CATEGORY)
    description=models.CharField(max_length=400,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS=(('pending','pending'),
            ('out for delivery','out for delivery'),
            ('Delivery','Delivery'),     
                    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=20,null=True,choices=STATUS)
