# Generated by Django 3.2.22 on 2023-10-27 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('offer', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='user_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='request',
            name='user_id',
            field=models.IntegerField(blank=True, default='0'),
        ),
    ]