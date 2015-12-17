from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from django.contrib import auth
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import template
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from .forms import CNRegistrationForm, TreeForm
from .models import CarouselSlide, UserModel, Friend, Tree

from decimal import *
from PIL import Image

class IndexView(generic.ListView):
    template_name = "Main/index.html"
    context_object_name = 'slides'
    
    def get_queryset(self):
        
        return CarouselSlide.objects.all()
 
def login(request):
    redirect_to = request.REQUEST.get('next', '/')
    
    if request.user.is_authenticated():
        return HttpResponseRedirect(redirect_to)
    else:
        if request.method == "POST":
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(redirect_to)
            
            else:
                args = locals()
                args.update(csrf(request))
                args['error_message'] = "Invalid username and password combination"
                return render_to_response('Main/login.html', args)
            
        else:
            args = locals()
            args.update(csrf(request))
            return render_to_response('Main/login.html', args)
    
def logout(request):
    redirect_to = request.REQUEST.get('next', '/')
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect(redirect_to)
   
class SignUpView(FormView):
    template_name = 'Main/signup.html'
    form_class = CNRegistrationForm 
    
    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        context['next_url'] = self.request.GET.get('next') 
        return context
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return '/finish_sign_up/?next=' + next_url 
        return '/finish_sign_up/' 
    
    def form_valid(self, form):
        form.save()
        user = auth.authenticate(username = self.request.POST.get('username'), 
                                 password = self.request.POST.get('password1'))    
        auth.login(self.request, user)
        return super(SignUpView, self).form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(request.REQUEST.get('next', '/'))
        else:
            return super(SignUpView, self).dispatch(request, *args, **kwargs)

def finish_sign_up(request):
    redirect_to = request.REQUEST.get('next', '/')
    if request.user.is_authenticated():
        if not UserModel.objects.filter(user = request.user):
            user_model = UserModel.objects.create(user = request.user)
            user_model.save()
            Friend.objects.create(user = request.user, friend = request.user, friend_model = user_model).save()
    return HttpResponseRedirect(redirect_to)

def AccountView(request, username):
    u = get_object_or_404(User, username = username)
    user = request.user
    args = locals()
    args.update(csrf(request))
    args['slides'] = CarouselSlide.objects.all()
    args['profile_user'] = u
    if user.is_authenticated():
        args['user'] = user
        args['friend'] = Friend.objects.filter(user = user, friend = u)
    userdata = UserModel.objects.get(user = u)
    args['userdata'] = userdata
    args['users'] = UserModel.objects.all()[:20]
    return render_to_response('Main/account.html', args)


class TreeView(FormView):
    template_name = 'Main/tree.html'
    form_class = TreeForm
    
    def get_form_kwargs(self, *args, **kwargs):
        return dict(
            super(TreeView, self).get_form_kwargs(*args, **kwargs),
            **{'user': self.request.user}
        )
        
    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        context['user'] = self.request.user 
        return context
    
    def get_success_url(self):
        user_page = self.request.user.get_username()
        if user_page:
            return '/user/' + user_page 
        return '/' 
    
    def form_valid(self, form):
        tree = form.save()
        user_model = UserModel.objects.get(user = tree.user)
        user_model.offset += tree.get_lifetime_offset()
        user_model.net_emission = user_model.get_net_emission()
        user_model.save()
        
        return super(TreeView, self).form_valid(form)
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TreeView, self).dispatch(*args, **kwargs)
    
@login_required
def edit_profile(request):
    if request.POST:
        user = request.user                   
        if request.POST.get('first_name'):
            user.first_name = request.POST.get('first_name')
        if request.POST.get('last_name'):
            user.last_name = request.POST.get('last_name')
        if request.POST.get('email'):
            user.email = request.POST.get('email') 
        if request.FILES.get('picture'):
            user_model = UserModel.objects.get(user = user)
            user_model.profile_img = request.FILES.get('picture')
            user_model.save()
        user.save()

        return HttpResponseRedirect('/user/' + user.get_username())            
    
    else:
        user = request.user
        args = locals()
        args.update(csrf(request))
        args['user'] = user
        userdata = UserModel.objects.get(user = user)
        args['userdata'] = userdata
        return render_to_response('Main/edit_profile.html', args)

@login_required
def change_password(request):
    user = request.user
    if request.POST:
        
        if user.check_password(str(request.POST.get('old_password'))) and (request.POST.get('new_password') == request.POST.get('confirm')):
            user.set_password(request.POST.get('new_password'))                  
            user.save()
            return HttpResponseRedirect('/user/' + user.get_username())
        else:
            args = locals()
            args.update(csrf(request))
            args['user'] = user
            userdata = UserModel.objects.get(user = user)
            args['userdata'] = userdata
            args['error_message'] = 'Changes not applied. Please check your old password'
            return render_to_response('Main/change_password.html', args)
  
                
                    
    else:
        
        args = locals()
        args.update(csrf(request))
        args['user'] = user
        userdata = UserModel.objects.get(user = user)
        args['userdata'] = userdata
        return render_to_response('Main/change_password.html', args)


