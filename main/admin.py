from django.contrib import admin
from .models import Category, Material, LibraryBook, SalfedjioVideo, YouTubeRecommendation, TeamMember, MaterialProgress


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']


@admin.register(LibraryBook)
class LibraryBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(SalfedjioVideo)
class SalfedjioVideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'youtube_url']


@admin.register(YouTubeRecommendation)
class YouTubeRecommendationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'youtube_url']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'job_title']


@admin.register(MaterialProgress)
class MaterialProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'material', 'is_completed', 'completed_at')
    list_filter = ('is_completed', 'completed_at')
    search_fields = ('user__username', 'user__email', 'material__title')
    ordering = ('-completed_at',)
