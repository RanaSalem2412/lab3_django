from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


#products = [
 #   {'id': 1, 'name': 'Laptop', 'image': 'products/images/p1.jpeg', 'price': 1000, 'stock': 5},
  #  {'id': 2, 'name': 'Phone', 'image': 'products/images/p3.jpeg', 'price': 500, 'stock': 10},
   # {'id': 3, 'name': 'Headphones', 'image': 'products/images/p2.jpeg', 'price': 100, 'stock': 15},
#]


#def index(request):
 #   return render(request, 'products/index.html', context={'products': products})


#def details(request, id):
 #   filter_product = list(filter(lambda p: p['id'] == id, products))
  #  if filter_product:
   #     product = filter_product[0]
    #    return render(request, 'products/details.html', context={'product': product})
    #else:
    #    return HttpResponse("====Product not found===")






def index(request):
    products = Product.get_all()
    return render(request, 'products/index.html', context={'products': products})


def show(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/details.html', context={'product': product})


from django.shortcuts import render, redirect
from .models import Product


from .forms import ProductForm

def create(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect(product.show_url)
    return render(request, 'products/create.html', {'form': form})




def delete(request, id):
    Product.delete_object_by_id(id)
    return redirect('products.index')






def edit(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(product.show_url)
    return render(request, 'products/edit.html', {'form': form})
