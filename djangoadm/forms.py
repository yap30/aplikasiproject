from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# creating a form
class ContactForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Contact

        # specify fields to be used
        fields = [
            "contact_name",
            "contact_email",
            "message",
        ]

# creating a form
class ReviewForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Review

        # specify fields to be used
        fields = [
            "product_id",
            "customer_name",
            "customer_email",
            "customer_review",
            "rate",
        ]

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
