# Generated by Django 3.1.1 on 2020-09-30 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_auto_20200930_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.CharField(default='', max_length=100, verbose_name='Email Id'),
            preserve_default=False,
        ),
    ]