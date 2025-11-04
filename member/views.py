from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileEditForm, PasswordChangeForm, LoginForm, RegisterForm


def member(request):
    context = {
        'form': LoginForm(),
        'register_form': RegisterForm(),
    }
    return render(request, 'member/member.html', context)


def account_sign_in(request):
    if 'sign_in_submit' in request.POST:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged In')
            return redirect('member:account')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('member:member')
    else:
        form = LoginForm()
    return render(request, 'index/index.html', {
        'form': form,
        'register_form': RegisterForm()
    })


@login_required
def account(request):
    profile_form = ProfileEditForm(instance=request.user)
    password_form = PasswordChangeForm(user=request.user)

    if 'profile_submit' in request.POST:
        profile_form = ProfileEditForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('member:account')
        else:
            messages.error(request, 'Profile update failed')

    elif 'password_submit' in request.POST:
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password updated successfully')
            return redirect('member:account')
        else:
            messages.error(request, 'Password update failed')

    context = {
        'profile_form': profile_form,
        'password_form': password_form,
    }
    return render(request, 'member/account.html', context)


@login_required
def account_sign_out(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'Logged out successfully')
    return redirect('index:index')


def account_sign_up(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            messages.success(request, 'Successfully Created')
            login(request, user)
            return redirect('member:account')
        else:
            for field, errors in register_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return redirect('member:member')
    else:
        register_form = RegisterForm()
    return render(request, 'index/index.html', {
        'form': LoginForm(),
        'register_form': register_form
    })
