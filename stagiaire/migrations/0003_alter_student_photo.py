# Generated by Django 4.1.7 on 2023-03-07 14:39

from django.db import migrations, models
import stagiaire.models


class Migration(migrations.Migration):

    dependencies = [
        ('stagiaire', '0002_alter_filiaire_filiaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=stagiaire.models.renomer_image),
        ),
    ]
