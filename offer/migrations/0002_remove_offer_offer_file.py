# Generated by Django 4.1.7 on 2023-02-19 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='offer_file',
        ),
    ]