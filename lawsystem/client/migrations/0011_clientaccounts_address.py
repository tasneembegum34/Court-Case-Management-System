# Generated by Django 3.2.4 on 2021-06-30 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_auto_20210628_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientaccounts',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]