# Generated by Django 5.0 on 2024-01-22 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToyShopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='toy_images/', verbose_name="toy's image"),
        ),
    ]
