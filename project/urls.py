from django.urls import path
from . import views


app_name = 'project'
urlpatterns = [
    path('service/', views.serviceListView, name='service-list'),
    path('service/detail/<int:pk>', views.serviceDetailView, name='service-detail'),
    path('sample/', views.worksampleView, name='sample-list'),
    path('sample/detail/<int:pk>', views.worksampleDetailView, name='sample-detail'),
]