# Generated by Django 3.2 on 2023-06-29 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='image',
            new_name='imagen',
        ),
    ]