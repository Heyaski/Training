# Generated by Django 5.1.2 on 2024-10-13 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_aboutmeinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmeinfo',
            name='firstParagraph',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutmeinfo',
            name='secondParagraph',
            field=models.TextField(blank=True, null=True),
        ),
    ]