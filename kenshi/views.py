from django.shortcuts import render


def kenshi(request):
    return render(request, 'kenshi/kenshi.html')
