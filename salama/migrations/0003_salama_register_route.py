# Generated by Django 5.0.6 on 2024-06-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("salama", "0002_orderform_user_alter_orderform_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="salama_register",
            name="route",
            field=models.CharField(default=9999, max_length=60),
            preserve_default=False,
        ),
    ]
