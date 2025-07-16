from modeltranslation.translator import register, TranslationOptions
from .models import Category, Material, LibraryBook, SalfedjioVideo, YouTubeRecommendation, TeamMember


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Material)
class MaterialTranslationOptions(TranslationOptions):
    fields = ('text', 'assignment_text',)


@register(LibraryBook)
class LibraryBookTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(SalfedjioVideo)
class SalfedjioVideoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(YouTubeRecommendation)
class YouTubeRecommendationTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('full_name', 'job_title', 'bio',)
