# Generated by Django 2.1.3 on 2018-11-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0014_remove_alumnus_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnus',
            name='job_title',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
