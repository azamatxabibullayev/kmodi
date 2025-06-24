from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from dashboard.decorators import admin_required
from django import forms
from django.contrib.auth import get_user_model

from main.models import (
    Category, Material, MaterialProgress,
    LibraryBook, SalfedjioVideo,
    YouTubeRecommendation, TeamMember
)

User = get_user_model()


@login_required
@admin_required
def dashboard_home(request):
    return render(request, 'dashboard/home.html')


# ==== FORMS ====
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['category', 'text', 'audio', 'assignment_text', 'assignment_audio', 'assignment_image']


class MaterialProgressForm(forms.ModelForm):
    class Meta:
        model = MaterialProgress
        fields = ['user', 'material', 'is_completed']


class LibraryBookForm(forms.ModelForm):
    class Meta:
        model = LibraryBook
        fields = ['title', 'description', 'pdf_file']


class SalfedjioVideoForm(forms.ModelForm):
    class Meta:
        model = SalfedjioVideo
        fields = ['title', 'youtube_url']


class YouTubeRecommendationForm(forms.ModelForm):
    class Meta:
        model = YouTubeRecommendation
        fields = ['title', 'youtube_url']


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['full_name', 'job_title', 'photo']


class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'phone', 'email', 'is_active']


# ==== GENERIC CRUD ====
def list_view(request, model, template_name, context_name):
    objects = model.objects.all()
    return render(request, template_name, {context_name: objects})


