# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_businessuser_user'),
        ('business', '0002_auto_20151004_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='business',
            field=models.ForeignKey(default=1, to='users.BusinessUser'),
            preserve_default=False,
        ),
    ]
