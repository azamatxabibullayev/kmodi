from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (
    Category, Material, LibraryBook,
    SalfedjioVideo, YouTubeRecommendation,
    TeamMember
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
class TeamMemberAdmin(TranslationAdmin):
    list_display = ('full_name', 'job_title')
    fields = (
        'full_name_uz', 'full_name_ru', 'full_name_en',
        'job_title_uz', 'job_title_ru', 'job_title_en',
        'bio_uz', 'bio_ru', 'bio_en',
        'photo'
    )
    search_fields = (
        'full_name_uz', 'full_name_ru', 'full_name_en',
        'job_title_uz', 'job_title_ru', 'job_title_en'
    )
