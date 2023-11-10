# Generated by Django 3.2.22 on 2023-11-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0007_remove_post_author_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='request',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Please enter your contact number'),
        ),
    ]
