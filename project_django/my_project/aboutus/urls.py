from django.urls import path
from . import views

app_name = 'aboutus'  # مهم جدًا لتستخدم namespacing في {% url %}

urlpatterns = [
    path('', views.about, name='about'),  # اسم URL هنا "about"
]
