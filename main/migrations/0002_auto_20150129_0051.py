# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_image',
            field=models.ImageField(null=True, upload_to=b'imgs/answers', blank=True),
            preserve_default=True,
        ),
    ]
