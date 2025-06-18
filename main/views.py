from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Material, LibraryBook, SalfedjioVideo


def home_view(request):
    books = LibraryBook.objects.all()
    return render(request, 'main/home.html', {'books': books})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'main/category_list.html', {'categories': categories})


def category_materials(request, category_id):
    category = Category.objects.get(id=category_id)
    materials = Material.objects.filter(category=category)
    return render(request, 'main/material_detail.html', {
        'category': category,
        'materials': materials
    })


def library_view(request):
    books = LibraryBook.objects.all()
    return render(request, 'main/library.html', {'books': books})


def salfedjio_view(request):
    videos = SalfedjioVideo.objects.all()
    return render(request, 'main/salfedjio.html', {'videos': videos})
