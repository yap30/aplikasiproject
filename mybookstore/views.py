from django.shortcuts import (get_object_or_404, render, redirect, HttpResponseRedirect)
from .models import *

# Create your views here.
def book_catalog(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["tabelbuku"] = tabelbuku.objects.all()
    return render(request, "book_catalog_mybookstore.html", context)