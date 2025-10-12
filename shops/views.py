from django.shortcuts import render


def shops(request):
    return render(request, 'shops/shops.html')
