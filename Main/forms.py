from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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