# Generated by Django 4.1.5 on 2023-01-17 14:49

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0017_alter_user_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.FileField(
                storage=django.core.files.storage.FileSystemStorage(location="media/"),
                upload_to="users_pic/",
            ),
        ),
    ]
