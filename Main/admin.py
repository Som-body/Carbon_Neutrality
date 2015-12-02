from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import CarouselSlide, UserModel, Tree, Friend

class UserModelInline(admin.StackedInline):
    model = UserModel

class TreeInline(admin.TabularInline):
    model = Tree
    extra = 0
    
class FriendInline(admin.TabularInline):
    model = Friend
    fk_name = 'user'
    extra = 0

class CarouselSlideAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Content', {'fields': ['url', 'image']}),
    ]
    list_display = ('url', 'image')
    
class UserAdmin(DjangoUserAdmin):
    inlines = [ UserModelInline, FriendInline, TreeInline, ]

admin.site.register(CarouselSlide, CarouselSlideAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)