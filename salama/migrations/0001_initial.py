# Generated by Django 5.0.6 on 2024-06-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OrderForm",
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
                ("item", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=100)),
                ("quantity", models.IntegerField()),
                ("route", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "salama_order",
            },
        ),
        migrations.CreateModel(
            name="salama_register",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("email_address", models.EmailField(max_length=30)),
                ("phone_number", models.IntegerField()),
            ],
            options={
                "db_table": "salama_customers",
            },
        ),
    ]
