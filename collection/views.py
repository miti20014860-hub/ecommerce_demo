from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import Collection


def collection(request):
    # 1. 初始 queryset
    collections = Collection.objects.all().order_by('-created_at', 'name_en')

    # 2. 取得所有可能的 GET 參數
    query = request.GET.get('q', '').strip()
    type_filters = request.GET.getlist('type')
    period_filters = request.GET.getlist('period_type')
    blade_min = request.GET.get('blade_length_min', '').strip()
    blade_max = request.GET.get('blade_length_max', '').strip()
    price_min = request.GET.get('price_min', '').strip()
    price_max = request.GET.get('price_max', '').strip()

    # -------------------------------------------------
    # 3. 只要有任何篩選條件，就執行過濾
    # -------------------------------------------------
    if query:
        collections = collections.filter(
            Q(period__icontains=query) |
            Q(name_jp__icontains=query) |
            Q(name_en__icontains=query) |
            Q(remarks__icontains=query) |
            Q(provider__icontains=query) |
            Q(signature__icontains=query)
        )

    if type_filters:
        collections = collections.filter(type__in=type_filters)

    if period_filters:
        collections = collections.filter(period_type__in=period_filters)

    if blade_min:
        try:
            collections = collections.filter(blade_length__gte=float(blade_min))
        except ValueError:
            pass

    if blade_max:
        try:
            collections = collections.filter(blade_length__lte=float(blade_max))
        except ValueError:
            pass

    if price_min:
        try:
            collections = collections.filter(price__gte=float(price_min))
        except ValueError:
            pass

    if price_max:
        try:
            collections = collections.filter(price__lte=float(price_max))
        except ValueError:
            pass

    # -------------------------------------------------
    # 5. 分頁（每頁 6 筆，與原本一致）
    # -------------------------------------------------
    paginator = Paginator(collections, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # -------------------------------------------------
    # 6. 傳給模板的 context
    # -------------------------------------------------
    context = {
        'collections': page_obj,          # 用於 {% for obj in page_obj %}
        'page_obj': page_obj,
        'query': query,
        'type_filters': type_filters,
        'period_filters': period_filters,
        'blade_min': blade_min,
        'blade_max': blade_max,
        'price_min': price_min,
        'price_max': price_max,

        # 下拉選單
        'type_choices':   Collection.TYPE_CHOICES,
        'period_choices': Collection.PERIOD_CHOICES,
    }

    # 只要有任何篩選條件，就使用搜尋模板；否則使用原本的列表模板
    template = 'collection/collection.html' if any([
        query, type_filters, period_filters,
        blade_min, blade_max, price_min, price_max
    ]) else 'collection/collection.html'

    return render(request, template, context)


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


def order_form(request):
    payment_method = request.POST.get('payment_method')
    # 可加入簡單驗證
    if not payment_method:
        messages.error(request, "請選擇付款方式")
    else:
        messages.success(request, f"已提交訂單，付款方式：{payment_method}")
    return render(request, 'collection/form.html')
