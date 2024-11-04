from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from blog.models import Article
from khayyam import JalaliDatetime



def articleListView(request):
    articles = Article.objects.all()
    for article in articles:
        jalali_date = JalaliDatetime(article.created).strftime('%d %B %Y، ساعت %H:%M')
        article.jalali_created = jalali_date
    page_num = request.GET.get('page')
    paginator = Paginator(articles, 9)
    objects_list = paginator.get_page(page_num)
    return render(request, 'blog/blog.html', {'articles': objects_list})


def articleDetailView(request, pk):
    article = get_object_or_404(Article, id=pk)
    jalali_date = JalaliDatetime(article.created).strftime('%d %B %Y، ساعت %H:%M')
    article.jalali_created = jalali_date
    return render(request, 'blog/blog-detail.html', {'article': article})

