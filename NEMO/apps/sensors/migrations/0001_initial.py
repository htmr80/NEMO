# Generated by Django 3.2.12 on 2022-04-18 14:37

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import NEMO.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("NEMO", "0038_version_4_0_0"),
    ]

    def add_modbus_tcp_sensor_category(apps, schema_editor):
        SensorCardCategory = apps.get_model("sensors", "SensorCardCategory")
        SensorCardCategory.objects.create(name="ModbusTcp", key="modbus_tcp")

    operations = [
        migrations.CreateModel(
            name="Sensor",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                (
                    "data_prefix",
                    models.CharField(blank=True, max_length=100, null=True, help_text="Prefix for sensor data values"),
                ),
                (
                    "data_suffix",
                    models.CharField(blank=True, max_length=100, null=True, help_text="Suffix for sensor data values"),
                ),
                ("unit_id", models.PositiveIntegerField(blank=True, null=True)),
                ("read_address", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "number_of_values",
                    models.PositiveIntegerField(
                        blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                (
                    "formula",
                    models.TextField(
                        blank=True,
                        help_text="Enter a formula to compute for this sensor values. The list of registers read is available as variable <b>registers</b>. Specific functions can be used based on the sensor type. See documentation for details.",
                        null=True,
                    ),
                ),
                (
                    "read_frequency",
                    models.PositiveIntegerField(
                        default=5,
                        help_text="Enter the read frequency in minutes. Every 2 hours = 120, etc. Max value is 1440 min (24hrs). Use 0 to disable sensor data read.",
                        validators=[
                            django.core.validators.MaxValueValidator(1440),
                            django.core.validators.MinValueValidator(0),
                        ],
                    ),
                ),
                (
                    "visible",
                    models.BooleanField(
                        default=True, help_text="Specifies whether this sensor is visible in the sensor dashboard"
                    ),
                ),
                (
                    "data_label",
                    models.CharField(blank=True, help_text="Label for graph and table data", max_length=200, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SensorCardCategory",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(help_text="The name for this sensor card category", max_length=200)),
                (
                    "key",
                    models.CharField(
                        help_text="The key to identify this sensor card category by in sensors.py", max_length=100
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Sensor card categories",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="SensorCategory",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(help_text="The name for this sensor category", max_length=200)),
            ],
            options={
                "verbose_name_plural": "Sensor categories",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="SensorData",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("value", models.FloatField()),
                ("sensor", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="sensors.sensor")),
            ],
            options={
                "verbose_name_plural": "Sensor data",
                "ordering": ["-created_date"],
            },
        ),
        migrations.CreateModel(
            name="SensorCard",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200)),
                ("server", models.CharField(max_length=200)),
                ("port", models.PositiveIntegerField()),
                ("username", models.CharField(blank=True, max_length=100, null=True)),
                ("password", models.CharField(blank=True, max_length=100, null=True)),
                ("enabled", models.BooleanField(default=True)),
                (
                    "category",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="sensors.sensorcardcategory"),
                ),
            ],
            options={
                "ordering": ["server"],
            },
        ),
        migrations.AddField(
            model_name="sensor",
            name="sensor_category",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="sensors.sensorcategory"
            ),
        ),
        migrations.AddField(
            model_name="sensor",
            name="interlock_card",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="NEMO.interlockcard"
            ),
        ),
        migrations.AddField(
            model_name="sensor",
            name="sensor_card",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="sensors.sensorcard"
            ),
        ),
        migrations.AddField(
            model_name="sensorcategory",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="children",
                to="sensors.sensorcategory",
            ),
        ),
        migrations.CreateModel(
            name="SensorAlertLog",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("time", models.DateTimeField(auto_now_add=True)),
                ("value", models.FloatField(blank=True, null=True)),
                ("reset", models.BooleanField(default=False)),
                ("condition", models.TextField(blank=True, null=True)),
                ("no_data", models.BooleanField(default=False)),
                ("sensor", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="sensors.sensor")),
            ],
            options={
                "ordering": ["-time"],
            },
        ),
        migrations.CreateModel(
            name="SensorAlertEmail",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("enabled", models.BooleanField(default=True)),
                (
                    "trigger_no_data",
                    models.BooleanField(
                        default=False, help_text="Check this box to trigger this alert when no data is available"
                    ),
                ),
                (
                    "trigger_condition",
                    models.TextField(
                        blank=True,
                        help_text="The trigger condition for this alert. The sensor value is available as a variable named <b>value</b>. e.g. value == 42 or value > 42.",
                        null=True,
                    ),
                ),
                ("triggered_on", models.DateTimeField(blank=True, null=True)),
                (
                    "additional_emails",
                    NEMO.fields.MultiEmailField(
                        blank=True,
                        help_text="Additional email address to contact when this alert is triggered. A comma-separated list can be used.",
                        max_length=2000,
                        null=True,
                    ),
                ),
                ("sensor", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="sensors.sensor")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RunPython(add_modbus_tcp_sensor_category),
    ]
