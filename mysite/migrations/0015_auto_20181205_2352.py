# Generated by Django 2.1.3 on 2018-12-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_auto_20181205_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='biletix_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]