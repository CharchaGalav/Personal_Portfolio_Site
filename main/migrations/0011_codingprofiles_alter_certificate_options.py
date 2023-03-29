# Generated by Django 4.0.6 on 2023-03-01 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_certificate_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodingProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.URLField(blank=True)),
                ('icon', models.ImageField(blank=True, upload_to='CodingProfile')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='certificate',
            options={'ordering': ['date']},
        ),
    ]
