# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
