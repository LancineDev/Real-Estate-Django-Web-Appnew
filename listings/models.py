from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, verbose_name='Agent immobilier')
  title = models.CharField(max_length=200, verbose_name='Titre')
  address = models.CharField(max_length=200, verbose_name='Adresse')
  city = models.CharField(max_length=100, verbose_name='Ville')
  state = models.CharField(max_length=100, verbose_name='Région')
  zipcode = models.CharField(max_length=20, verbose_name='Code postal')
  description = models.TextField(blank=True, verbose_name='Description')
  price = models.IntegerField(verbose_name='Prix')
  bedrooms = models.IntegerField(verbose_name='Chambres')
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Salles de bain')
  garage = models.IntegerField(default=0, verbose_name='Garage')
  sqft = models.IntegerField(verbose_name='Superficie (pieds carrés)')
  lot_size = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Taille du lot (acres)')
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo principale')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo 1')
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo 2')
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo 3')
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo 4')
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo 5')
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo 6')
  is_published = models.BooleanField(default=True, verbose_name='Publié')
  list_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name="Date d'inscription")
  def __str__(self):
    return self.title
  class Meta:
    verbose_name = 'Annonce'
    verbose_name_plural = 'Annonces'
