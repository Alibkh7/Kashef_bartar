from django.shortcuts import render
from django.views.generic import TemplateView
from project.models import Service
from blog.models import Article



def homeView(request):
    services = Service.objects.order_by('-created')[:6]
    articles = Article.objects.order_by('-created')[:6]
    return render(request, 'home/index.html', {'services': services, 'articles': articles})
