# Generated by Django 5.1.2 on 2024-10-13 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_about_me', models.ImageField(blank=True, null=True, upload_to='about_me_photo/')),
            ],
        ),
        migrations.DeleteModel(
            name='AboutMe',
        ),
    ]