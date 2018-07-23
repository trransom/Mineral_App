# Generated by Django 2.0.7 on 2018-07-19 16:28
from __future__ import unicode_literals
from django.db import migrations, models

import json




class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('img_filename', models.CharField(max_length=300)),
                ('img_caption', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=300)),
                ('formula', models.CharField(max_length=300)),
                ('strunz_class', models.CharField(max_length=300)),
                ('color', models.CharField(max_length=300)),
                ('crystal_sys', models.CharField(max_length=300)),
                ('unit_cell', models.CharField(max_length=300)),
                ('crystal_sym', models.CharField(max_length=300)),
                ('cleavage', models.CharField(max_length=300)),
                ('mohs', models.CharField(max_length=300)),
                ('luster', models.CharField(max_length=300)),
                ('streak', models.CharField(max_length=300)),
                ('diaphaneity', models.CharField(max_length=300)),
                ('optical_prop', models.CharField(max_length=300)),
                ('refractive_inx', models.CharField(default='', max_length=300)),
                ('crystal_habit', models.CharField(default='', max_length=300)),
                ('spec_gravity', models.CharField(default='', max_length=300)),
            ],
        ),
    ]