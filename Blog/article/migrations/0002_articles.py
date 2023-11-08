# Generated by Django 3.1.2 on 2023-11-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorname', models.CharField(max_length=150)),
                ('nachname', models.CharField(max_length=150)),
                ('date_of_Birth', models.CharField(max_length=150)),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('slug', models.CharField(max_length=150)),
            ],
        ),
    ]
