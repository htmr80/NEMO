# Generated by Django 3.2.14 on 2022-09-06 16:26

from django.db import migrations, models

import NEMO.utilities


class Migration(migrations.Migration):
    dependencies = [
        ("NEMO", "0040_version_4_2_0"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chemical",
            name="document",
            field=models.FileField(
                blank=True, max_length=500, null=True, upload_to=NEMO.utilities.get_chemical_document_filename
            ),
        ),
    ]
