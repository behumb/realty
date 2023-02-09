# Generated by Django 4.1.6 on 2023-02-09 10:33

import catalog.services
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to=catalog.services.real_estate_dir_path, verbose_name='Image')),
                ('cost', models.FloatField(verbose_name='Cost')),
                ('year_build', models.IntegerField(verbose_name='Year build')),
                ('parking_space_count', models.IntegerField(verbose_name='Parking space count')),
                ('parking_detail', models.CharField(max_length=50, verbose_name='Parking detail')),
                ('deal_type', models.CharField(choices=[('B', 'Buy'), ('R', 'Rent')], max_length=1, verbose_name='Deal type')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='Value')),
                ('real_estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='catalog.realestate')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150, verbose_name='Address')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
                ('real_estate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='catalog.realestate')),
            ],
        ),
    ]
