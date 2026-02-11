from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm

def index(request):
    categories = Category.objects.all()
    return render(request, 'categories/index.html', {'categories': categories})


def show(request, id):
    category = Category.objects.get(id=id)
    return render(request, 'categories/show.html', {'category': category})


def create(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            return redirect(category.show_url)

    return render(request, 'categories/create.html', {'form': form})



def delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('categories.index')


def edit(request, id):
    category = Category.objects.get(id=id)

    form = CategoryForm(instance=category)

    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect(category.show_url)

    return render(request, 'categories/edit.html', {'form': form})


def show(request, id):
    category = Category.objects.get(id=id)
    products = category.product_set.all()
    return render(request, 'categories/show.html', {
        'category': category,
        'products': products
    })


