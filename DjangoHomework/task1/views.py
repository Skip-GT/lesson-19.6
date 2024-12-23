from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News


def news(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 3)
    page_number = request.GET.get('page')
    news_page = paginator.get_page(page_number)
    return render(request, 'fourth_task//news.html', {'news': news_page})
