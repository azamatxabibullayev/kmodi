from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_category_name_en_category_name_ru_category_name_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='Bio / About'),
        ),
    ]
