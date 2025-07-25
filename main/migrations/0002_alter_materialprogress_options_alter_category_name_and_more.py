import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materialprogress',
            options={'verbose_name': 'Material Progress', 'verbose_name_plural': 'Material Progresses'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='librarybook',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='librarybook',
            name='pdf_file',
            field=models.FileField(upload_to='library/', verbose_name='PDF File'),
        ),
        migrations.AlterField(
            model_name='librarybook',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='material',
            name='assignment_audio',
            field=models.FileField(blank=True, null=True, upload_to='main/material/audio/', verbose_name='Assignment Audio'),
        ),
        migrations.AlterField(
            model_name='material',
            name='assignment_image',
            field=models.ImageField(blank=True, null=True, upload_to='main/material/images/', verbose_name='Assignment Image'),
        ),
        migrations.AlterField(
            model_name='material',
            name='assignment_text',
            field=models.TextField(blank=True, null=True, verbose_name='Assignment Text'),
        ),
        migrations.AlterField(
            model_name='material',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='main/material/audios/', verbose_name='Audio File'),
        ),
        migrations.AlterField(
            model_name='material',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='material',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='materialprogress',
            name='completed_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Completed At'),
        ),
        migrations.AlterField(
            model_name='materialprogress',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='Completed'),
        ),
        migrations.AlterField(
            model_name='materialprogress',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.material', verbose_name='Material'),
        ),
        migrations.AlterField(
            model_name='materialprogress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='salfedjiovideo',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Video Title'),
        ),
        migrations.AlterField(
            model_name='salfedjiovideo',
            name='youtube_url',
            field=models.URLField(verbose_name='YouTube URL'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='job_title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Job Title'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='youtuberecommendation',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Recommendation Title'),
        ),
        migrations.AlterField(
            model_name='youtuberecommendation',
            name='youtube_url',
            field=models.URLField(verbose_name='YouTube URL'),
        ),
    ]
