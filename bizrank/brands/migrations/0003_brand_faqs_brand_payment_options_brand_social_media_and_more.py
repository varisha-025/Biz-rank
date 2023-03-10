# Generated by Django 4.1.7 on 2023-03-01 19:34

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
        ("brands", "0002_brandownership"),
    ]

    operations = [
        migrations.AddField(
            model_name="brand",
            name="FAQs",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="brand",
            name="payment_options",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=64),
                blank=True,
                null=True,
                size=None,
            ),
        ),
        migrations.AddField(
            model_name="brand",
            name="social_media",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="brandownership",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.user",
            ),
        ),
        migrations.AlterField(
            model_name="brand",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="brand",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="brand",
            name="website",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="brandownership",
            name="brand",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="brands.brand",
            ),
        ),
    ]