# Generated by Django 4.2.7 on 2023-11-14 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main_app.task'),
        ),
    ]