# Generated by Django 4.2.7 on 2023-11-12 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_task_workspace'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='workspace',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.workspace'),
        ),
    ]