@login_required
def friend_user(request):
    friend = User.objects.filter(username = request.REQUEST.get('friend'))
    user = request.user
    
    if friend:
        friend = friend[0]
        friendship = Friend.objects.create(user = user, friend = friend, friend_model = UserModel.objects.get(user = friend))
        reverse_friendship = Friend.objects.create(user = friend, friend = user, friend_model = UserModel.objects.get(user = user))
        friendship.save()
        reverse_friendship.save()

    return HttpResponseRedirect('/user/' + friend.get_username())

@login_required 
def unfriend_user(request):
    friend = User.objects.filter(username = request.REQUEST.get('friend'))
    user = request.user
    if friend:
        friend = friend[0]
        friendship = Friend.objects.filter(user = user, friend = friend)
        reverse_friendship = Friend.objects.filter(user = friend, friend = user)
        if friendship:
            friendship.delete()
            reverse_friendship.delete()
    
    return HttpResponseRedirect('/user/' + friend.get_username())

@login_required
def find_friend(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        friend = User.objects.filter(username=username)
            
        if friend:
            friend = friend[0]
            friendship = Friend.objects.filter(user = request.user, friend = friend)
            if not friendship:
                return HttpResponseRedirect('/friend_user/?friend=' + friend.get_username())
            else:
                args = locals()
                args.update(csrf(request))
                args['user'] = request.user
                args['error_message'] = "You are already friends with that user"
                return render_to_response('Main/find_friend.html', args)
            
        else:
            args = locals()
            args.update(csrf(request))
            args['user'] = request.user
            args['error_message'] = "A person with this username does not exist"
            return render_to_response('Main/find_friend.html', args)
            
    else:
        args = locals()
        args.update(csrf(request))
        args['user'] = request.user
        return render_to_response('Main/find_friend.html', args)

def carbon_emissions(request):
    user = request.user
    if request.POST:
        if user.is_authenticated():
            user_model = UserModel.objects.filter(user = user)
            print('test1')
            if user_model:
                print('test2')
                user_model = user_model[0]
                if request.POST.get('car_miles') and request.POST.get('car_efficiency') and request.POST.get('car_fuel'):
                    user_model.precal_car_efficiency = int(request.POST.get('car_efficiency'))
                    user_model.car_efficiency = Decimal(str(user_model.precal_car_efficiency))
                    user_model.precal_fuel_type = request.POST.get('car_fuel')
                    if user_model.precal_fuel_type == 'Gasoline':
                        user_model.fuel_emission = Decimal('8874')
                    else:
                        user_model.fuel_emission = Decimal('10153')
                    user_model.precal_car = int(request.POST.get('car_miles'))
                    user_model.car_emissions = (Decimal(str(user_model.precal_car)) / user_model.car_efficiency) * user_model.fuel_emission
                if request.POST.get('bus_miles'):
                    user_model.precal_bus = int(request.POST.get('bus_miles'))
                    user_model.bus_emissions = Decimal(str(user_model.precal_bus)) * Decimal('300')
                if request.POST.get('train_miles'):
                    user_model.precal_train = int(request.POST.get('train_miles'))
                    user_model.train_emissions = Decimal(str(user_model.precal_train)) * Decimal('163')
                if request.POST.get('flight_miles'):
                    user_model.precal_plane = int(request.POST.get('flight_miles'))
                    user_model.plane_emissions = Decimal(str(user_model.precal_plane)) * Decimal('223')
                    
                if request.POST.get('housing_electricity'):
                    user_model.precal_electricity = int(request.POST.get('housing_electricity'))
                    user_model.electricity_emissions = Decimal(str(user_model.precal_electricity)) * Decimal('835')
                if request.POST.get('housing_fuel'):
                    user_model.precal_fuel = int(request.POST.get('housing_fuel'))
                    user_model.fuel_emissions = Decimal(str(user_model.precal_fuel)) * Decimal('682')
                if request.POST.get('housing_gas'):
                    user_model.precal_gas = int(request.POST.get('housing_gas'))
                    user_model.gas_emissions = Decimal(str(user_model.precal_gas)) * Decimal('54.7')
                if request.POST.get('housing_water'):
                    user_model.precal_water = int(request.POST.get('housing_water'))
                    user_model.water_emissions = Decimal(str(user_model.precal_water)) * Decimal('11707')
                
                if request.POST.get('food_general_meat'):
                    user_model.precal_general_meat = int(request.POST.get('food_general_meat'))
                    user_model.general_meat_emissions = Decimal(str(user_model.precal_general_meat)) * Decimal('6.09') * Decimal('52')
                if request.POST.get('food_poultry'):
                    user_model.precal_poultry = int(request.POST.get('food_poultry'))
                    user_model.poultry_emissions = Decimal(str(user_model.precal_poultry)) * Decimal('4.27') * Decimal('52')
                if request.POST.get('food_seafood'):
                    user_model.precal_seafood = int(request.POST.get('food_seafood'))
                    user_model.seafood_emissions = Decimal(str(user_model.precal_seafood)) * Decimal('5.71') * Decimal('52')
                if request.POST.get('food_vegetables'):
                    user_model.precal_vegetable = int(request.POST.get('food_vegetables'))
                    user_model.vegetable_emissions = Decimal(str(user_model.precal_vegetable)) * Decimal('3.35') * Decimal('52')
                if request.POST.get('food_milk'):
                    user_model.precal_milk = int(request.POST.get('food_milk'))
                    user_model.milk_emissions = Decimal(str(user_model.precal_milk)) * Decimal('4') * Decimal('52')
                if request.POST.get('food_drinks'):
                    user_model.precal_drink = int(request.POST.get('food_drinks'))
                    user_model.drink_emissions = Decimal(str(user_model.precal_drink)) * Decimal('2.24') * Decimal('52')
                    
                if request.POST.get('shopping_clothes'):
                    user_model.precal_clothes = int(request.POST.get('shopping_clothes'))
                    user_model.clothes_emissions = Decimal(str(user_model.precal_clothes)) * Decimal('750') * Decimal('12')
                if request.POST.get('shopping_furniture'):
                    user_model.precal_furniture = int(request.POST.get('shopping_furniture'))
                    user_model.furniture_emissions = Decimal(str(user_model.precal_furniture)) * Decimal('614') * Decimal('12')
                if request.POST.get('shopping_health_care'):
                    user_model.precal_health = int(request.POST.get('shopping_health_care'))
                    user_model.health_emissions = Decimal(str(user_model.precal_health)) * Decimal('696') * Decimal('12')
                if request.POST.get('shopping_vehicles'):
                    user_model.precal_vehicle = int(request.POST.get('shopping_vehicles'))
                    user_model.vehicle_emissions = Decimal(str(user_model.precal_vehicle)) * Decimal('558') * Decimal('12')
                if request.POST.get('shopping_house_maintenance'):
                    user_model.precal_house = int(request.POST.get('shopping_house_maintenance'))
                    user_model.house_emissions = Decimal(str(user_model.precal_house)) * Decimal('954') * Decimal('12')
                
                user_model.emissions = user_model.get_emissions()
                user_model.net_emission = user_model.get_net_emission()
                user_model.save()
                return HttpResponseRedirect('/user/' + user.get_username())
            else:
                return HttpResponseRedirect('/signup/?next=' + request.path) 
            
        else:
            args = locals()
            args.update(csrf(request))
            args['user'] = user
            return HttpResponseRedirect('/signup/?next=' + request.path)    
                    
    else:
        
        args = locals()
        args.update(csrf(request))
        args['user'] = user
        if user.is_authenticated():
            userdata = UserModel.objects.get(user = user)
            args['userdata'] = userdata
        return render_to_response('Main/carbon_emissions.html', args)

def about(request):
    return render_to_response('Main/about.html')

def tree_detail(request, pk):
    tree = get_object_or_404(Tree, id = pk)
    user = request.user
    args = locals()
    args['user'] = user
    args['tree'] = tree
    return render_to_response('Main/tree_detail.html', args)
            
def tree_edit(request, pk):
    tree = get_object_or_404(Tree, id = pk)
    user = request.user
    if user != tree.user:
        return HttpResponseRedirect('/tree/' + pk + '/')
    else:
        if request.POST:
            if request.POST.get('species'):
                tree.species = request.POST.get('species')
            if request.POST.get('location'):
                tree.location = request.POST.get('location')
            if request.POST.get('longitude'):
                tree.longitude = Decimal(str(request.POST.get('longitude')))
            if request.POST.get('latitude'):
                tree.latitude = Decimal(str(request.POST.get('latitude')))
            if request.POST.get('adult_diameter'):
                user_model = UserModel.objects.get(user = user)
                user_model.offset -= tree.get_lifetime_offset()
                tree.adult_diameter = Decimal(str(request.POST.get('adult_diameter')))
                tree.save()
                user_model.offset += tree.get_lifetime_offset()
                user_model.net_emission = user_model.get_net_emission()
                user_model.save()
            if request.FILES.get('picture'):
                tree.picture = request.FILES.get('picture')
                
            tree.save()
            return HttpResponseRedirect('/tree/' + pk + '/')  
         
        else:
            args = locals()
            args.update(csrf(request))
            args['user'] = user
            args['tree'] = tree
            return render_to_response('Main/tree_edit.html', args)
