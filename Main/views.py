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

from .forms import CNRegistrationForm
from .models import CarouselSlide, UserModel
from django.views.generic.detail import DetailView

class IndexView(generic.ListView):
    template_name = "Main/index.html"
    context_object_name = 'slides'
    
    def get_queryset(self):
        return CarouselSlide.objects.all()
 
def login(request):
    redirect_to = request.REQUEST.get('next', '/')
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

def finish_sign_up(request):
    redirect_to = request.REQUEST.get('next', '/')
    if request.user.is_authenticated():
        if not UserModel.objects.filter(user = request.user):
            UserModel.objects.create(user = request.user)
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

            
    
