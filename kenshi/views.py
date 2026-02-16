from django.shortcuts import render
from .models import Kenshi


def kenshi(request):
    kenshi = Kenshi.objects.all().order_by('-created_at')
    return render(request, 'kenshi/kenshi.html', {
        'kenshi': kenshi,
    })
