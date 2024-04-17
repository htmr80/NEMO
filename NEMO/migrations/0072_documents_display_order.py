# Generated by Django 3.2.25 on 2024-04-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NEMO", "0071_wait_list"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="projectdocuments",
            options={"ordering": ["display_order", "-uploaded_at"], "verbose_name_plural": "Project documents"},
        ),
        migrations.AlterModelOptions(
            name="safetyitemdocuments",
            options={"ordering": ["display_order", "-uploaded_at"], "verbose_name_plural": "Safety item documents"},
        ),
        migrations.AlterModelOptions(
            name="staffknowledgebaseitemdocuments",
            options={
                "ordering": ["display_order", "-uploaded_at"],
                "verbose_name_plural": "Staff knowledge base item documents",
            },
        ),
        migrations.AlterModelOptions(
            name="tooldocuments",
            options={"ordering": ["display_order", "-uploaded_at"], "verbose_name_plural": "Tool documents"},
        ),
        migrations.AlterModelOptions(
            name="userdocuments",
            options={"ordering": ["display_order", "-uploaded_at"], "verbose_name_plural": "User documents"},
        ),
        migrations.AlterModelOptions(
            name="userknowledgebaseitemdocuments",
            options={
                "ordering": ["display_order", "-uploaded_at"],
                "verbose_name_plural": "User knowledge base item documents",
            },
        ),
        migrations.AddField(
            model_name="projectdocuments",
            name="display_order",
            field=models.IntegerField(
                default=1,
                help_text="The order in which choices are displayed on the landing page, from left to right, top to bottom. Lower values are displayed first.",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="safetyitemdocuments",
            name="display_order",
            field=models.IntegerField(
                default=1,
                help_text="The order in which choices are displayed on the landing page, from left to right, top to bottom. Lower values are displayed first.",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="staffknowledgebaseitemdocuments",
            name="display_order",
            field=models.IntegerField(
                default=1,
                help_text="The order in which choices are displayed on the landing page, from left to right, top to bottom. Lower values are displayed first.",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tooldocuments",
            name="display_order",
            field=models.IntegerField(
                default=1,
                help_text="The order in which choices are displayed on the landing page, from left to right, top to bottom. Lower values are displayed first.",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userdocuments",
            name="display_order",
            field=models.IntegerField(
                default=1,
                help_text="The order in which choices are displayed on the landing page, from left to right, top to bottom. Lower values are displayed first.",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userknowledgebaseitemdocuments",
            name="display_order",
            field=models.IntegerField(
                default=1,
                help_text="The order in which choices are displayed on the landing page, from left to right, top to bottom. Lower values are displayed first.",
            ),
            preserve_default=False,
        ),
    ]
