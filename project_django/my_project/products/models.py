from django.db import models

from categories.models import Category





# Create your models here.



from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    

    def __str__(self):
        return f"{self.name} ({self.id})"

    
    @property
    def show_url(self):
        return reverse("products.show", args=[self.id])

    
    @property
    def delete_url(self):
        return reverse("products.delete", args=[self.id])
    
    @property
    def image_url(self):
        return f"/media/{self.image}"

    
    @classmethod
    def get_all(cls):
        return cls.objects.all().order_by('id')

    
    @classmethod
    def delete_object_by_id(cls, id):
        obj = cls.objects.filter(id=id).first()
        if obj:
            obj.delete()
            return True
        return False



    
    





    