from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Material, LibraryBook, SalfedjioVideo, YouTubeRecommendation, TeamMember
from django.db.models import Q


def home_view(request):
    books = LibraryBook.objects.all()
    videos = YouTubeRecommendation.objects.all()
    team_members = TeamMember.objects.all()
    return render(request, 'main/home.html', {
        'books': books,
        'videos': videos,
        'team_members': team_members,
    })


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


def search_view(request):
    query = request.GET.get('q')
    materials = SalfedjioVideo.objects.none()
    videos = Material.objects.none()

    if query:
        materials = Material.objects.filter(Q(text__icontains=query) | Q(assignment_text__icontains=query))
        videos = SalfedjioVideo.objects.filter(Q(title__icontains=query) | Q(youtube_url__icontains=query))

    return render(request, 'main/search_results.html', {
        'query': query,
        'materials': materials,
        'videos': videos
    })
