# Generated by Django 3.2.22 on 2023-10-23 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_request_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
