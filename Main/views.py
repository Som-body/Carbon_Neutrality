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

from .forms import CNRegistrationForm, TreeForm
from .models import CarouselSlide, UserModel, Friend, Tree


register = template.Library()

@register.filter
def modulo(num, val):
    return num % val

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
            UserModel.objects.create(user = request.user)
            Friend.objects.create(user = request.user, friend = request.user).save()
    return HttpResponseRedirect(redirect_to)

def AccountView(request, username):
    u = User.objects.get(username=username)
    user = request.user
    args = locals()
    args.update(csrf(request))
    args['slides'] = CarouselSlide.objects.all()
    args['profile_user'] = u
    if user.is_authenticated():
        args['user'] = user
    userdata = UserModel.objects.get(user = u)
    args['userdata'] = userdata
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
        if request.FILES['picture']:
            user_model = UserModel.objects.get(user = user)
            user_model.profile_img = request.FILES['picture']
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
    if request.POST:
        user = request.user
        
        if user.check_password(str(request.POST.get('old_password'))) and (request.POST.get('new_password') == request.POST.get('confirm')):
            user.set_password(request.POST.get('new_password'))                  
            user.save()
            return HttpResponseRedirect('/user/' + user.get_username())
        else:
            
            user = request.user
            args = locals()
            args.update(csrf(request))
            args['user'] = user
            userdata = UserModel.objects.get(user = user)
            args['userdata'] = userdata
            return render_to_response('Main/change_password.html', args)
  
                
                    
    else:
        user = request.user
        args = locals()
        args.update(csrf(request))
        args['user'] = user
        userdata = UserModel.objects.get(user = user)
        args['userdata'] = userdata
        return render_to_response('Main/change_password.html', args)



            
    
