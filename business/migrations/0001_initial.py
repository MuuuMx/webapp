# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('unity', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('longitude', models.IntegerField(default=0)),
                ('latitude', models.IntegerField(default=0)),
                ('business_user', models.ForeignKey(to='users.BusinessUser')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('product', models.ForeignKey(to='business.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(to='business.Product')),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='product',
            field=models.ForeignKey(to='business.Product'),
        ),
    ]
