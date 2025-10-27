from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from .models import Collection  # 匯入模型


def collection(request):
    collections = Collection.objects.all()
    return render(request, 'collection/collection.html', {
        'collections': collections
    })


def item(request):
    pk = request.GET.get('id')
    if not pk:
        # 修正：Rcrender → render
        return render(request, 'collection/item.html')
    collection = get_object_or_404(Collection, pk=pk)
    return render(request, 'collection/item.html', {
        'collection': collection
    })


def form(request):
    return render(request, 'collection/form.html')


@require_POST
@csrf_protect
def order_form(request):
    payment_method = request.POST.get('payment_method')
    # 可加入簡單驗證
    if not payment_method:
        messages.error(request, "請選擇付款方式")
    else:
        messages.success(request, f"已提交訂單，付款方式：{payment_method}")
    return render(request, 'collection/form.html')
