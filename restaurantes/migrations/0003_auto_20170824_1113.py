# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('restaurantes', '0002_auto_20170824_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasePlate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sopa', models.CharField(max_length=150)),
                ('segundo', models.CharField(max_length=150)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_restaurantes.baseplate_set+', to='contenttypes.ContentType')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantes.Restaurant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='executiveplate',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='executiveplate',
            name='id',
        ),
        migrations.RemoveField(
            model_name='executiveplate',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='executiveplate',
            name='segundo',
        ),
        migrations.RemoveField(
            model_name='executiveplate',
            name='sopa',
        ),
        migrations.RemoveField(
            model_name='executiveplate',
            name='updated_on',
        ),
        migrations.RemoveField(
            model_name='studentsplate',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='studentsplate',
            name='id',
        ),
        migrations.RemoveField(
            model_name='studentsplate',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='studentsplate',
            name='segundo',
        ),
        migrations.RemoveField(
            model_name='studentsplate',
            name='sopa',
        ),
        migrations.RemoveField(
            model_name='studentsplate',
            name='updated_on',
        ),
        migrations.AddField(
            model_name='executiveplate',
            name='baseplate_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='restaurantes.BasePlate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentsplate',
            name='baseplate_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='restaurantes.BasePlate'),
            preserve_default=False,
        ),
    ]
