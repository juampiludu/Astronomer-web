# Generated by Django 3.0.6 on 2020-06-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astronomerweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lunareclipse',
            name='short_eclipse_info',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='solareclipse',
            name='short_eclipse_info',
            field=models.TextField(default=''),
        ),
    ]
