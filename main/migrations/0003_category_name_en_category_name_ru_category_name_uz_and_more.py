from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_materialprogress_options_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Category Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Category Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Category Name'),
        ),
        migrations.AddField(
            model_name='librarybook',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='librarybook',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='librarybook',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='librarybook',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='librarybook',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='librarybook',
            name='title_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='material',
            name='assignment_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Assignment Text'),
        ),
        migrations.AddField(
            model_name='material',
            name='assignment_text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Assignment Text'),
        ),
        migrations.AddField(
            model_name='material',
            name='assignment_text_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Assignment Text'),
        ),
        migrations.AddField(
            model_name='material',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='material',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='material',
            name='text_uz',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='salfedjiovideo',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Video Title'),
        ),
        migrations.AddField(
            model_name='salfedjiovideo',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Video Title'),
        ),
        migrations.AddField(
            model_name='salfedjiovideo',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Video Title'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='full_name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Full Name'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='full_name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Full Name'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='full_name_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='Full Name'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='job_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Job Title'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='job_title_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Job Title'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='job_title_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Job Title'),
        ),
        migrations.AddField(
            model_name='youtuberecommendation',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Recommendation Title'),
        ),
        migrations.AddField(
            model_name='youtuberecommendation',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Recommendation Title'),
        ),
        migrations.AddField(
            model_name='youtuberecommendation',
            name='title_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Recommendation Title'),
        ),
    ]
