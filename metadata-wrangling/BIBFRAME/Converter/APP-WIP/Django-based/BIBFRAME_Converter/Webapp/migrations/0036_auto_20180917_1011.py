# Generated by Django 2.1 on 2018-09-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0035_auto_20180917_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processing',
            name='apis',
            field=models.CharField(blank=True, max_length=999),
        ),
    ]
