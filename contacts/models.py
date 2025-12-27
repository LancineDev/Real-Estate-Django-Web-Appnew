from django.db import models
from datetime import datetime

class Contact(models.Model):
  listing = models.CharField(max_length=200, verbose_name='Propriété')
  listing_id = models.IntegerField(verbose_name="ID de l’annonce")
  name = models.CharField(max_length=200, verbose_name='Nom')
  email = models.CharField(max_length=100, verbose_name='Email')
  phone = models.CharField(max_length=100, verbose_name='Téléphone')
  message = models.TextField(blank=True, verbose_name='Message')
  contact_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Date de contact')
  user_id = models.IntegerField(blank=True, verbose_name='Utilisateur')
  def __str__(self):
    return self.name
  class Meta:
    verbose_name = 'Contact'
    verbose_name_plural = 'Contacts'
