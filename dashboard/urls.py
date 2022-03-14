from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('contactus/', views.contactus, name='contactus'),
    path('search/', views.search, name='search'),
    path('calender/', views.calender, name='calender'),

]
