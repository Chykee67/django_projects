# Generated by Django 5.2.dev20240903141902 on 2024-09-22 16:45

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('level', models.PositiveIntegerField(choices=[(1, 'ground floor'), (2, 'first floor'), (3, 'second floor'), (4, 'third floor')], help_text='Please enter a positive integer value for the storey level of this floor', primary_key=True, serialize=False)),
            ],
            managers=[
                ('floors', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('description', models.CharField(help_text='Item tags', max_length=15, primary_key=True, serialize=False, verbose_name='tag')),
            ],
            managers=[
                ('tags', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('description', models.CharField(help_text='Title of mall section', max_length=100, primary_key=True, serialize=False, verbose_name='Section')),
                ('trend', models.IntegerField(default=0)),
                ('floor', models.ForeignKey(help_text='Floor where section can be found', on_delete=django.db.models.deletion.CASCADE, to='store.floor')),
            ],
            managers=[
                ('sections', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Aisle',
            fields=[
                ('id', models.CharField(help_text="Aisle's unique ID", max_length=5, primary_key=True, serialize=False, verbose_name='Aisle ID')),
                ('section', models.ForeignKey(help_text='Mall section where rack is found', on_delete=django.db.models.deletion.CASCADE, to='store.section')),
            ],
            managers=[
                ('aisles', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('description', models.CharField(default='item', help_text='Title of item for sale', max_length=100, primary_key=True, serialize=False, verbose_name='Item title')),
                ('price', models.PositiveIntegerField(default=0, help_text='Price of item in Naira', verbose_name='Selling price')),
                ('cost', models.PositiveIntegerField(default=0, help_text='Cost of Item in Naira', verbose_name='Cost price')),
                ('trend', models.IntegerField(default=0)),
                ('aisle', models.ForeignKey(default='AA000', help_text='Aisle where item is displayed', on_delete=django.db.models.deletion.CASCADE, to='store.aisle')),
                ('section', models.ForeignKey(default='section', help_text='Mall Section', on_delete=django.db.models.deletion.CASCADE, to='store.section')),
                ('tags', models.ManyToManyField(to='store.tag')),
            ],
            managers=[
                ('items', django.db.models.manager.Manager()),
            ],
        ),
    ]
