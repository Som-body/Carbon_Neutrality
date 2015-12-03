from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from decimal import *
from math import exp

class CarouselSlide(models.Model):
    url = models.CharField(max_length = 255, default = '')
    image = models.ImageField(upload_to = 'pictures/')
    
    def __str__(self):
        return self.image.url
    
class UserModel(models.Model):
    user = models.OneToOneField(User, related_name='info')
    profile_img = models.ImageField(upload_to = 'profile_pic/', default = 'profile_pic/default_pic.png')
    
    precal_car = models.IntegerField(default = 0)
    precal_car_efficiency = models.IntegerField(default = 0)
    precal_fuel_type = models.CharField(default='Gasoline', max_length='9')
    precal_bus = models.IntegerField(default = 0)
    precal_train = models.IntegerField(default = 0)
    precal_plane = models.IntegerField(default = 0)
    precal_electricity = models.IntegerField(default = 0)
    precal_fuel = models.IntegerField(default = 0)
    precal_gas = models.IntegerField(default = 0)
    precal_water = models.IntegerField(default = 0)
    precal_general_meat = models.IntegerField(default = 0)
    precal_poultry = models.IntegerField(default = 0)
    precal_seafood = models.IntegerField(default = 0)
    precal_vegetable = models.IntegerField(default = 0)
    precal_milk = models.IntegerField(default = 0)
    precal_drink = models.IntegerField(default = 0)
    precal_clothes = models.IntegerField(default = 0)
    precal_furniture = models.IntegerField(default = 0)
    precal_health = models.IntegerField(default = 0)
    precal_vehicle = models.IntegerField(default = 0)
    precal_house = models.IntegerField(default = 0)
    
    
    car_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    car_efficiency = models.DecimalField(default = Decimal('0.00'), max_digits = 6, decimal_places=2)
    fuel_emission = models.DecimalField(default = Decimal('8874'), max_digits = 5, decimal_places=0)
    bus_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    train_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    plane_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    electricity_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    fuel_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    gas_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    water_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    general_meat_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    poultry_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    seafood_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    vegetable_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    milk_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    drink_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    clothes_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    furniture_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    health_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    vehicle_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    house_emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 15, decimal_places=2)
    
    emissions = models.DecimalField(default = Decimal('0.00'), max_digits = 16, decimal_places=2)
    
    offset = models.DecimalField(default = Decimal('0.00'), max_digits = 16, decimal_places=2)
    
    net_emission = models.DecimalField(default = Decimal('0.00'), max_digits = 16, decimal_places=2)
    
    def get_emissions(self):
        return (self.car_emissions + self.train_emissions + self.bus_emissions + self.plane_emissions + 
                self.electricity_emissions + self.fuel_emissions + self.gas_emissions + self.water_emissions +
                self.general_meat_emissions + self.poultry_emissions + self.seafood_emissions + self.milk_emissions + self.vegetable_emissions + self.drink_emissions +
                self.clothes_emissions + self.furniture_emissions + self.health_emissions + self.vehicle_emissions + self.house_emissions)
    
    def get_net_emission(self):
        return (self.get_emissions() / Decimal('1000')) - self.offset
    
    class Meta:
        ordering = ['net_emission']
        
    def __str__(self):
        return 'name: ' + self.user.get_username() + ' emissions: ' + str(self.net_emission)
        
    
class Tree(models.Model):
    user = models.ForeignKey(User)
    adult_diameter = models.DecimalField(max_digits = 6, decimal_places = 2) #cm
    location = models.CharField(max_length = 50)
    longitude = models.DecimalField(max_digits = 8, decimal_places = 5)
    latitude = models.DecimalField(max_digits = 7, decimal_places = 5)
    species = models.CharField(max_length = 50)
    date_planted = models.DateField()
    is_alive = models.BooleanField(default = True)
    picture = models.ImageField(upload_to = 'trees', default = 'trees/tree101.png')
    date_died = models.DateField(null = True, blank = True, default = None)
    
    def get_lifetime_offset(self):
        return self.cal_lifetime_offset()[0]
    
    def get_offset_over_time(self):
        return self.cal_lifetime_offset()[1]
    
    def cal_lifetime_offset(self):
        
        lifetime_offset = Decimal('0.0')
        offset_over_time = []
        
        body_mass = Decimal('0.0998') * (self.adult_diameter ** Decimal('2.5445'))
        growth_rate = Decimal('0.208') * (body_mass ** Decimal('0.763'))
        
        for i in range(86):
            calculation_year = self.date_planted.year + i
            
            dkdy = (Decimal(str(exp(1 - (((growth_rate * Decimal(str(exp(1)))) * Decimal(str(calculation_year - self.date_planted.year)) / body_mass))))) / Decimal(str(exp(1)))) * (growth_rate * Decimal(str(exp(1))))
            dkdyt = dkdy * Decimal('1.24')
            carbon = dkdyt * Decimal('0.47')
            co2 = carbon * Decimal('3.6663')
            co2 = co2.quantize(Decimal('.01'), rounding=ROUND_UP)
            lifetime_offset += co2
            
            offset_over_time.append(co2)
        
        return (lifetime_offset, offset_over_time)
    
    class Meta:
        ordering = ['-date_planted']
    
class Friend(models.Model):
    user = models.ForeignKey(User)
    friend = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_friends")
    friend_model = models.ForeignKey(UserModel, null = True)
    date_friended = models.DateTimeField(default = timezone.now)
    
    class Meta:
        unique_together = (("user", "friend"),)
        ordering = ['friend_model']
        
    def __str__(self):
        return 'user: ' + self.user.get_username() + ' friend: ' + self.friend.get_username()
    

    

