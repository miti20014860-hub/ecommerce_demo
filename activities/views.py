from django.shortcuts import render


def activities(request):
    return render(request, 'activities/activities.html')
