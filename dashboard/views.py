from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from dashboard.decorators import admin_required
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as _t

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
        labels = {
            'name': _("Category Name"),
        }


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['category', 'text', 'audio', 'assignment_text', 'assignment_audio', 'assignment_image']
        labels = {
            'category': _("Category"),
            'text': _("Text"),
            'audio': _("Audio"),
            'assignment_text': _("Assignment Text"),
            'assignment_audio': _("Assignment Audio"),
            'assignment_image': _("Assignment Image"),
        }


class MaterialProgressForm(forms.ModelForm):
    class Meta:
        model = MaterialProgress
        fields = ['user', 'material', 'is_completed']
        labels = {
            'user': _("User"),
            'material': _("Material"),
            'is_completed': _("Is Completed"),
        }


class LibraryBookForm(forms.ModelForm):
    class Meta:
        model = LibraryBook
        fields = ['title', 'description', 'pdf_file']
        labels = {
            'title': _("Title"),
            'description': _("Description"),
            'pdf_file': _("PDF File"),
        }


class SalfedjioVideoForm(forms.ModelForm):
    class Meta:
        model = SalfedjioVideo
        fields = ['title', 'youtube_url']
        labels = {
            'title': _("Title"),
            'youtube_url': _("YouTube URL"),
        }


class YouTubeRecommendationForm(forms.ModelForm):
    class Meta:
        model = YouTubeRecommendation
        fields = ['title', 'youtube_url']
        labels = {
            'title': _("Title"),
            'youtube_url': _("YouTube URL"),
        }


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['full_name', 'job_title', 'photo']
        labels = {
            'full_name': _("Full Name"),
            'job_title': _("Job Title"),
            'photo': _("Photo"),
        }


class StudentForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput,
        required=True
    )
    password2 = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput,
        required=True
    )

    class Meta:
        model = User
        fields = ['full_name', 'phone', 'email', 'is_active']
        labels = {
            'full_name': _("Full Name"),
            'phone': _("Phone"),
            'email': _("Email"),
            'is_active': _("Is Active"),
        }

    def clean(self):
        cleaned_data = super().clean()
        pw1 = cleaned_data.get("password1")
        pw2 = cleaned_data.get("password2")

        if pw1 and pw2 and pw1 != pw2:
            raise forms.ValidationError(_("Passwords do not match"))

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password1"]
        user.set_password(password)
        if commit:
            user.save()
        return user


# ==== GENERIC CRUD ====
def list_view(request, model, template_name, context_name):
    objects = model.objects.all()
    return render(request, template_name, {context_name: objects})


