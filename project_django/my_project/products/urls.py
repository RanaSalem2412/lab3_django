from django.urls import path
from .views import index, show, create, delete ,edit

urlpatterns = [
    path('', index, name='products.index'),
    path('show/<int:id>', show, name='products.show'),
    path('create/', create, name='products.create'),
    path('delete/<int:id>', delete, name='products.delete'),
    path('edit/<int:id>/', edit, name='products.edit'),
    

]


