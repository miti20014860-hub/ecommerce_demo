from django.shortcuts import render


def activities(request):
    return render(request, 'activities/activities.html')


def plan(request):
    return render(request, 'activities/plan.html')
