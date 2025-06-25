import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Category, Material, LibraryBook, SalfedjioVideo,
    YouTubeRecommendation, TeamMember, MaterialProgress
)
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.http import JsonResponse


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
    categories = list(Category.objects.all().order_by('id'))
    user = request.user

    completed_material_ids = set(
        MaterialProgress.objects.filter(user=user, is_completed=True).values_list('material_id', flat=True)
    )

    unlocked = True
    for i, category in enumerate(categories):
        materials = list(Material.objects.filter(category=category))

        if i == 0:
            category.unlocked = True
            continue

        prev_category = categories[i - 1]
        prev_materials = Material.objects.filter(category=prev_category)

        if prev_materials.exists():
            prev_material_ids = set(m.id for m in prev_materials)
            all_prev_completed = prev_material_ids.issubset(completed_material_ids)
        else:
            all_prev_completed = True

        category.unlocked = all_prev_completed

    return render(request, 'main/category_list.html', {
        'categories': categories
    })


@login_required
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    categories = list(Category.objects.all().order_by('id'))
    current_index = categories.index(category)

    if current_index > 0:
        prev_category = categories[current_index - 1]
        prev_materials = Material.objects.filter(category=prev_category)
        completed_ids = set(
            MaterialProgress.objects.filter(user=request.user, is_completed=True).values_list('material_id', flat=True))

        if not all(m.id in completed_ids for m in prev_materials):
            return redirect('category_list')

    materials = Material.objects.filter(category=category)
    completed_ids = set(
        MaterialProgress.objects.filter(user=request.user, is_completed=True).values_list('material_id', flat=True))
    for m in materials:
        m.is_completed = m.id in completed_ids

    return render(request, 'main/material_detail.html', {'category': category, 'materials': materials})


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
    query = request.GET.get('q')
    materials = Material.objects.none()
    videos = SalfedjioVideo.objects.none()
    material_categories = {}
    completed_material_ids = []

    if query:
        materials = Material.objects.filter(
            category__name__icontains=query
        )

        videos = SalfedjioVideo.objects.filter(
            title__icontains=query
        )

        completed_material_ids = list(MaterialProgress.objects.filter(
            user=request.user, is_completed=True
        ).values_list('material_id', flat=True))

        from collections import defaultdict
        material_categories = defaultdict(list)
        for m in Material.objects.all():
            material_categories[str(m.category.id)].append(m.id)

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
