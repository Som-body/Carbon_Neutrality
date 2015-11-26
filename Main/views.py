from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from django.contrib import auth
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

from .forms import CNRegistrationForm
from .models import CarouselSlide

class IndexView(generic.ListView):
    template_name = "Main/index.html"
    context_object_name = 'slides'
    
    def get_queryset(self):
        return CarouselSlide.objects.all()
 
def login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        
        else:
            args = {}
            args.update(csrf(request))
            args['error_message'] = "Invalid username and password combination"
            return render_to_response('Main/login.html', args)
        
    else:
        c = {}
        c.update(csrf(request))
        return render_to_response('Main/login.html', c)
    
def logout(request):
    auth.logout(request)
    return render_to_response('Main/logout.html')
   
class SignUpView(FormView):
    template_name = 'Main/signup.html'
    form_class = CNRegistrationForm
    success_url = '/'
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(SignUpView, self).form_valid(form)

            
    
