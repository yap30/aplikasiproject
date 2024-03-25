from django.urls import path
from . import views


urlpatterns = [
	path('webauth/', views.index, name ='index'),
    path('webauthcreate/', views.create_view, name='create view'),
    path('webauthlist/', views.list_view, name='list_view'),
    path('webauthlist1/', views.book_list, name='list_view'),
    path('webauthcreate1/', views.book_create, name='create view'),
    path('webauthlogin/', views.user_login, name='user_login'),
    path('webauthlogout/', views.user_logout, name='user_logout'),
    path('<id>/webauth/', views.detail_view, name='detail view'),
    path('<id>/webauth/updatebuku/', views.update_view, name='update view'),
    path('<id>/webauth/deletebuku/', views.delete_view,name='delete view'),
]