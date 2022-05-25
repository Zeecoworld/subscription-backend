from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args , **kwargs):
        super().__init__(*args,**kwargs)
        self.fields["username"].widget.attrs.update({"class":"form-control","name":"username","placeholder":"Enter Your Username"})
        self.fields["first_name"].widget.attrs.update({"class":"form-control","name":"name","placeholder":"Enter First Name"})
        self.fields["last_name"].widget.attrs.update({"class":"form-control","name":"name","placeholder":"Enter Last Name"})
        self.fields["email"].widget.attrs.update({"class":"form-control","name":"email","placeholder":"Enter Your E-mail"})
        self.fields["wallet_address"].widget.attrs.update({"class":"form-control","name":"name","placeholder":"Enter Your USDT(TRC20) Public Wallet Address"})
        self.fields["password1"].widget.attrs.update({"class":"form-control","name":"password","placeholder":"Enter Your Password"})
        self.fields["password2"].widget.attrs.update({"class":"form-control","name":"password_confirmation","id":"InputRetypepassword","placeholder":"Re-type Password"})
    class Meta:
        model = User
        fields = ( "username", 
                  "first_name", 
                  "last_name",
                  "email",
                  "wallet_address", 
                  "password1", 
                  "password2" )

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['wallet_address']
        if commit:
            user.save()
        return user
