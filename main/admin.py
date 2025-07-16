from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (
    Category, Material, LibraryBook,
    SalfedjioVideo, YouTubeRecommendation,
    TeamMember, MaterialProgress
)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['id', 'name']


@admin.register(Material)
class MaterialAdmin(TranslationAdmin):
    list_display = ['id', 'category']


@admin.register(LibraryBook)
class LibraryBookAdmin(TranslationAdmin):
    list_display = ['id', 'title']


@admin.register(SalfedjioVideo)
class SalfedjioVideoAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'youtube_url']


@admin.register(YouTubeRecommendation)
class YouTubeRecommendationAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'youtube_url']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title')
    fields = ('full_name', 'job_title', 'bio', 'photo')
    search_fields = ('full_name', 'job_title')


@admin.register(MaterialProgress)
class MaterialProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'material', 'is_completed', 'completed_at')
    list_filter = ('is_completed', 'completed_at')
    search_fields = ('user__username', 'user__email', 'material__text')
    ordering = ('-completed_at',)
