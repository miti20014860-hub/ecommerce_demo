from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from .models import Activity


def activities(request):
    activities = Activity.objects.all().order_by('-created_at')

    paginator = Paginator(activities, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    return render(request, 'activities/activities.html', {
        'activities': page_obj,
        'page_obj': page_obj,
    })


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
