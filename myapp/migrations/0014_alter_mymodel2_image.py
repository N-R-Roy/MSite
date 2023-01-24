# Generated by Django 4.1.5 on 2023-01-13 12:13

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0013_alter_mymodel2_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mymodel2",
            name="image",
            field=models.FileField(
                storage=django.core.files.storage.FileSystemStorage(
                    location="media/my_photo/"
                ),
                upload_to="",
            ),
        ),
    ]
