# Generated by Django 3.1.1 on 2020-09-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0008_orderupdates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdates',
            name='update_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
