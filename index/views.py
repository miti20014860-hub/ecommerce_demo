from django.shortcuts import render


def index(request):
    return render(request, 'index/index.html')


def news(request):
    return render(request, 'index/news.html')


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
