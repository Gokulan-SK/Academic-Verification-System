# Generated by Django 5.0.1 on 2024-02-13 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='degree_certificate_hash',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='student',
            name='transcript_hash',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]