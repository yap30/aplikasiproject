# urls.py
from django.urls import path
from .views import BukuCreate
from .views import BukuList
from .views import BukuDetailView
from .views import BukuUpdateView
from .views import BukuDeleteView

urlpatterns = [

	path('about/', BukuCreate.as_view()),
    path('', BukuCreate.as_view()),
    path('listbuku/', BukuList.as_view()),
    # <pk> is identification for id field,
    # slug can also be used
    path('listbuku/<pk>/', BukuDetailView.as_view()),
    path('<pk>/updatebuku/', BukuUpdateView.as_view()),
    path('<pk>/deletebuku/', BukuDeleteView.as_view()),

]
