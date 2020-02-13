# Generated by Django 2.1.11 on 2020-02-13 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidate', '0016_bitbyteactivity'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitbyteactivity',
            name='candidate',
            field=models.ForeignKey(default=None, limit_choices_to={'groups__name': 'candidate'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bitbyteactivity',
            name='confirm_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bitbyteactivity',
            name='notes',
            field=models.TextField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='offchallenge',
            name='officer',
            field=models.ForeignKey(default=None, limit_choices_to={'groups__name': 'officer'}, on_delete=django.db.models.deletion.CASCADE, related_name='given_challenges', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='offchallenge',
            name='requester',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='received_challenges', to=settings.AUTH_USER_MODEL),
        ),
    ]
