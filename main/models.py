from django.db import models
from urllib.parse import urlparse, parse_qs


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Material(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(default="Hozircha matn mavjud emas.")
    audio = models.FileField(upload_to='main/material/audios/', blank=True, null=True)
    assignment_text = models.TextField(blank=True, null=True)
    assignment_audio = models.FileField(upload_to='main/material/audio/', blank=True, null=True)
    assignment_image = models.ImageField(upload_to='main/material/images/', blank=True, null=True)

    def __str__(self):
        return f"Material for {self.category.name}" if self.category else "Material (kategoriya yo‘q)"


class LibraryBook(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='library/')

    def __str__(self):
        return self.title


class SalfedjioVideo(models.Model):
    title = models.CharField(max_length=100)
    youtube_url = models.URLField()

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
    title = models.CharField(max_length=100)
    youtube_url = models.URLField()

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
