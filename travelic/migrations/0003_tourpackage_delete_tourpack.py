# Generated by Django 5.0.6 on 2024-05-18 13:21

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelic', '0002_tourpack_delete_tourpackage'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('des', tinymce.models.HTMLField()),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='TourPack',
        ),
    ]