def create_view(request, form_class, redirect_url, title):
    form = form_class(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(redirect_url)
    return render(request, 'dashboard/form.html', {'form': form, 'title': title})


def update_view(request, pk, model, form_class, redirect_url, title):
    obj = get_object_or_404(model, pk=pk)
    form = form_class(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(redirect_url)
    return render(request, 'dashboard/form.html', {'form': form, 'title': title})


def delete_view(request, pk, model, redirect_url, title):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect(redirect_url)
    return render(request, 'dashboard/confirm_delete.html', {'object': obj, 'title': title})


# ==== CATEGORY CRUD ====
@login_required
@admin_required
def category_list(request):
    return list_view(request, Category, 'dashboard/category_list.html', 'categories')


@login_required
@admin_required
def category_create(request):
    return create_view(request, CategoryForm, 'dashboard:category_list', 'Kategoriya qo\'shish')


@login_required
@admin_required
def category_edit(request, pk):
    return update_view(request, pk, Category, CategoryForm, 'dashboard:category_list', 'Kategoriya tahrirlash')


@login_required
@admin_required
def category_delete(request, pk):
    return delete_view(request, pk, Category, 'dashboard:category_list', 'Kategoriya o\'chirish')


# ==== MATERIAL CRUD ====
@login_required
@admin_required
def material_list(request):
    return list_view(request, Material, 'dashboard/material_list.html', 'materials')


@login_required
@admin_required
def material_create(request):
    return create_view(request, MaterialForm, 'dashboard:material_list', 'Material qo\'shish')


@login_required
@admin_required
def material_edit(request, pk):
    return update_view(request, pk, Material, MaterialForm, 'dashboard:material_list', 'Material tahrirlash')


@login_required
@admin_required
def material_delete(request, pk):
    return delete_view(request, pk, Material, 'dashboard:material_list', 'Material o\'chirish')


# ==== MATERIAL PROGRESS CRUD ====
@login_required
@admin_required
def progress_list(request):
    return list_view(request, MaterialProgress, 'dashboard/progress_list.html', 'progresses')


@login_required
@admin_required
def progress_create(request):
    return create_view(request, MaterialProgressForm, 'dashboard:progress_list', 'Material Progress qo\'shish')


@login_required
@admin_required
def progress_edit(request, pk):
    return update_view(request, pk, MaterialProgress, MaterialProgressForm, 'dashboard:progress_list',
                       'Material Progress tahrirlash')


@login_required
@admin_required
def progress_delete(request, pk):
    return delete_view(request, pk, MaterialProgress, 'dashboard:progress_list', 'Material Progress o\'chirish')


# ==== LIBRARY BOOK CRUD ====
@login_required
@admin_required
def book_list(request):
    return list_view(request, LibraryBook, 'dashboard/book_list.html', 'books')


@login_required
@admin_required
def book_create(request):
    return create_view(request, LibraryBookForm, 'dashboard:book_list', 'Kitob qo\'shish')


@login_required
@admin_required
def book_edit(request, pk):
    return update_view(request, pk, LibraryBook, LibraryBookForm, 'dashboard:book_list', 'Kitob tahrirlash')


@login_required
@admin_required
def book_delete(request, pk):
    return delete_view(request, pk, LibraryBook, 'dashboard:book_list', 'Kitob o\'chirish')


# ==== SALFEDJIO VIDEO CRUD ====
@login_required
@admin_required
def video_list(request):
    return list_view(request, SalfedjioVideo, 'dashboard/video_list.html', 'videos')


@login_required
@admin_required
def video_create(request):
    return create_view(request, SalfedjioVideoForm, 'dashboard:video_list', 'Video qo\'shish')


@login_required
@admin_required
def video_edit(request, pk):
    return update_view(request, pk, SalfedjioVideo, SalfedjioVideoForm, 'dashboard:video_list', 'Video tahrirlash')


@login_required
@admin_required
def video_delete(request, pk):
    return delete_view(request, pk, SalfedjioVideo, 'dashboard:video_list', 'Video o\'chirish')


# ==== YOUTUBE RECOMMENDATION CRUD ====
@login_required
@admin_required
def recommendation_list(request):
    return list_view(request, YouTubeRecommendation, 'dashboard/recommendation_list.html', 'recommendations')


@login_required
@admin_required
def recommendation_create(request):
    return create_view(request, YouTubeRecommendationForm, 'dashboard:recommendation_list', 'Tavsiya qo\'shish')


@login_required
@admin_required
def recommendation_edit(request, pk):
    return update_view(request, pk, YouTubeRecommendation, YouTubeRecommendationForm, 'dashboard:recommendation_list',
                       'Tavsiya tahrirlash')


@login_required
@admin_required
def recommendation_delete(request, pk):
    return delete_view(request, pk, YouTubeRecommendation, 'dashboard:recommendation_list', 'Tavsiya o\'chirish')


# ==== TEAM MEMBER CRUD ====
@login_required
@admin_required
def team_list(request):
    return list_view(request, TeamMember, 'dashboard/team_list.html', 'team')


@login_required
@admin_required
def team_create(request):
    return create_view(request, TeamMemberForm, 'dashboard:team_list', 'A\'zo qo\'shish')


@login_required
@admin_required
def team_edit(request, pk):
    return update_view(request, pk, TeamMember, TeamMemberForm, 'dashboard:team_list', 'A\'zo tahrirlash')


@login_required
@admin_required
def team_delete(request, pk):
    return delete_view(request, pk, TeamMember, 'dashboard:team_list', 'A\'zo o\'chirish')


# ==== STUDENT USER CRUD ====
@login_required
@admin_required
def student_list(request):
    students = User.objects.filter(role='student')
    return render(request, 'dashboard/student_list.html', {'students': students})


@login_required
@admin_required
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        student = form.save(commit=False)
        student.role = 'student'
        student.set_password('default123')  # You may prompt real password later
        student.save()
        return redirect('dashboard:student_list')
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Talaba qo\'shish'})


@login_required
@admin_required
def student_edit(request, pk):
    student = get_object_or_404(User, pk=pk, role='student')
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('dashboard:student_list')
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Talaba tahrirlash'})


@login_required
@admin_required
def student_delete(request, pk):
    student = get_object_or_404(User, pk=pk, role='student')
    if request.method == 'POST':
        student.delete()
        return redirect('dashboard:student_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': student, 'title': 'Talaba o\'chirish'})
