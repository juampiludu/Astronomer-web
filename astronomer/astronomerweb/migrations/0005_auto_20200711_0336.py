# Generated by Django 3.0.7 on 2020-07-11 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astronomerweb', '0004_auto_20200602_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eclipses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eclipse_title', models.CharField(max_length=30)),
                ('solar_lunar', models.CharField(max_length=30)),
                ('eclipse_type', models.CharField(max_length=30)),
                ('eclipse_info', models.TextField()),
                ('eclipse_date', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='LunarEclipse',
        ),
        migrations.DeleteModel(
            name='SolarEclipse',
        ),
    ]
