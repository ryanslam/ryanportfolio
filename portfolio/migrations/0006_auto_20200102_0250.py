# Generated by Django 3.0.1 on 2020-01-02 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20200102_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='github_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='linkedin_url',
            field=models.URLField(blank=True, default=''),
        ),
    ]
