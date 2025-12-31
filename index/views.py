from django.shortcuts import render, get_object_or_404
from .models import Banner, Quotes, News, Notice


def index(request):
    featured_newses = News.objects.filter(is_featured=True).order_by('-created_at')[:2]
    recent_newses = News.objects.filter(is_featured=False).order_by('-created_at')[:7]

    context = {
        'featured_newses': featured_newses,
        'recent_newses': recent_newses,
        'banners': Banner.objects.filter(is_active=True),
        'quotes': Quotes.objects.filter(is_featured=True),
        'newses': News.objects.all().order_by('-created_at'),
        'notices': Notice.objects.all().order_by('-created_at'),
    }
    return render(request, 'index/index.html', context)


def news(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'index/news.html', {'news': news})


def notice(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'index/notice.html', {'notice': notice})


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

# index/views.py
# from django.shortcuts import render

# def index(request):
#     return render(request, 'base.html')

# def news(request, pk=None):
#     return render(request, 'base.html')

# def notice(request, pk=None):
#     return render(request, 'base.html')

# def about(request):
#     return render(request, 'base.html')

# def privacy(request):
#     return render(request, 'base.html')

# def contact(request):
#     return render(request, 'base.html')

# def terms(request):
#     return render(request, 'base.html')

# def faq(request):
#     return render(request, 'base.html')