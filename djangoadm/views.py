from django.shortcuts import (get_object_or_404, render, redirect, HttpResponseRedirect)
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def landing(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Product.objects.all()
    return render(request, "landing.html", context)

def product(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Product.objects.get(id = id)
    context["reviews"] = Review.objects.filter(product_id = id)
    return render(request, "product.html", context)

def contact(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    form = ContactForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
        return redirect("/landingpageabout/")
          
    context['form']= form 
    return render(request, "contact.html", context)

def create_review(request): 
    if request.method == "POST":
        # add the dictionary during initialization 
        form = ReviewForm(request.POST) 
        print(form)
        if form.is_valid(): 
            form.save() 
            return redirect("landing") #landing ambil dari name= landing di urls.py
    # else:
    #     form = ReviewForm()
    # return render(request, "product.html", {'form':form}) #form warna merah dari form warna merah diatas, form warna hijau bebas

# def register(request):
#     return render(request, "register.html")

# def detail_review(request, id):
#     # dictionary for initial data with 
#     # field names as keys
#     context ={}
 
#     # add the dictionary during initialization
#     context["data"] = Review.objects.get(id = id)
         
#     return render(request, "product.html", context)

def custom_404(request, exception):
    return render(request, "404.html", status=404)

# signup page
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing')
    else:
        form = UserRegistrationForm()
    return render(request, 'landingpageregister.html', {'form': form})


# login page
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landing')  # Redirect to home page after login
    else:
        form = UserLoginForm()
    return render(request, 'landingpagelogin.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('landing')

def cart(request): 
    return render(request, "cart.html")