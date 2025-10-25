from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


def member(request):
    return render(request, 'member/member.html')


def account(request):
    return render(request, 'member/account.html')


@require_POST
@csrf_protect
def sign_in(request):
    if request.method == 'POST':
        acc_name = request.POST.get('acc_name')
        acc_password = request.POST.get('acc_password')
        user = auth.authenticate(username=acc_name, password=acc_password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged In')
            return redirect('member:account')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('member:member')
    else:
        return render(request, 'index/index.html')


@require_POST
@csrf_protect
def sign_up(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')
        user_password_re = request.POST.get('user_password_re')
        if user_password == user_password_re:
            if User.objects.filter(name=user_name).exists():
                messages.error(request, f'Username already registered')
                return redirect('member:member')
            else:
                user = User.objects.create_user(username=user_name, email=user_email, password=user_password)
                user.save()
                messages.success(request, f'Successfully Created')
            return render(request, 'member/account.html')
        else:
            messages.error(request, f'Password do not match')
            return redirect('member:member')
    else:
        return render(request, 'index/index.html')


@require_POST
@csrf_protect
def sign_out(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('index:index')


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
