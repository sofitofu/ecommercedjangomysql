from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
#MODELOS

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Customer(models.Model):
    
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold'),
    ]
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True)
    phone = PhoneNumberField(region='US')
    birth_date = models.DateField(null= True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default= MEMBERSHIP_BRONZE)
    
    
class Address(models.Model):
    street = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    zip = models.IntegerField(default=0)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    
class Collection(models.Model):
    title = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    featured_product = models.ForeignKey('Product', on_delete = models.SET_NULL, null = True, related_name= '+')
    
class Product(models.Model):
    title = models.CharField(max_length=254)
    slug = models.SlugField()
    description = models.TextField(max_length=254)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    lastupdate = models.DateTimeField(auto_now_add=True)
    collection = models.ForeignKey(Collection, on_delete= models.SET_NULL, null=True)
    promotions = models.ManyToManyField(Promotion, related_name='products')

class Order(models.Model):
        
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    payment_status = [
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]
    
    placed_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete= models.PROTECT)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete= models.PROTECT)
    product = models.ForeignKey(Product, on_delete= models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.SmallIntegerField()   

