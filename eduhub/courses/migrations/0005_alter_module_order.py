# Generated by Django 4.1.3 on 2022-11-28 11:55

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_module_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='order',
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]