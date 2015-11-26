from django.contrib import admin

from .models import CarouselSlide

class CarouselSlideAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Content', {'fields': ['url', 'image']}),
    ]
    list_display = ('url', 'image')

admin.site.register(CarouselSlide, CarouselSlideAdmin)
