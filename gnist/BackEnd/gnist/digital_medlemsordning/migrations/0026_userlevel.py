# Generated by Django 5.0.1 on 2024-03-11 19:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "digital_medlemsordning",
            "0025_alter_activity_image_alter_members_certificate_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="UserLevel",
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
                ("levelName", models.CharField(max_length=45)),
                ("points", models.IntegerField()),
            ],
        ),
    ]
