# Generated by Django 3.2.22 on 2023-11-13 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('offer', '0012_alter_request_user_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='user_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
