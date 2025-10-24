from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect


def member(request):
    return render(request, 'member/member.html')


def account(request):
    return render(request, 'member/account.html')


def sing_in(request):
    if request.method == 'POST':
        email_address = request.POST.get('email_address')
        acc_password = request.POST.get('acc_password')
        messages.success(request, f"Logged In")
    return render(request, 'member/account.html')


@require_POST
@csrf_protect
def sing_up(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')
        user_password_re = request.POST.get('user_password_re')
        messages.success(request, f"Registered")
    return render(request, 'member/account.html')


@require_POST
@csrf_protect
def profile(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_phone = request.POST.get('user_password')
        user_addresses = request.POST.get('user_password')
        user_payment = request.POST.get('user_password_re')
        messages.success(request, f"Updated")
    return render(request, 'member/account.html')


@require_POST
@csrf_protect
def update_profile(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_phone = request.POST.get('user_password')
        user_addresses = request.POST.get('user_password')
        user_payment = request.POST.get('user_password_re')
        messages.success(request, f"Updated")
    return render(request, 'member/account.html')


@require_POST
@csrf_protect
def change_password(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_phone = request.POST.get('user_password')
        user_addresses = request.POST.get('user_password')
        user_payment = request.POST.get('user_password_re')
        messages.success(request, f"Updated")
    return render(request, 'member/account.html')
