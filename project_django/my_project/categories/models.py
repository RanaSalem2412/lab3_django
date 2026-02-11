from django.db import models

# Create your models here.
from django.db import models
from django.shortcuts import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/images', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def show_url(self):
        return reverse('categories.show', args=[self.id])

    @property
    def delete_url(self):
        return reverse('categories.delete', args=[self.id])
    
    @property
    def image_url(self):
        return f"/media/{self.image}"
    
    
