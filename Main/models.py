from django.db import models
from django.contrib.auth.models import User

class CarouselSlide(models.Model):
    url = models.CharField(max_length = 255, default = '')
    image = models.ImageField(upload_to = 'pictures/')
    
    def __str__(self):
        return self.image.url
    
class UserModel(models.Model):
    user = models.OneToOneField(User)
    profile_img = models.ImageField(upload_to = 'profile_pic/', default = 'profile_pic/default_pic.png')
    
    
    

