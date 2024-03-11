from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    reg_date = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'Username: {self.name}, age: {self.age}, email: {self.email}, phone: {self.phone}, address: {self.address}.'
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=0);    
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name: {self.name}, description: {self.description}, price: {self.price}, quantity: {self.quantity}.'

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Customer: {self.customer}, products ids: {self.products}, total_pric: {self.total_price}.'



