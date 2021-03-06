# Generated by Django 4.0.2 on 2022-03-22 13:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('responsible_person', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('deadline', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.CharField(max_length=100)),
                ('project_name', models.CharField(default=False, max_length=50)),
            ],
        ),
    ]
