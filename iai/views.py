from django.shortcuts import render


def iai(request):
    return render(request, 'iai/iai.html')
