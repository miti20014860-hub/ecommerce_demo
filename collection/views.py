from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect


def collection(request):
    return render(request, 'collection/collection.html')


def item(request):
    return render(request, 'collection/item.html')


def form(request):
    return render(request, 'collection/form.html')


@require_POST
@csrf_protect
def order_form(request):
    payment_method = request.POST.get('payment_method')

    return render(request, 'collection/form.html')
