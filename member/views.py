from django.shortcuts import render


def member(request):
    return render(request, 'member/member.html')


def account(request):
    return render(request, 'member/account.html')
