from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product, Series, CoachingToken


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    product_key = f'product_{item_id}'
    print("Current Bag Contents:", bag)

    if product_key in bag:
        messages.info(request,
                            (f"Oops, '{product.name}' "
                            f"is already in your bag, you only need one"))
    else:
        bag[product_key] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    try:
        product_id = int(item_id.split('_')[1])
    except (IndexError, ValueError):
        messages.error(request, 'Invalid product identifier')
        return redirect('view_bag')
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    product_key = f'product_{product_id}'
    if quantity > 0:
        bag[product_key] = quantity
        messages.success(request, f'Updated {product.name} quantity to {quantity}')
    else:
        if product_key in bag:
            bag.pop(product_key)
            messages.success(request, f'Removed {product.name} from your bag')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        bag = request.session.get('bag', {})
        
        # Check if item_id directly exists in the bag (assuming item_id includes prefix)
        if item_id in bag:
            item_type, product_id = item_id.split('_')
            product = get_object_or_404(Product, pk=product_id)  # Ensure this ID refers to a Product
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')
            request.session['bag'] = bag
            return HttpResponse(status=200)
        else:
            messages.error(request, 'Item not found in bag')
            return HttpResponse(status=404)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

"""
def remove_from_bag(request, item_id):
    Remove the item from the shopping bag

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
"""

# ADDING/ADJUSTING/REMOVING SERIES IN BAG

def add_series_to_bag(request, item_id):
    """ Add a quantity of the specified series to the shopping bag """
    series = get_object_or_404(Series, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    series_key = f'series_{item_id}'
    if series_key in bag:
        messages.info(request,
                            (f'Oops {series.name} '
                            f'is already in your bag, you only need 1'))
    else:
        bag[series_key] = quantity
        messages.success(request, f'Added {series.friendly_name} to your bag')
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_series_in_bag(request, item_id):
    """Adjust the quantity of the specified series to the specified amount"""
    try:
        series_id = int(item_id.split('_')[1])
    except (IndexError, ValueError):
        messages.error(request, 'Invalid series identifier')
        return redirect('view_bag')
    series = get_object_or_404(Series, pk=series_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    series_key = f'series_{series_id}'
    if quantity > 0:
        bag[series_key] = quantity
        messages.success(request, f'Updated {series.friendly_name} quantity to {quantity}')
    else:
        if series_key in bag:
            bag.pop(series_key)
            messages.success(request, f'Removed {series.name} from your bag')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
    


def remove_series_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        series = get_object_or_404(Series, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {series.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


# ADDING/ADJUSTING/REMOVING CoachingToken IN BAG

def add_token_to_bag(request, item_id):
    """ Add a quantity of the specified coachingtoken to the shopping bag """

    coachingtoken = get_object_or_404(CoachingToken, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request,
                            (f'Updated {coachingtoken.name} '
                            f'quantity to {bag[item_id]}'))
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {coachingtoken.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_token_in_bag(request, item_id):
    """Adjust the quantity of the specified series to the specified amount"""
    try:
        token_id = int(item_id.split('_')[1])
    except (IndexError, ValueError):
        messages.error(request, 'Invalid token identifier')
        return redirect('view_bag')
    token = get_object_or_404(CoachingToken, pk=token_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    token_key = f'token_{token_id}'
    if quantity > 0:
        bag[token_key] = quantity
        messages.success(request, f'Updated {token.name} quantity to {quantity}')
    else:
        if token_key in bag:
            bag.pop(token_key)
            messages.success(request, f'Removed {token.name} from your bag')
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_token_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        coachingtoken = get_object_or_404(CoachingToken, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {coachingtoken.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)