# Generated by Django 5.2.dev20240930195228 on 2024-10-23 23:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
        ('user_profile', '0006_alter_order_item_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.order'),
        ),
    ]
