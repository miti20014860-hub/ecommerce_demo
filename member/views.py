from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .forms import ProfileEditForm


def member(request):
    return render(request, 'member/member.html')


@login_required
def account(request):
    profile_form = ProfileEditForm(request.user, instance=request.user)
    password_form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        if 'profile_submit' in request.POST:
            profile_form = ProfileEditForm(request.user, request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('member:account')

        elif 'password_submit' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password updated successfully.')
                return redirect('member:account')

    context = {
        'profile_form': profile_form,
        'password_form': password_form,
    }
    return render(request, 'member/account.html', context)


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


def sign_up(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')
        user_password_re = request.POST.get('user_password_re')
        if user_password == user_password_re:
            if User.objects.filter(name=user_name).exists():
                messages.error(request, 'Username already registered')
                return redirect('member:member')
            else:
                user = User.objects.create_user(username=user_name, email=user_email, password=user_password)
                user.save()
                messages.success(request, 'Successfully Created')
            return render(request, 'member/account.html')
        else:
            messages.error(request, 'Password do not match')
            return redirect('member:member')
    else:
        return render(request, 'index/index.html')


@login_required
def sign_out(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('index:index')
