# Generated by Django 2.2.27 on 2022-03-17 13:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import NEMO.utilities


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# NEMO.migrations.0010_version_1_20_0


class Migration(migrations.Migration):
    replaces = [
        ("NEMO", "0002_version_1_1_0"),
        ("NEMO", "0003_version_1_2_0"),
        ("NEMO", "0004_version_1_3_0"),
        ("NEMO", "0005_version_1_4_0"),
        ("NEMO", "0006_version_1_8_0"),
        ("NEMO", "0007_version_1_15_0"),
        ("NEMO", "0008_version_1_16_0"),
        ("NEMO", "0009_version_1_19_0"),
        ("NEMO", "0010_version_1_20_0"),
        ("NEMO", "0011_version_1_22_0"),
    ]

    dependencies = [
        ("NEMO", "0001_version_1_0_0"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    def add_and_set_default_interlock_category(apps, schema_editor):
        InterlockCardCategory = apps.get_model("NEMO", "InterlockCardCategory")
        InterlockCard = apps.get_model("NEMO", "InterlockCard")
        stanford_category = InterlockCardCategory.objects.create(name="Stanford", key="stanford")
        InterlockCardCategory.objects.create(name="WebRelayHttp", key="web_relay_http")
        for interlock_card in InterlockCard.objects.all():
            interlock_card.category = stanford_category
            interlock_card.save()

    operations = [
        migrations.AddField(
            model_name="landingpagechoice",
            name="hide_from_users",
            field=models.BooleanField(
                default=False,
                help_text="Hides this choice from normal users. When checked, only staff, technicians, and super-users can see the choice",
            ),
        ),
        migrations.CreateModel(
            name="ScheduledOutageCategory",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name_plural": "Scheduled outage categories",
                "ordering": ["name"],
            },
        ),
        migrations.AlterModelOptions(
            name="resourcecategory",
            options={"ordering": ["name"], "verbose_name_plural": "resource categories"},
        ),
        migrations.RemoveField(
            model_name="task",
            name="first_responder",
        ),
        migrations.RemoveField(
            model_name="task",
            name="first_response_time",
        ),
        migrations.RemoveField(
            model_name="task",
            name="status",
        ),
        migrations.AddField(
            model_name="consumable",
            name="visible",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="task",
            name="cancelled",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="task",
            name="resolved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="tool",
            name="post_usage_questions",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="usageevent",
            name="run_data",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="resource",
            name="restriction_message",
            field=models.TextField(
                blank=True,
                help_text="The message that is displayed to users on the tool control page when this resource is unavailable.",
            ),
        ),
        migrations.CreateModel(
            name="ScheduledOutage",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("start", models.DateTimeField()),
                ("end", models.DateTimeField()),
                (
                    "title",
                    models.CharField(
                        help_text="A brief description to quickly inform users about the outage", max_length=100
                    ),
                ),
                (
                    "details",
                    models.TextField(
                        blank=True,
                        help_text="A detailed description of why there is a scheduled outage, and what users can expect during the outage",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
                ("tool", models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="NEMO.Tool")),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        help_text="A categorical reason for why this outage is scheduled. Useful for trend analytics.",
                        max_length=200,
                    ),
                ),
                (
                    "resource",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="NEMO.Resource"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TaskHistory",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(help_text="A text description of the task's status", max_length=200)),
                (
                    "time",
                    models.DateTimeField(
                        auto_now_add=True, help_text="The date and time when the task status was changed"
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        help_text="The task that this historical entry refers to",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="history",
                        to="NEMO.Task",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user that changed the task to this status",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "task histories",
                "ordering": ["time"],
                "get_latest_by": "time",
            },
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("created", models.DateTimeField(help_text="The date and time this story was first published")),
                (
                    "original_content",
                    models.TextField(
                        help_text="The content of the story when it was first published, useful for visually hiding updates 'in the middle' of the story"
                    ),
                ),
                ("all_content", models.TextField(help_text="The entire content of the story")),
                ("last_updated", models.DateTimeField(help_text="The date and time this story was last updated")),
                (
                    "last_update_content",
                    models.TextField(
                        help_text="The most recent update to the story, useful for visually hiding updates 'in the middle' of the story"
                    ),
                ),
                (
                    "archived",
                    models.BooleanField(
                        default=False, help_text="A story is removed from the 'Recent News' page when it is archived"
                    ),
                ),
                (
                    "update_count",
                    models.PositiveIntegerField(
                        help_text="The number of times this story has been updated. When the number of updates is greater than 2, then only the original story and the latest update are displayed in the 'Recent News' page"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "News",
                "ordering": ["-last_updated"],
            },
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("expiration", models.DateTimeField()),
                ("object_id", models.PositiveIntegerField()),
                (
                    "content_type",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="contenttypes.ContentType"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notifications",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="landingpagechoice",
            name="notifications",
            field=models.CharField(
                blank=True,
                choices=[
                    ("news", "News creation and updates - notifies all users"),
                    ("safetyissue", "New safety issues - notifies staff only"),
                ],
                help_text="Displays a the number of new notifications for the user. For example, if the user has two unread news notifications then the number '2' would appear for the news icon on the landing page.",
                max_length=25,
                null=True,
            ),
        ),
        migrations.RemoveField(
            model_name="tool",
            name="secondary_owner",
        ),
        migrations.CreateModel(
            name="TaskStatus",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200, unique=True)),
                (
                    "notify_primary_tool_owner",
                    models.BooleanField(
                        default=False, help_text="Notify the primary tool owner when a task transitions to this status"
                    ),
                ),
                (
                    "notify_tool_notification_email",
                    models.BooleanField(
                        default=False,
                        help_text="Send an email to the tool notification email address when a task transitions to this status",
                    ),
                ),
                (
                    "custom_notification_email_address",
                    models.EmailField(
                        blank=True,
                        help_text="Notify a custom email address when a task transitions to this status. Leave this blank if you don't need it.",
                        max_length=254,
                    ),
                ),
                ("notification_message", models.TextField(blank=True)),
                (
                    "notify_backup_tool_owners",
                    models.BooleanField(
                        default=False, help_text="Notify the backup tool owners when a task transitions to this status"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "task statuses",
                "ordering": ["name"],
            },
        ),
        migrations.AddField(
            model_name="tool",
            name="backup_owners",
            field=models.ManyToManyField(
                blank=True,
                help_text="Alternate staff members who are responsible for administration of this tool when the primary owner is unavailable.",
                related_name="backup_for_tools",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="tool",
            name="grant_badge_reader_access_upon_qualification",
            field=models.CharField(
                blank=True,
                help_text="Badge reader access is granted to the user upon qualification for this tool.",
                max_length=100,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="tool",
            name="policy_off_end_time",
            field=models.TimeField(
                blank=True, help_text="The end time when policy rules should NOT be enforced", null=True
            ),
        ),
        migrations.AddField(
            model_name="tool",
            name="policy_off_start_time",
            field=models.TimeField(
                blank=True, help_text="The start time when policy rules should NOT be enforced", null=True
            ),
        ),
        migrations.CreateModel(
            name="UserPreferences",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "attach_created_reservation",
                    models.BooleanField(
                        default=False,
                        help_text="Whether or not to send a calendar invitation when creating a new reservation",
                        verbose_name="created_reservation_invite",
                    ),
                ),
                (
                    "attach_cancelled_reservation",
                    models.BooleanField(
                        default=False,
                        help_text="Whether or not to send a calendar invitation when cancelling a reservation",
                        verbose_name="cancelled_reservation_invite",
                    ),
                ),
            ],
            options={
                "verbose_name": "User preferences",
                "verbose_name_plural": "User preferences",
            },
        ),
        migrations.AddField(
            model_name="tool",
            name="policy_off_between_times",
            field=models.BooleanField(
                default=False, help_text="Check this box to disable policy rules every day between the given times"
            ),
        ),
        migrations.AddField(
            model_name="tool",
            name="policy_off_weekend",
            field=models.BooleanField(
                default=False, help_text="Whether or not policy rules should be enforced on weekends"
            ),
        ),
        migrations.AlterField(
            model_name="alert",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="hidden_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="hidden_comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="door",
            name="area",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="doors", to="NEMO.Area"),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="cancelled_by",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="resource",
            name="category",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="NEMO.ResourceCategory"
            ),
        ),
        migrations.AlterField(
            model_name="safetyissue",
            name="reporter",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reported_safety_issues",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="safetyissue",
            name="resolver",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="resolved_safety_issues",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="last_updated_by",
            field=models.ForeignKey(
                blank=True,
                help_text="The last user who modified this task. This should always be a staff member.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="problem_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="problem_category",
                to="NEMO.TaskCategory",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="resolution_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="resolution_category",
                to="NEMO.TaskCategory",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="resolver",
            field=models.ForeignKey(
                blank=True,
                help_text="The staff member who resolved the task.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="task_resolver",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="tool",
            name="primary_owner",
            field=models.ForeignKey(
                help_text="The staff member who is responsible for administration of this tool.",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="primary_tool_owner",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="tool",
            name="requires_area_access",
            field=models.ForeignKey(
                blank=True,
                help_text="Indicates that this tool is physically located in a billable area and requires an active area access record in order to be operated.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="NEMO.Area",
            ),
        ),
        migrations.CreateModel(
            name="TaskImages",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.ImageField(upload_to=NEMO.utilities.get_task_image_filename, verbose_name="Image")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                ("task", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="NEMO.Task")),
            ],
            options={
                "verbose_name_plural": "Task images",
                "ordering": ["-uploaded_at"],
            },
        ),
        migrations.CreateModel(
            name="InterlockCardCategory",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(help_text="The name for this interlock category", max_length=200)),
                (
                    "key",
                    models.CharField(
                        help_text="The key to identify this interlock category by in interlocks.py", max_length=100
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Interlock card categories",
                "ordering": ["name"],
            },
        ),
        migrations.AddField(
            model_name="interlockcard",
            name="category",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="NEMO.InterlockCardCategory"
            ),
        ),
        migrations.AddField(
            model_name="interlockcard",
            name="password",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="interlockcard",
            name="username",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="interlockcard",
            name="enabled",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="interlockcard",
            name="even_port",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="interlockcard",
            name="odd_port",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="interlockcard",
            name="number",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="interlock",
            name="channel",
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name="Channel/Relay"),
        ),
        migrations.AddField(
            model_name="tool",
            name="grant_physical_access_level_upon_qualification",
            field=models.ForeignKey(
                blank=True,
                help_text="The designated physical access level is granted to the user upon qualification for this tool.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="NEMO.PhysicalAccessLevel",
            ),
        ),
        migrations.AlterField(
            model_name="door",
            name="interlock",
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to="NEMO.Interlock"),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="descendant",
            field=models.OneToOneField(
                blank=True,
                help_text="Any time a reservation is moved or resized, the old reservation is cancelled and a new reservation with updated information takes its place. This field links the old reservation to the new one, so the history of reservation moves & changes can be easily tracked.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="ancestor",
                to="NEMO.Reservation",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="preferences",
            field=models.OneToOneField(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="NEMO.UserPreferences"
            ),
        ),
        migrations.RunPython(
            code=add_and_set_default_interlock_category,
        ),
        migrations.AddField(
            model_name="tool",
            name="parent_tool",
            field=models.ForeignKey(
                blank=True,
                help_text="Select a parent tool to allow alternate usage",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tool_children_set",
                to="NEMO.Tool",
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="category",
            new_name="_category",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_category",
            field=models.CharField(
                blank=True,
                db_column="category",
                help_text='Create sub-categories using slashes. For example "Category 1/Sub-category 1".',
                max_length=1000,
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="backup_owners",
            new_name="_backup_owners",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_backup_owners",
            field=models.ManyToManyField(
                blank=True,
                db_table="NEMO_tool_backup_owners",
                help_text="Alternate staff members who are responsible for administration of this tool when the primary owner is unavailable.",
                related_name="backup_for_tools",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="allow_delayed_logoff",
            new_name="_allow_delayed_logoff",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_allow_delayed_logoff",
            field=models.BooleanField(
                db_column="allow_delayed_logoff",
                default=False,
                help_text='Upon logging off users may enter a delay before another user may use the tool. Some tools require "spin-down" or cleaning time after use.',
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="grant_badge_reader_access_upon_qualification",
            new_name="_grant_badge_reader_access_upon_qualification",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_grant_badge_reader_access_upon_qualification",
            field=models.CharField(
                blank=True,
                db_column="grant_badge_reader_access_upon_qualification",
                help_text="Badge reader access is granted to the user upon qualification for this tool.",
                max_length=100,
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="grant_physical_access_level_upon_qualification",
            new_name="_grant_physical_access_level_upon_qualification",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_grant_physical_access_level_upon_qualification",
            field=models.ForeignKey(
                blank=True,
                db_column="grant_physical_access_level_upon_qualification_id",
                help_text="The designated physical access level is granted to the user upon qualification for this tool.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="NEMO.PhysicalAccessLevel",
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="interlock",
            new_name="_interlock",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_interlock",
            field=models.OneToOneField(
                blank=True,
                db_column="interlock_id",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="NEMO.Interlock",
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="location",
            new_name="_location",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_location",
            field=models.CharField(blank=True, db_column="location", max_length=100, null=True),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="maximum_future_reservation_time",
            new_name="_maximum_future_reservation_time",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_maximum_future_reservation_time",
            field=models.PositiveIntegerField(
                blank=True,
                db_column="maximum_future_reservation_time",
                help_text="The maximum amount of time (in minutes) that a user may reserve from the current time onwards.",
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="maximum_reservations_per_day",
            new_name="_maximum_reservations_per_day",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_maximum_reservations_per_day",
            field=models.PositiveIntegerField(
                blank=True,
                db_column="maximum_reservations_per_day",
                help_text="The maximum number of reservations a user may make per day for this tool.",
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="maximum_usage_block_time",
            new_name="_maximum_usage_block_time",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_maximum_usage_block_time",
            field=models.PositiveIntegerField(
                blank=True,
                db_column="maximum_usage_block_time",
                help_text="The maximum amount of time (in minutes) that a user may reserve this tool for a single reservation. Leave this field blank to indicate that no maximum usage block time exists for this tool.",
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="minimum_time_between_reservations",
            new_name="_minimum_time_between_reservations",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_minimum_time_between_reservations",
            field=models.PositiveIntegerField(
                blank=True,
                db_column="minimum_time_between_reservations",
                help_text="The minimum amount of time (in minutes) that the same user must have between any two reservations for this tool.",
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="minimum_usage_block_time",
            new_name="_minimum_usage_block_time",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_minimum_usage_block_time",
            field=models.PositiveIntegerField(
                blank=True,
                db_column="minimum_usage_block_time",
                help_text="The minimum amount of time (in minutes) that a user must reserve this tool for a single reservation. Leave this field blank to indicate that no minimum usage block time exists for this tool.",
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="missed_reservation_threshold",
            new_name="_missed_reservation_threshold",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_missed_reservation_threshold",
            field=models.PositiveIntegerField(
                blank=True,
                db_column="missed_reservation_threshold",
                help_text='The amount of time (in minutes) that a tool reservation may go unused before it is automatically marked as "missed" and hidden from the calendar. Usage can be from any user, regardless of who the reservation was originally created for. The cancellation process is triggered by a timed job on the web server.',
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="notification_email_address",
            new_name="_notification_email_address",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_notification_email_address",
            field=models.EmailField(
                blank=True,
                db_column="notification_email_address",
                help_text="Messages that relate to this tool (such as comments, problems, and shutdowns) will be forwarded to this email address. This can be a normal email address or a mailing list address.",
                max_length=254,
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="operational",
            new_name="_operational",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_operational",
            field=models.BooleanField(
                db_column="operational",
                default=False,
                help_text="Marking the tool non-operational will prevent users from using the tool.",
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="phone_number",
            new_name="_phone_number",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_phone_number",
            field=models.CharField(blank=True, db_column="phone_number", max_length=100, null=True),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="policy_off_between_times",
            new_name="_policy_off_between_times",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_policy_off_between_times",
            field=models.BooleanField(
                db_column="policy_off_between_times",
                default=False,
                help_text="Check this box to disable policy rules every day between the given times",
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="policy_off_end_time",
            new_name="_policy_off_end_time",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_policy_off_end_time",
            field=models.TimeField(
                blank=True,
                db_column="policy_off_end_time",
                help_text="The end time when policy rules should NOT be enforced",
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="policy_off_start_time",
            new_name="_policy_off_start_time",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_policy_off_start_time",
            field=models.TimeField(
                blank=True,
                db_column="policy_off_start_time",
                help_text="The start time when policy rules should NOT be enforced",
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="policy_off_weekend",
            new_name="_policy_off_weekend",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_policy_off_weekend",
            field=models.BooleanField(
                db_column="policy_off_weekend",
                default=False,
                help_text="Whether or not policy rules should be enforced on weekends",
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="post_usage_questions",
            new_name="_post_usage_questions",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_post_usage_questions",
            field=models.TextField(blank=True, db_column="post_usage_questions", null=True),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="primary_owner",
            new_name="_primary_owner",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_primary_owner",
            field=models.ForeignKey(
                blank=True,
                db_column="primary_owner_id",
                help_text="The staff member who is responsible for administration of this tool.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="primary_tool_owner",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="requires_area_access",
            new_name="_requires_area_access",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_requires_area_access",
            field=models.ForeignKey(
                blank=True,
                db_column="requires_area_access_id",
                help_text="Indicates that this tool is physically located in a billable area and requires an active area access record in order to be operated.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="NEMO.Area",
            ),
        ),
        migrations.RenameField(
            model_name="tool",
            old_name="reservation_horizon",
            new_name="_reservation_horizon",
        ),
        migrations.AlterField(
            model_name="tool",
            name="_reservation_horizon",
            field=models.PositiveIntegerField(
                blank=True,
                db_column="reservation_horizon",
                default=14,
                help_text="Users may create reservations this many days in advance. Leave this field blank to indicate that no reservation horizon exists for this tool.",
                null=True,
            ),
        ),
    ]
