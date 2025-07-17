from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_teammember_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='bio_en',
            field=models.TextField(blank=True, null=True, verbose_name='Bio / About'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='bio_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Bio / About'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='bio_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Bio / About'),
        ),
    ]