def create_view(request, form_class, redirect_url, title):
    form = form_class(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(redirect_url)
    return render(request, 'dashboard/form.html', {'form': form, 'title': _t(title)})


def update_view(request, pk, model, form_class, redirect_url, title):
    obj = get_object_or_404(model, pk=pk)
    form = form_class(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(redirect_url)
    return render(request, 'dashboard/form.html', {'form': form, 'title': _t(title)})


def delete_view(request, pk, model, redirect_url, title):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect(redirect_url)
    return render(request, 'dashboard/confirm_delete.html', {'object': obj, 'title': _t(title)})


# ==== CATEGORY CRUD ====
@login_required
@admin_required
def category_list(request):
    return list_view(request, Category, 'dashboard/category_list.html', 'categories')


@login_required
@admin_required
def category_create(request):
    return create_view(request, CategoryForm, 'dashboard:category_list', _("Add Category"))


@login_required
@admin_required
def category_edit(request, pk):
    return update_view(request, pk, Category, CategoryForm, 'dashboard:category_list', _("Edit Category"))


@login_required
@admin_required
def category_delete(request, pk):
    return delete_view(request, pk, Category, 'dashboard:category_list', _("Delete Category"))


# ==== MATERIAL CRUD ====
@login_required
@admin_required
def material_list(request):
    return list_view(request, Material, 'dashboard/material_list.html', 'materials')


@login_required
@admin_required
def material_create(request):
    return create_view(request, MaterialForm, 'dashboard:material_list', _("Add Material"))


@login_required
@admin_required
def material_edit(request, pk):
    return update_view(request, pk, Material, MaterialForm, 'dashboard:material_list', _("Edit Material"))


@login_required
@admin_required
def material_delete(request, pk):
    return delete_view(request, pk, Material, 'dashboard:material_list', _("Delete Material"))


# ==== MATERIAL PROGRESS CRUD ====
@login_required
@admin_required
def progress_list(request):
    return list_view(request, MaterialProgress, 'dashboard/progress_list.html', 'progresses')


@login_required
@admin_required
def progress_create(request):
    return create_view(request, MaterialProgressForm, 'dashboard:progress_list', _("Add Material Progress"))


@login_required
@admin_required
def progress_edit(request, pk):
    return update_view(request, pk, MaterialProgress, MaterialProgressForm, 'dashboard:progress_list',
                       _("Edit Material Progress"))


@login_required
@admin_required
def progress_delete(request, pk):
    return delete_view(request, pk, MaterialProgress, 'dashboard:progress_list', _("Delete Material Progress"))


# ==== LIBRARY BOOK CRUD ====
@login_required
@admin_required
def book_list(request):
    return list_view(request, LibraryBook, 'dashboard/book_list.html', 'books')


@login_required
@admin_required
def book_create(request):
    return create_view(request, LibraryBookForm, 'dashboard:book_list', _("Add Book"))


@login_required
@admin_required
def book_edit(request, pk):
    return update_view(request, pk, LibraryBook, LibraryBookForm, 'dashboard:book_list', _("Edit Book"))


@login_required
@admin_required
def book_delete(request, pk):
    return delete_view(request, pk, LibraryBook, 'dashboard:book_list', _("Delete Book"))


# ==== SALFEDJIO VIDEO CRUD ====
@login_required
@admin_required
def video_list(request):
    return list_view(request, SalfedjioVideo, 'dashboard/video_list.html', 'videos')


@login_required
@admin_required
def video_create(request):
    return create_view(request, SalfedjioVideoForm, 'dashboard:video_list', _("Add Video"))


@login_required
@admin_required
def video_edit(request, pk):
    return update_view(request, pk, SalfedjioVideo, SalfedjioVideoForm, 'dashboard:video_list', _("Edit Video"))


@login_required
@admin_required
def video_delete(request, pk):
    return delete_view(request, pk, SalfedjioVideo, 'dashboard:video_list', _("Delete Video"))


# ==== YOUTUBE RECOMMENDATION CRUD ====
@login_required
@admin_required
def recommendation_list(request):
    return list_view(request, YouTubeRecommendation, 'dashboard/recommendation_list.html', 'recommendations')


@login_required
@admin_required
def recommendation_create(request):
    return create_view(request, YouTubeRecommendationForm, 'dashboard:recommendation_list', _("Add Recommendation"))


@login_required
@admin_required
def recommendation_edit(request, pk):
    return update_view(request, pk, YouTubeRecommendation, YouTubeRecommendationForm, 'dashboard:recommendation_list',
                       _("Edit Recommendation"))


@login_required
@admin_required
def recommendation_delete(request, pk):
    return delete_view(request, pk, YouTubeRecommendation, 'dashboard:recommendation_list', _("Delete Recommendation"))


# ==== TEAM MEMBER CRUD ====
@login_required
@admin_required
def team_list(request):
    return list_view(request, TeamMember, 'dashboard/team_list.html', 'team')


@login_required
@admin_required
def team_create(request):
    return create_view(request, TeamMemberForm, 'dashboard:team_list', _("Add Team Member"))


@login_required
@admin_required
def team_edit(request, pk):
    return update_view(request, pk, TeamMember, TeamMemberForm, 'dashboard:team_list', _("Edit Team Member"))


@login_required
@admin_required
def team_delete(request, pk):
    return delete_view(request, pk, TeamMember, 'dashboard:team_list', _("Delete Team Member"))


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
        student.set_password('default123')
        student.save()
        return redirect('dashboard:student_list')
    return render(request, 'dashboard/form.html', {'form': form, 'title': _("Add Student")})


@login_required
@admin_required
def student_edit(request, pk):
    student = get_object_or_404(User, pk=pk, role='student')
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('dashboard:student_list')
    return render(request, 'dashboard/form.html', {'form': form, 'title': _("Edit Student")})


@login_required
@admin_required
def student_delete(request, pk):
    student = get_object_or_404(User, pk=pk, role='student')
    if request.method == 'POST':
        student.delete()
        return redirect('dashboard:student_list')
    return render(request, 'dashboard/confirm_delete.html', {'object': student, 'title': _("Delete Student")})
