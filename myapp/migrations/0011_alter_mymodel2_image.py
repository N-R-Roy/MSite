# Generated by Django 4.1.5 on 2023-01-12 16:21

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0010_mymodel2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mymodel2",
            name="image",
            field=models.FileField(
                storage=django.core.files.storage.FileSystemStorage(
                    location="/my_photo/"
                ),
                upload_to=django.core.files.storage.FileSystemStorage(
                    location="/my_photo/"
                ),
            ),
        ),
    ]
