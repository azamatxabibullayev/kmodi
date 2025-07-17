from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import (
    Category, Material, LibraryBook, SalfedjioVideo,
    YouTubeRecommendation, TeamMember
)


@login_required
def home_view(request):
    books = LibraryBook.objects.all()
    videos = YouTubeRecommendation.objects.all()
    team_members = TeamMember.objects.all()
    return render(request, 'main/home.html', {
        'books': books,
        'videos': videos,
        'team_members': team_members,
    })


@login_required
def category_list(request):
    categories = Category.objects.all().order_by('id')
    return render(request, 'main/category_list.html', {
        'categories': categories
    })


@login_required
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    materials = Material.objects.filter(category=category)
    return render(request, 'main/material_detail.html', {
        'category': category,
        'materials': materials
    })


@login_required
def library_view(request):
    books = LibraryBook.objects.all()
    return render(request, 'main/library.html', {'books': books})


@login_required
def salfedjio_view(request):
    videos = SalfedjioVideo.objects.all()
    return render(request, 'main/salfedjio.html', {'videos': videos})


def search_view(request):
    query = request.GET.get("q", "")
    language = request.LANGUAGE_CODE

    def translated(field):
        return f"{field}_{language}"

    categories = Category.objects.filter(
        Q(**{translated("name") + "__icontains": query})
    )

    materials = Material.objects.filter(
        Q(**{translated("text") + "__icontains": query}) |
        Q(**{translated("assignment_text") + "__icontains": query})
    )

    books = LibraryBook.objects.filter(
        Q(**{translated("title") + "__icontains": query})
    )

    videos = SalfedjioVideo.objects.all()
    filtered_videos = []
    for i, video in enumerate(videos, 1):
        if query.lower() in f"video {i}".lower():
            filtered_videos.append(video)

    team_members = TeamMember.objects.filter(
        Q(**{translated("full_name") + "__icontains": query}) |
        Q(**{translated("job_title") + "__icontains": query}) |
        Q(**{translated("bio") + "__icontains": query})
    )

    context = {
        "query": query,
        "categories": categories,
        "materials": materials,
        "books": books,
        "videos": filtered_videos,
        "team_members": team_members,
    }
    return render(request, "main/search_results.html", context)
