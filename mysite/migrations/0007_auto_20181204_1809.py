# Generated by Django 2.1.3 on 2018-12-04 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_event_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.Profile'),
        ),
    ]
