# Generated by Django 2.2.1 on 2019-06-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0004_auto_20190611_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
