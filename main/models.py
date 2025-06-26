from django.db import models
from urllib.parse import urlparse, parse_qs
from django.utils.translation import gettext_lazy as _
from dualedu import settings


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=100)

    def __str__(self):
        return self.name


class Material(models.Model):
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE)
    text = models.TextField(_("Text"))
    audio = models.FileField(_("Audio File"), upload_to='main/material/audios/', blank=True, null=True)

    assignment_text = models.TextField(_("Assignment Text"), blank=True, null=True)
    assignment_audio = models.FileField(_("Assignment Audio"), upload_to='main/material/audio/', blank=True, null=True)
    assignment_image = models.ImageField(_("Assignment Image"), upload_to='main/material/images/', blank=True,
                                         null=True)

    def __str__(self):
        return f"{_('Material for')} {self.category.name}"


class MaterialProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE)
    material = models.ForeignKey(Material, verbose_name=_("Material"), on_delete=models.CASCADE)
    is_completed = models.BooleanField(_("Completed"), default=False)
    completed_at = models.DateTimeField(_("Completed At"), auto_now_add=True)

    class Meta:
        unique_together = ('user', 'material')
        verbose_name = _("Material Progress")
        verbose_name_plural = _("Material Progresses")


class LibraryBook(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(_("Description"))
    pdf_file = models.FileField(_("PDF File"), upload_to='library/')

    def __str__(self):
        return self.title


class SalfedjioVideo(models.Model):
    title = models.CharField(_("Video Title"), max_length=100)
    youtube_url = models.URLField(_("YouTube URL"))

    def __str__(self):
        return self.title

    def get_video_id(self):
        url = self.youtube_url.strip()
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname

        if hostname in ['youtu.be']:
            return parsed_url.path.lstrip('/')

        if hostname in ['www.youtube.com', 'youtube.com']:
            if parsed_url.path == '/watch':
                query = parse_qs(parsed_url.query)
                return query.get('v', [None])[0]
            elif parsed_url.path.startswith('/embed/'):
                return parsed_url.path.split('/embed/')[1]
            elif parsed_url.path.startswith('/shorts/'):
                return parsed_url.path.split('/shorts/')[1]

        return None


class YouTubeRecommendation(models.Model):
    title = models.CharField(_("Recommendation Title"), max_length=100)
    youtube_url = models.URLField(_("YouTube URL"))

    def __str__(self):
        return self.title

    def video_id(self):
        parsed_url = urlparse(self.youtube_url)
        if parsed_url.hostname == 'youtu.be':
            return parsed_url.path[1:]
        elif parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
            query = parse_qs(parsed_url.query)
            return query.get('v', [None])[0]
        return None


class TeamMember(models.Model):
    full_name = models.CharField(_("Full Name"), max_length=200)
    job_title = models.CharField(_("Job Title"), max_length=200, blank=True, null=True)
    photo = models.ImageField(_("Photo"), upload_to='users/', blank=True, null=True)

    def __str__(self):
        return self.full_name
