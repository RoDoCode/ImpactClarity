from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product, Series
from profiles.models import UserProfile


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag."""

    product = get_object_or_404(Product, pk=item_id)
    series = product.series_no
    series_key = f'series_{series.pk}'
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')

    bag = request.session.get('bag', {})
    product_key = f'product_{item_id}'

    if product_key in bag:
        messages.info(
            request,
            f"Oops, '{product.name}' is already"
            f" in your bag, you only need one."
        )
    elif series_key in bag:
        messages.info(
            request,
            f"Oops, '{product.name}' is already"
            f" in '{series.friendly_name}', no need to add it twice."
        )
    elif request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            series_list = user_profile.series_access.all()
            product_list = user_profile.product_access.all()

            if series in series_list:
                messages.info(
                    request,
                    f"Oops, you already own '{product.name}' "
                    f"in '{series.friendly_name}', check your library."
                )
            elif product in product_list:
                messages.info(
                    request,
                    f"Oops, you already own "
                    f"'{product.name}', check your library."
                )
            else:
                bag[product_key] = quantity
                messages.success(request, f'Added {product.name} to your bag.')
        except UserProfile.DoesNotExist:
            messages.error(request, "Your user profile could not be found.")
            return redirect(redirect_url)
    else:
        bag[product_key] = quantity
        messages.success(request, f'Added {product.name} to your bag.')

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
        messages.success(request, f'Updated {product.name} quantity '
                                  f'to {quantity}')
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

        if item_id in bag:
            item_type, product_id = item_id.split('_')
            product = get_object_or_404(Product, pk=product_id)
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


# ADDING/ADJUSTING/REMOVING SERIES IN BAG

def add_series_to_bag(request, item_id):
    """ Add a quantity of the specified series to the shopping bag """
    series = get_object_or_404(Series, pk=item_id)
    products = Product.objects.filter(series_no=series)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')

    bag = request.session.get('bag', {})
    series_key = f'series_{item_id}'

    if series_key in bag:
        messages.info(
            request,
            f'Oops {series.name} is already in your bag, you only need 1'
        )
    elif request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            series_list = user_profile.series_access.all()
            if series in series_list:
                messages.info(
                    request,
                    f"Oops, you already own "
                    f"'{series.friendly_name}', check your library"
                )
            else:
                pass
        except UserProfile.DoesNotExist:
            messages.error(request, "Your user profile could not be found.")
            return redirect(redirect_url)
    else:
        any_removed = False
        for product in products:
            product_key = f'product_{product.pk}'
            if product_key in bag:
                del bag[product_key]
                any_removed = True
        bag[series_key] = quantity
        if any_removed:
            messages.info(
                request,
                f'Some of the episodes in your bag were already in '
                f'{series.friendly_name}, so we removed them from your '
                f'bag and added the series')
        else:
            messages.success(
                request, 
                f'Added {series.friendly_name} '
                f'to your bag'
            )

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
        messages.success(request, f'Updated {series.friendly_name} '
                                  f'quantity to {quantity}')
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
