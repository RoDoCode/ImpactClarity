from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages
from .models import Contact, ContactRequest
from .forms import ContactForm
from django.conf import settings

def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_request = contact_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")
            
            send_mail(
                subject='Thank you for contacting us',
                message=f"Dear {contact_request.name},\n\nThank you for reaching out. We have received your message and will respond within 2 working days.\n\nMessage: {contact_request.message}\n\nBest regards,\nYour Company Name",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact_request.email],
                fail_silently=False,
            )

            send_mail(
                subject=f"New contact request from {contact_request.name}",
                message=f"Name: {contact_request.name}\nEmail: {contact_request.email}\nMessage: {contact_request.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

    contact = Contact.objects.all().order_by('-updated_on').first()
    contact_form = ContactForm()
    return render(
        request,
        "contact/contact.html",
        {"contact": contact, "contact_form": contact_form},
    )
