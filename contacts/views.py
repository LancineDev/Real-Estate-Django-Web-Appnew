from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Contact

def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']
    sender_email = email
    admin_email = getattr(settings, 'ADMIN_EMAIL', settings.DEFAULT_FROM_EMAIL)

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('/listings/'+listing_id)

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    # Send email to property realtor (with admin fallback)
    subject = 'Property Listing Inquiry'
    body = (
      'There has been an inquiry for ' + listing + '\n' +
      'Details:\n' +
      'Name: ' + name + '\n' +
      'Email: ' + sender_email + '\n' +
      'Phone: ' + phone + '\n' +
      'Message: ' + message + '\n' +
      'Listing ID: ' + listing_id
    )

    # Choose recipient: realtor if available, else admin
    recipients = []
    if realtor_email and '@' in realtor_email:
      recipients = [realtor_email]
      used_admin_fallback_initial = False
    else:
      recipients = [admin_email]
      used_admin_fallback_initial = True

    email_message = EmailMessage(
      subject,
      body,
      settings.DEFAULT_FROM_EMAIL,
      recipients,
      reply_to=[sender_email]
    )

    try:
      email_message.send(fail_silently=False)
      if used_admin_fallback_initial:
        messages.success(request, 'Your inquiry was sent to the site admin (realtor email unavailable).')
      else:
        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    except Exception as e:
      # If sending to realtor failed, try admin fallback once
      if not used_admin_fallback_initial:
        try:
          EmailMessage(
            subject,
            body + '\n\n[FALLBACK] Original send failed, delivered to admin.',
            settings.DEFAULT_FROM_EMAIL,
            [admin_email],
            reply_to=[sender_email]
          ).send(fail_silently=False)
          messages.success(request, 'Your inquiry was sent to the site admin (realtor email delivery failed).')
        except Exception as e2:
          messages.error(request, 'Could not send email to realtor or admin: ' + str(e2))
      else:
        messages.error(request, 'Could not send email to admin: ' + str(e))

    return redirect('/listings/'+listing_id)
