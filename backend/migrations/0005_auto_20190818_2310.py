# Generated by Django 2.2.4 on 2019-08-18 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20190818_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general_details',
            name='latitude',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='general_details',
            name='longitude',
            field=models.CharField(max_length=100),
        ),
    ]
