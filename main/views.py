import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.db.models import Q
from .models import (
    Category, Material, LibraryBook, SalfedjioVideo,
    YouTubeRecommendation, TeamMember, MaterialProgress
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
    completed_ids = set(
        MaterialProgress.objects.filter(user=request.user, is_completed=True).values_list('material_id', flat=True)
    )
    for m in materials:
        m.is_completed = m.id in completed_ids

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


@login_required
def search_view(request):
    query = request.GET.get('q', '')
    materials = Material.objects.none()
    videos = SalfedjioVideo.objects.none()
    material_categories = {}
    completed_material_ids = []

    if query:
        materials = Material.objects.filter(category__name__icontains=query)
        videos = SalfedjioVideo.objects.filter(title__icontains=query)

        completed_material_ids = list(MaterialProgress.objects.filter(
            user=request.user, is_completed=True
        ).values_list('material_id', flat=True))

        from collections import defaultdict
        material_categories = defaultdict(list)
        for material in materials:
            material_categories[str(material.category.id)].append(material.id)

    return render(request, 'main/search_results.html', {
        'query': query,
        'materials': materials,
        'videos': videos,
        'completed_material_ids': json.dumps(completed_material_ids, cls=DjangoJSONEncoder),
        'material_categories': json.dumps(material_categories, cls=DjangoJSONEncoder),
    })


@require_POST
@login_required
def mark_material_completed(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    MaterialProgress.objects.get_or_create(user=request.user, material=material, defaults={'is_completed': True})
    return JsonResponse({'status': 'ok'})
