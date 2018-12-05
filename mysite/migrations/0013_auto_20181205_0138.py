# Generated by Django 2.1.3 on 2018-12-04 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_auto_20181205_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventowner',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='eventowner',
            name='last_name',
        ),
        migrations.AddField(
            model_name='eventowner',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.Profile'),
        ),
    ]