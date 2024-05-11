from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Series, UserProfile, Product
from django.http import HttpResponseForbidden
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def library(request):
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return render(request, 'profiles/library.html', {'error': 'UserProfile not found.'})
        series_list = user_profile.series_access.all()
        product_list = user_profile.product_access.all()
        context = {
            'series_list': series_list,
            'product_list': product_list
        }
        return render(request, 'profiles/library.html', context)
    else:
        return render(request, 'profiles/library.html')


@login_required
def series_library(request, series_no):
    series = get_object_or_404(Series, series_no=series_no)
    user_profile = UserProfile.objects.get(user=request.user)
    if series not in user_profile.series_access.all():
        return HttpResponseForbidden("You do not have access to this series.")
    products = Product.objects.filter(series_no=series)
    return render(
        request,
        'profiles/series_library.html',
        {'series': series, 'products': products}
    )


@login_required
def product_viewer(request, product_id):
    """ A view to show individual product video """

    product = get_object_or_404(Product, pk=product_id)
    if product not in user_profile.product_access.all():
        return HttpResponseForbidden("You do not have access to this tutorial.")
    context = {
        'product': product,
    }
    return render(request, 'profiles/product_viewer.html', context)
