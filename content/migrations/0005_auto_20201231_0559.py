# Generated by Django 3.0.3 on 2020-12-31 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20201231_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_sw',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
