# Generated by Django 3.2.3 on 2021-05-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('github_url', models.URLField(blank=True)),
                ('live_url', models.URLField(blank=True)),
            ],
        ),
    ]
