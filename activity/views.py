from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal, InvalidOperation
from django.core.paginator import Paginator
from django.utils.http import urlencode
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from .models import Activity
from .forms import BookingForm


def activity(request):
    activities = Activity.objects.all().order_by('-created_at')

    # === 1. Text ===
    query = request.GET.get('q', '').strip()
    if query:
        activities = activities.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(provider__icontains=query)
        )

    # === 2. Activity Type  ===
    type_filters = request.GET.getlist('type')
    if type_filters:
        activities = activities.filter(type__in=type_filters)

    # === 3. Prefecture  ===
    prefecture_filters = request.GET.getlist('prefecture')

    selected_prefectures = prefecture_filters

    if selected_prefectures:
        activities = activities.filter(prefecture__in=selected_prefectures)

    # === 4. Event Ends ===
    event_ends = request.GET.get('event_ends', '').strip()
    if event_ends:
        try:
            filter_date = datetime.strptime(event_ends, '%Y-%m-%d').date()
            activities = activities.filter(event_ends__gte=filter_date)
        except ValueError:
            pass

    # === 5. Price===
    charge_min = request.GET.get('charge_min', '').strip()
    charge_max = request.GET.get('charge_max', '').strip()

    if charge_min:
        clean_min = charge_min.replace(',', '').strip()
        if clean_min:
            try:
                min_val = Decimal(clean_min)
                activities = activities.filter(minimum_charge__gte=min_val)
            except (InvalidOperation, ValueError, TypeError):
                pass

    if charge_max:
        clean_max = charge_max.replace(',', '').strip()
        if clean_max:
            try:
                max_val = Decimal(clean_max)
                activities = activities.filter(minimum_charge__lte=max_val)
            except (InvalidOperation, ValueError, TypeError):
                pass

    # === Ordering ===
    activities = activities.order_by('-updated_at')

    # === Paginator ===
    paginator = Paginator(activities, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # === Templates ===
    context = {
        'activities': page_obj,
        'page_obj': page_obj,
        'query': query,
        'type_filters': type_filters,
        'event_ends': event_ends,
        'charge_min': charge_min,
        'charge_max': charge_max,
        'type_choices': Activity.Type_CHOICES,
        'selected_prefectures': selected_prefectures,
        'region_groups': [
            {'value': 'hokkaido', 'label': 'Hokkaido', 'prefectures': Activity.HOKKAIDO},
            {'value': 'tohoku', 'label': 'Tohoku', 'prefectures': Activity.TOHOKU},
            {'value': 'kanto', 'label': 'Kanto', 'prefectures': Activity.KANTO},
            {'value': 'chubu', 'label': 'Chubu', 'prefectures': Activity.CHUBU},
            {'value': 'kansai', 'label': 'Kansai', 'prefectures': Activity.KANSAI},
            {'value': 'chugoku', 'label': 'Chugoku', 'prefectures': Activity.CHUGOKU},
            {'value': 'shikoku', 'label': 'Shikoku', 'prefectures': Activity.SHIKOKU},
            {'value': 'kyushu_okinawa', 'label': 'Kyushu & Okinawa', 'prefectures': Activity.KYUSHU_OKINAWA},
        ],

    }

    current_query = request.GET.copy()
    if 'page' in current_query:
        del current_query['page']
    clean_query = {}
    for key, value in current_query.lists():
        if value and (value != [''] and value != ['[]']):
            clean_query[key] = value
    context['current_query'] = urlencode(clean_query, doseq=True)

    return render(request, 'activity/activity.html', context)


def plan(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'activity/plan.html', {'activity': activity})


def booking_view(request, pk):
    activity = get_object_or_404(Activity, pk=pk)

    if request.method == "POST":
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.activity = activity.title
            booking.user = request.user if request.user.is_authenticated else None
            booking.activity_obj = activity
            booking.save()
            messages.success(request, "Your booking has been submitted successfully!")
            return redirect('activity:plan', pk=pk)
    else:
        form = BookingForm(user=request.user)

    return render(request, 'activity/plan.html', {'form': form, 'activity': activity, })
