from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class CarouselSlide(models.Model):
    url = models.CharField(max_length = 255, default = '')
    image = models.ImageField(upload_to = 'pictures/')
    
    def __str__(self):
        return self.image.url
    
class UserModel(models.Model):
    user = models.OneToOneField(User)
    profile_img = models.ImageField(upload_to = 'profile_pic/', default = 'profile_pic/default_pic.png')
    
    car_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    motorcyle_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    train_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    bus_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    plane_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    electricity_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    fuel_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    gas_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    water_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    general_meat_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    poultry_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    seafood_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    milk_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    vegetable_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    drink_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    clothes_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    furniture_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    health_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    vehicle_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    house_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 10, decimal_places=2)
    
class Tree(models.Model):
    user = models.ForeignKey(User)
    adult_diameter = models.DecimalField(max_digits = 6, decimal_places = 2)
    location = models.CharField(max_length = 50)
    longitude = models.DecimalField(max_digits = 8, decimal_places = 5)
    latitude = models.DecimalField(max_digits = 7, decimal_places = 5)
    species = models.CharField(max_length = 50)
    date_planted = models.DateField()
    is_alive = models.BooleanField(default = True)
    picture = models.ImageField(upload_to = '/trees', default = 'pictures/tree101.png')
    date_died = models.DateField(null = True, blank = True, default = None)
    
    class Meta:
        ordering = ['-date_planted']
    
class Friends(models.Model):
    user = models.OneToOneField(User)
    friend = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_friends")
    date_friended = models.DateTimeField()
    
    class Meta:
        unique_together = (("user", "friend"),)
    

    

