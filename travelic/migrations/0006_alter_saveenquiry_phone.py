# Generated by Django 5.0.6 on 2024-05-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelic', '0005_saveenquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveenquiry',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
