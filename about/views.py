from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import About, Resource
from .forms import ResourceForm


def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )


def resources(request):
    """
    Renders the resources page with dynamic content
    """
    resources = Resource.objects.all().order_by('title')

    if request.method == "POST" and request.user.is_superuser:
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resources')
    else:
        form = ResourceForm()
    
    return render(
        request,
        "about/resources.html",
        {"resources": resources, "form": form}
    )
