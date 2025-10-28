from django.shortcuts import render
from .models import Kenshi


def kenjutsuka(request):
    kenjutsuka = Kenshi.objects.all().order_by('-date', '-created_at')
    return render(request, 'kenshi/kenshi.html', {
        'kenjutsuka': kenjutsuka,
    })
