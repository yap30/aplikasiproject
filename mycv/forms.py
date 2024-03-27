from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TestimoniForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Testimoni

        # specify fields to be used
        fields = [
            "Nama",
            "Profesi",
            "Deskripsi",
        ]