# Generated by Django 4.1.5 on 2023-01-17 14:46

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0016_author_book_authors"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.FileField(
                storage=django.core.files.storage.FileSystemStorage(location="media/"),
                upload_to="",
            ),
        ),
    ]
