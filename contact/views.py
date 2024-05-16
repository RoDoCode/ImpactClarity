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
            messages.add_message(
                request,
                messages.SUCCESS,
                "Collaboration request received! "
                "I endeavour to respond within "
                "2 working days."
            )

            customer_message = (
                f"Dear {contact_request.name},\n\n"
                f"Thank you for reaching out. We have received your message "
                f"and will respond within 2 working days.\n\n"
                f"Message: {contact_request.message}\n\n"
                f"Best regards,\nYour Company Name"
            )

            admin_message = (
                f"Name: {contact_request.name}\n"
                f"Email: {contact_request.email}\n"
                f"Message: {contact_request.message}"
            )

            send_mail(
                subject='Thank you for contacting us',
                message=customer_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact_request.email],
                fail_silently=False,
            )

            send_mail(
                subject=f"New contact request from {contact_request.name}",
                message=admin_message,
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
