from . import views
from django.urls import path, include


app_name = 'blog'
urlpatterns = [
    path('list', views.articleListView, name='blog_list'),
    path('detail/<int:pk>', views.articleDetailView, name='blog_detail'),
]
