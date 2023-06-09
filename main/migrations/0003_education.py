# Generated by Django 4.0.6 on 2023-03-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=200)),
                ('link', models.URLField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
