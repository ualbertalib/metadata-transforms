# Generated by Django 2.1 on 2018-08-30 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0005_remove_document_file_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file_format',
            field=models.CharField(choices=[('mrc', 'marc'), ('bib', 'bibframe')], default='mrc', max_length=2),
        ),
    ]
