# Generated by Django 4.2.17 on 2024-12-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "Task_Management_System",
            "0004_remove_comment_created_at_remove_comment_updated_at_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="end_date",
            field=models.DateField(),
        ),
    ]
