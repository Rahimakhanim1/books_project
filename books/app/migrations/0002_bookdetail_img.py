# Generated by Django 5.1.6 on 2025-02-23 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdetail',
            name='img',
            field=models.ImageField(null=True, upload_to='book_covers/'),
        ),
    ]
