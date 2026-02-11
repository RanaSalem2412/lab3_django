from django.urls import path
from . import views





urlpatterns = [
    path('', views.index, name='categories.index'),
    path('show/<int:id>/', views.show, name='categories.show'),
    path('create/', views.create, name='categories.create'),
    path('edit/<int:id>/', views.edit, name='categories.edit'),
    path('delete/<int:id>/', views.delete, name='categories.delete'),
]
