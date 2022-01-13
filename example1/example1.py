

from django.db.models import Q
from django.core import serializers
from django.htttp import JsonResponse


def live_search(request, template_name="shop/livesearch_results.html"):
    q = request.GET.get("q", "")
    data = Product.objects.filter(Q(sku__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))
    data = serializers.serialize('json', data)

    return JsonResponse({'data': data})

