# Generated by Django 3.2.22 on 2023-10-09 10:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100, verbose_name="Enter customer's contact number")),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Completed', 'Completed')], default='Pending', max_length=25)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='offer.post')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
