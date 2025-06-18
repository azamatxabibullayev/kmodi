from django.db import models


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
