# Generated by Django 5.1.2 on 2024-10-13 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_aboutmeinfo_firstparagraph_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('publication_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]