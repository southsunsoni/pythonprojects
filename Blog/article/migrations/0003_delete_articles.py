# Generated by Django 3.1.2 on 2023-11-02 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_articles'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Articles',
        ),
    ]
