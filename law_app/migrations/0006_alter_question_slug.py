# Generated by Django 4.0.6 on 2022-11-27 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law_app', '0005_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]