from django.db import models

class CarouselSlide(models.Model):
    url = models.CharField(max_length = 255, default = '')
    image = models.ImageField(upload_to = 'pictures/')
    
    def __str__(self):
        return self.image.url
    

