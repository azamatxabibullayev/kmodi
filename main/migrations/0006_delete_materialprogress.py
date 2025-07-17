from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_teammember_bio_en_teammember_bio_ru_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MaterialProgress',
        ),
    ]
