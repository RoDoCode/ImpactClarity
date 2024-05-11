from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Series, CoachingToken


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_key, item_data in bag.items():

        item_type, item_id = item_key.split('_')
        item_id = int(item_id)

        if item_type == 'product':
            item = get_object_or_404(Product, pk=item_id)
        elif item_type == 'series':
            item = get_object_or_404(Series, pk=item_id)
        elif item_type == 'coachingtoken':
            item = get_object_or_404(CoachingToken, pk=item_id)
        else:
            continue

        if isinstance(item_data, int):
            total += item_data * item.price
            product_count += item_data
            bag_items.append({
                'item_id': item_key,
                'quantity': item_data,
                'product': item,
            })
        else:
            continue

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
