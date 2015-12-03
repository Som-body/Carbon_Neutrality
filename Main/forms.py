from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from .models import Tree, UserModel

class CNRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form_input', 'placeholder' : "Username", "maxlength" : '30'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control form_input', 'placeholder' : "Email Address"}))
    first = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form_input', 'placeholder' : "First Name"}))
    last = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form_input', 'placeholder' : "Last Name"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form_input', 'placeholder' : "Password", "maxlength" : '30'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control form_input', 'placeholder' : "Confirm Password", "maxlength" : '30'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first', 'last', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first']
        user.last_name = self.cleaned_data['last']
        
        if commit:
            user.save()
        return user

class TreeForm(forms.ModelForm):
    species = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form_input', 'placeholder' : "Species", "maxlength" : '50'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form_input', 'placeholder' : "Location", "maxlength" : '50'}))
    longitude = forms.DecimalField(widget=forms.NumberInput(attrs={'class' : 'form-control form_input', 'placeholder' : "Longitude (-180 to 180)", 'min' : "-180", 'max' : "180"}))
    latitude = forms.DecimalField(widget=forms.NumberInput(attrs={'class' : 'form-control form_input', 'placeholder' : "Latitude (-90 to 90)", 'min' : "-90", 'max' : "90"}))
    date_planted = forms.DateField(widget=forms.DateInput(attrs={'class' : 'form-control form_input', 'placeholder' : "Date (YYYY-MM-DD)"}), initial = timezone.now())
    adult_diameter = forms.DecimalField(widget=forms.NumberInput(attrs={'class' : 'form-control form_input', 'placeholder' : "Adult Diameter", 'min' : "0"}), initial='/media/trees/tree101.png')
    picture = forms.ImageField(widget=forms.FileInput(attrs={'accept' : 'image/*'}), required = False)
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TreeForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Tree
        fields = ['species', 'location', 'longitude', 'latitude', 'date_planted', 'adult_diameter', 'picture']
        exclude = ('user', 'is_alive')
        
    def save(self, commit=True):
        tree = super(TreeForm, self).save(commit=False)
        tree.user = self.user
        tree.species = self.cleaned_data['species']
        tree.location = self.cleaned_data['location']
        tree.longitude = self.cleaned_data['longitude']
        tree.latitude = self.cleaned_data['latitude']
        tree.date_planted = self.cleaned_data['date_planted']
        tree.adult_diameter = self.cleaned_data['adult_diameter']
        if self.cleaned_data['picture']:
            tree.picture = self.cleaned_data['picture']
            
        if commit:
            tree.save()
        return tree
    

    
    