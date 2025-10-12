from django.shortcuts import render


def kenjutsu(request):
    return render(request, 'kenjutsu/kenjutsu.html')
