from django.shortcuts import (get_object_or_404, render, redirect, HttpResponseRedirect)
from .models import *
from. forms import *    

# Create your views here.
def testimoni(request):
    if request.method == "POST":
        # add the dictionary during initialization 
        form = TestimoniForm(request.POST) 
        print(form)
        print(form)
        if form.is_valid(): 
            form.save() 
            return redirect("mycv")
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["Testimoni"] = Testimoni.objects.all()
    context["Berita"] = Berita.objects.all()
    return render(request, "profile_mycv.html", context)

