# Generated by Django 4.2.6 on 2024-01-03 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.TextField(max_length=300, null=True),
        ),
    ]