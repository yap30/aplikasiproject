from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import BookModel
from .forms import BookForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_logout(request):
    logout(request)
    return redirect('user_login')

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid:
            book = form.save()
            book.save()
            return redirect('index')
    else:
        form = BookForm()
        return render(request, 'book_create.html', {'form': form})

@login_required
def book_list(request):
    books = BookModel.objects.all()
    return render(request, 'book_list.html', {'books':books})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'invalid username or password')
    return render(request, 'login.html')

@login_required
def create_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    form = BookForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
        return redirect("/webauthlist/")
          
    context['form']= form 
    return render(request, "book_create.html", context) 

@login_required
def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["books"] = BookModel.objects.all()
         
    return render(request, "book_list.html", context)

@login_required
# after updating it will redirect to detail_View
def detail_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["books"] = BookModel.objects.get(id = id)
          
    return render(request, "book_detail.html", context)

@login_required 
# update view for details
def update_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(BookModel, id = id)
 
    # pass the object as instance in form
    form = BookForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("/webauthlist/")
 
    # add form dictionary to context
    context["forms"] = form
 
    return render(request, "book_update.html", context)

@login_required
# delete view for details
def delete_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(BookModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/webauthlist/")
 
    return render(request, "book_delete.html", context)