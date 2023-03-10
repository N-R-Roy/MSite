# Generated by Django 4.1.5 on 2023-01-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0019_alter_employee_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("price", models.DecimalField(decimal_places=5, max_digits=8)),
            ],
        ),
    ]
