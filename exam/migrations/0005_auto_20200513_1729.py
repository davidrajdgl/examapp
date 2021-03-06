# Generated by Django 3.0.6 on 2020-05-13 17:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_examtaker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examtaker',
            name='completed_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='examtaker',
            name='started_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
