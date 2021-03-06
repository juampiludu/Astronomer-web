# Generated by Django 3.0.6 on 2020-06-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astronomerweb', '0003_auto_20200602_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolarEclipse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_type', models.CharField(max_length=30)),
                ('eclipse_info', models.TextField()),
                ('short_eclipse_info', models.TextField(default='')),
                ('eclipse_image_route', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=40)),
            ],
        ),
        migrations.RenameModel(
            old_name='Eclipse',
            new_name='LunarEclipse',
        ),
    ]
