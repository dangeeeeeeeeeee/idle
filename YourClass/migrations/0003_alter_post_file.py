# Generated by Django 4.1.6 on 2023-02-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("YourClass", "0002_alter_post_file_alter_post_viewcount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="file",
            field=models.FileField(null=True, upload_to="%Y/%m%/d"),
        ),
    ]
