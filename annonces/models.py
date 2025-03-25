from django.db import models
from django.urls import reverse

# Create your models here.
class Annonce(models.Model):
    title       = models.CharField(max_length=120)
    description = models.CharField(max_length=300)
    content     = models.CharField(max_length=100000)

    def get_absolute_url(self):
        return reverse('annonces:annonce-detail', kwargs={"id": self.id})
    