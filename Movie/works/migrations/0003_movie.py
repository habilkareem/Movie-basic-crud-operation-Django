# Generated by Django 4.2.6 on 2024-01-03 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_genre_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('duration', models.PositiveIntegerField()),
                ('summary', models.TextField(max_length=300)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.genre')),
            ],
        ),
    ]