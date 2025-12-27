from django.db import models
from datetime import datetime

class Realtor(models.Model):
  name = models.CharField(max_length=200, verbose_name='Nom')
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo')
  description = models.TextField(blank=True, verbose_name='Description')
  phone = models.CharField(max_length=20, verbose_name='Téléphone')
  email = models.CharField(max_length=50, verbose_name='Email')
  is_mvp = models.BooleanField(default=False, verbose_name='Agent du mois')
  hire_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name="Date d'embauche")
  def __str__(self):
    return self.name
  class Meta:
    verbose_name = 'Agent immobilier'
    verbose_name_plural = 'Agents immobiliers'
