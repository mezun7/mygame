# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=1000)),
                ('score', models.IntegerField(choices=[(10, 10), (20, 20), (30, 30), (40, 40), (50, 50)])),
                ('image', models.ImageField(null=True, upload_to=b'imgs/questions', blank=True)),
                ('used', models.BooleanField(default=False)),
                ('question_answer', models.TextField(max_length=1000)),
                ('answer_image', models.ImageField(null=True, upload_to=b'imgas/answers', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='team_answered',
            field=models.ForeignKey(blank=True, to='main.Team', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='topic_name',
            field=models.ForeignKey(to='main.Topic'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('topic_name', 'score')]),
        ),
    ]
