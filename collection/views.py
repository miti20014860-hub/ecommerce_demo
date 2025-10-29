from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from .models import Collection


def collection_search(request):
    """
    搜尋 Collections：支援關鍵字 + 類型篩選 + 價格區間
    """
    # 所有資料
    collections = Collection.objects.all().order_by('-created_at', 'name_en')

    # 取得搜尋參數
    query = request.GET.get('q', '').strip()           # 關鍵字
    type_filter = request.GET.get('type', '').strip()  # 刀種
    min_price = request.GET.get('min_price', '').strip()
    max_price = request.GET.get('max_price', '').strip()

    # === 關鍵字搜尋（多欄位）===
    if query:
        collections = collections.filter(
            Q(name_jp__icontains=query) |
            Q(name_en__icontains=query) |
            Q(provider__icontains=query) |
            Q(signature__icontains=query) |
            Q(period__icontains=query) |
            Q(koshirae__icontains=query) |
            Q(remarks__icontains=query)
        )

    # === 刀種篩選 ===
    if type_filter and type_filter in dict(Collection.TYPE_CHOICES):
        collections = collections.filter(type=type_filter)

    # === 價格區間 ===
    if min_price and min_price.isdigit():
        collections = collections.filter(price__gte=float(min_price))
    if max_price and max_price.isdigit():
        collections = collections.filter(price__lte=float(max_price))

    return render(request, 'collections/search.html', {
        'collections': collections,
        'query': query,
        'type_filter': type_filter,
        'min_price': min_price,
        'max_price': max_price,
        'count': collections.count(),
        'type_choices': Collection.TYPE_CHOICES,
    })


def collection(request):
    collections = Collection.objects.all().order_by('-created_at', 'name_en')

    paginator = Paginator(collections, 6)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    return render(request, 'collection/collection.html', {
        'collections': page_obj,
        'page_obj': page_obj,
        'type_choices': Collection.TYPE_CHOICES,
    })


def item(request):
    pk = request.GET.get('id')
    if not pk:
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
