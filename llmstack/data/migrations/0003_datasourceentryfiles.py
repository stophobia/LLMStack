# Generated by Django 4.2.11 on 2024-03-26 17:57

import uuid

from django.db import migrations, models

import llmstack.data.models


class Migration(migrations.Migration):

    dependencies = [
        ("datasources", "0002_datasource_config_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DataSourceEntryFiles",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False, help_text="UUID of the asset")),
                ("metadata", models.JSONField(blank=True, default=dict, help_text="Metadata for the asset", null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("ref_id", models.UUIDField(blank=True, help_text="UUID of the datasource entry this file belongs to")),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        null=True,
                        storage=llmstack.data.models.DataSourceEntryFiles.select_storage,
                        upload_to=llmstack.data.models.DataSourceEntryFiles.datasource_upload_to,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
