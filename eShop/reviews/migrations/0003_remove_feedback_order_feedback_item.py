# Generated by Django 5.2.dev20240930195228 on 2024-10-24 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_feedback_order'),
        ('store', '0006_item_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='order',
        ),
        migrations.AddField(
            model_name='feedback',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.item'),
        ),
    ]