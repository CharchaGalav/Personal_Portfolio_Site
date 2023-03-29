# Generated by Django 4.0.6 on 2023-03-01 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_codingprofiles_alter_certificate_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codingprofiles',
            name='icon',
            field=models.FileField(blank=True, upload_to='CodingProfile'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.FileField(blank=True, upload_to='skills'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(blank=True, upload_to='avatars'),
        ),
    ]
