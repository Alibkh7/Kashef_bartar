from django.urls import path
from . import views



app_name = 'contactus_app'
urlpatterns = [
    path('', views.contact_view, name='contactus'),
    path('about', views.about_view, name='about'),
]