# Generated by Django 3.2.4 on 2021-06-24 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_clientaccounts_hiredadusername'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientaccounts',
            name='confirmedAds',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
