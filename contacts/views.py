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
        messages.error(request, 'Vous avez déjà fait une demande pour cette annonce')
        return redirect('/listings/'+listing_id)

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    # Send email to property realtor (with admin fallback)
    subject = 'Demande de renseignement immobilier'
    body = (
      'Il y a eu une demande pour ' + listing + '\n' +
      'Détails :\n' +
      'Nom : ' + name + '\n' +
      'Email : ' + sender_email + '\n' +
      'Téléphone : ' + phone + '\n' +
      'Message : ' + message + '\n' +
      'ID de l\'annonce : ' + listing_id
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
        messages.success(request, 'Votre demande a été envoyée à l\'administrateur du site (email de l\'agent indisponible).')
      else:
        messages.success(request, 'Votre demande a été soumise, un agent vous contactera bientôt')
    except Exception as e:
      # If sending to realtor failed, try admin fallback once
      if not used_admin_fallback_initial:
        try:
          EmailMessage(
            subject,
            body + '\n\n[FALLBACK] Échec de l\'envoi original, livré à l\'admin.',
            settings.DEFAULT_FROM_EMAIL,
            [admin_email],
            reply_to=[sender_email]
          ).send(fail_silently=False)
          messages.success(request, 'Votre demande a été envoyée à l\'administrateur du site (échec de l\'envoi à l\'agent).')
        except Exception as e2:
          messages.error(request, 'Impossible d\'envoyer un email à l\'agent ou à l\'administrateur : ' + str(e2))
      else:
        messages.error(request, 'Impossible d\'envoyer un email à l\'administrateur : ' + str(e))

    return redirect('/listings/'+listing_id)