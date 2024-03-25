from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import BukuModel

class BukuCreate(CreateView):

    # specify the model for create view
    model = BukuModel

    success_url = "/listbuku/"

    # specify the fields to be displayed

    fields = ['title_book', 'description_book', 'date_book', 'author_book', 'file_book']

class BukuList(ListView):

    # specify the model for list view
    model = BukuModel

class BukuDetailView(DetailView):
    # specify the model to use
    model = BukuModel

class BukuUpdateView(UpdateView):
    # specify the model you want to use
    model = BukuModel

 
    # specify the fields
    fields = [
        "title_book",
        "description_book",
        "date_book",
        "author_book",
        "file_book",
    ]
 
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/listbuku/"

class BukuDeleteView(DeleteView):
    # specify the model you want to use
    model = BukuModel
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="/listbuku/"

    


