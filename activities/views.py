from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect


def activities(request):
    return render(request, 'activities/activities.html')


def plan(request):
    return render(request, 'activities/plan.html')


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
