# Generated by Django 3.0.3 on 2020-12-31 03:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examine', '0002_auto_20201230_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='body_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='guide',
            name='body_sw',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='guide',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='guide',
            name='title_sw',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
