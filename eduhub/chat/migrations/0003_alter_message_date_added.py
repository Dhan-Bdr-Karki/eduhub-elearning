# Generated by Django 4.1.3 on 2022-12-10 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_added',
            field=models.DateTimeField(default='2022-12-10T04:31:03.978450+00:00'),
        ),
    ]
