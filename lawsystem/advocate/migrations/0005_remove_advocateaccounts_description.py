# Generated by Django 3.2.4 on 2021-06-18 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advocate', '0004_auto_20210618_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advocateaccounts',
            name='description',
        ),
    ]