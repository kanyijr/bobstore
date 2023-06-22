from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Buyer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='users/buyers/images/profiles/', default="default.png")
    user  = models.OneToOneField(User, related_name="buyers", on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True, default=None)
    def __str__(self):
        return self.firstname + "" + self.lastname
    
    @property
    def imageURL(self):
        try:
            url = self.profile_pic.url
        except:
            url =''
        return url 
class StoreType(models.Model):
      name = models.CharField(max_length=100)

      def __str__(self):
          return    self.name

class Seller(models.Model):
    store_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='users/sellers/images/profiles/')
    user = models.OneToOneField(User, related_name='sellers', on_delete=models.CASCADE)
    email = models.EmailField(default=None, null=True)
    storetype  = models.ForeignKey(StoreType, on_delete=models.SET_NULL, null=True , default=None)

    def __str__(self):
        return self.store_name
    

    @property
    def imageURL(self):
        try:
            url = self.profile_pic.url
        except:
            url = ''
        return url

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100) 

    def __str__(self):
        return self.category_name 


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.FloatField()
    picture = models.ImageField(upload_to="users/sellers/images/products/")
    picture.thumbnail = ImageSpecField(source='picture', processors=[ResizeToFill(100,100)], options={'quality':60})
    seller = models.ForeignKey(Seller, related_name="products", on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name="products")
    

    def __str__(self):
        return self.product_name
    


    @property
    def imageURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url

          

class order(models.Model):
    buyer = models.ForeignKey( Buyer, on_delete=models.CASCADE, related_name="orders")
    date_created = models.DateTimeField(auto_now=True)

    @property
    def get_cart_items(self):
        items = self.orderitem_set.all()
        return items.count()
    @property
    def get_cart_total(self):
        total = 0
        items = self.orderitem_set.all()
        for item in items:
            total += (item.product.price * item.quantity)
        return total    

class orderitem(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE , default=None, null=False)
    quantity = models.IntegerField(default=1)
    
    @property
    def total(self):
        price = self.product.price * self.quantity
        return price


class Transaction(models.Model):
    sender = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    Order = models.OneToOneField(order, on_delete=models.SET_NULL, null=True)

    @property
    def transac_property(self):
        return {'id':self.id, 'amount':self.amount, 'order_id':self.Order }
