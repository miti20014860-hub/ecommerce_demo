from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.utils import timezone
from datetime import datetime
from .models import Activity


def activities(request):
    activities = Activity.objects.all().order_by('-created_at')

    # === 1. 文字搜尋 ===
    query = request.GET.get('q', '').strip()
    if query:
        activities = activities.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(provider__icontains=query)
        )

    # === 2. Activity Type (多選) ===
    type_filters = request.GET.getlist('type')
    if type_filters:
        activities = activities.filter(type__in=type_filters)

    # === 3. Prefecture (只有縣市多選) ===
    prefecture_filters = request.GET.getlist('prefecture')  # 只有縣市

    selected_prefectures = prefecture_filters  # 直接使用

    if selected_prefectures:
        activities = activities.filter(prefecture__in=selected_prefectures)

    # === 4. Event Ends (日期篩選) ===
    event_ends = request.GET.get('event_ends', '').strip()
    if event_ends:
        try:
            filter_date = datetime.strptime(event_ends, '%Y-%m-%d').date()
            activities = activities.filter(event_ends__gte=filter_date)
        except ValueError:
            pass  # 無效日期忽略

    # === 5. Minimum Charge (數字範圍) ===
    charge_min = request.GET.get('charge_min', '').strip()
    charge_max = request.GET.get('charge_max', '').strip()

    if charge_min:
        try:
            activities = activities.filter(
                Q(minimum_charge__regex=r'^\d+$') |
                Q(minimum_charge__regex=r'^\d+[,]\d+$'),
                minimum_charge__gte=int(charge_min.replace(',', ''))
            )
        except:
            pass

    if charge_max:
        try:
            activities = activities.filter(
                Q(minimum_charge__regex=r'^\d+$') |
                Q(minimum_charge__regex=r'^\d+[,]\d+$'),
                minimum_charge__lte=int(charge_max.replace(',', ''))
            )
        except:
            pass

    # === 排序 ===
    activities = activities.order_by('-created_at')

    # === 分頁 ===
    paginator = Paginator(activities, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # === 傳遞給模板 ===
    context = {
        'activities': page_obj,
        'page_obj': page_obj,
        'query': query,
        'type_filters': type_filters,
        'event_ends': event_ends,
        'charge_min': charge_min,
        'charge_max': charge_max,
        'type_choices': Activity.Type_CHOICES,
        'selected_prefectures': selected_prefectures,  # 用於 checked
        # 供模板使用
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

    return render(request, 'activities/activities.html', context)


def plan(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'activities/plan.html', {'activity': activity})


@require_POST
@csrf_protect
def booking(request):
    if request.method == 'POST':
        activity = request.POST.get('activity')
        full_name = request.POST.get('full_name')
        email_address = request.POST.get('email_address')
        prefer_date = request.POST.get('prefer_date')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        messages.success(request, f"Booking for {activity} on {prefer_date} submitted!")
    return render(request, 'activities/plan.html')
