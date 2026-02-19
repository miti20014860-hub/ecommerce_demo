from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils.http import urlencode
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from .models import Collection
from .forms import OrderForm


def collection(request):
    collections = Collection.objects.all().order_by('-created_at', 'name_en')

    query = request.GET.get('q', '').strip()
    type_filters = request.GET.getlist('type')
    period_filters = request.GET.getlist('period_type')
    blade_min = request.GET.get('blade_length_min', '').strip()
    blade_max = request.GET.get('blade_length_max', '').strip()
    price_min = request.GET.get('price_min', '').strip()
    price_max = request.GET.get('price_max', '').strip()

    if query:
        collections = collections.filter(
            Q(period__icontains=query) |
            Q(name_jp__icontains=query) |
            Q(name_en__icontains=query) |
            Q(remarks__icontains=query) |
            Q(provider__icontains=query) |
            Q(signature__icontains=query)
        )

    if type_filters:
        collections = collections.filter(type__in=type_filters)

    if period_filters:
        collections = collections.filter(period_type__in=period_filters)

    if blade_min:
        try:
            collections = collections.filter(blade_length__gte=float(blade_min))
        except ValueError:
            pass

    if blade_max:
        try:
            collections = collections.filter(blade_length__lte=float(blade_max))
        except ValueError:
            pass

    if price_min:
        try:
            collections = collections.filter(price__gte=float(price_min))
        except ValueError:
            pass

    if price_max:
        try:
            collections = collections.filter(price__lte=float(price_max))
        except ValueError:
            pass

    paginator = Paginator(collections, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'collections': page_obj,
        'page_obj': page_obj,
        'query': query,
        'type_filters': type_filters,
        'period_filters': period_filters,
        'blade_min': blade_min,
        'blade_max': blade_max,
        'price_min': price_min,
        'price_max': price_max,

        'type_choices':   Collection.TYPE_CHOICES,
        'period_choices': Collection.PERIOD_CHOICES,
    }

    # Search or not
    template = 'collection/collection.html' if any([
        query, type_filters, period_filters,
        blade_min, blade_max, price_min, price_max
    ]) else 'collection/collection.html'

    current_query = request.GET.copy()
    if 'page' in current_query:
        del current_query['page']
    clean_query = {}
    for key, value in current_query.lists():
        if value and (value != [''] and value != ['[]']):
            clean_query[key] = value
    context['current_query'] = urlencode(clean_query, doseq=True)

    return render(request, template, context)


def item(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    return render(request, 'collection/item.html', {'collection': collection})


def order_form(request, pk):
    collection = get_object_or_404(Collection, pk=pk)

    if request.method == "POST":
        form = OrderForm(request.POST, user=request.user, collection=collection)
        if form.is_valid():
            order = form.save(commit=False)
            order.name_jp = collection.name_jp
            order.user = request.user if request.user.is_authenticated else None
            order.collection_obj = collection
            order.save()
            messages.success(request, "Your order has been submitted successfully!")
            return redirect('collection:item', pk=pk)
    else:
        form = OrderForm(user=request.user, collection=collection)

    return render(request, 'collection/form.html', {'form': form, 'collection': collection, })
