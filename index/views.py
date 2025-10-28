from django.shortcuts import render, get_object_or_404
from .models import Notice
from .models import News


def index(request):
    newses = News.objects.all().order_by('-date', '-created_at')
    notices = Notice.objects.all().order_by('-date', '-created_at')
    return render(request, 'index/index.html', {
        'newses': newses,
        'notices': notices
    })


def news(request, pk):
    news = get_object_or_404(Notice, pk=pk)
    return render(request, 'index/news.html', {
        'news': news
    })


def notice(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'index/notice.html', {
        'notice': notice
    })


def about(request):
    return render(request, 'index/about.html')


def privacy(request):
    return render(request, 'index/privacy.html')


def contact(request):
    return render(request, 'index/contact.html')


def terms(request):
    return render(request, 'index/terms.html')


def faq(request):
    return render(request, 'index/faq.html')
