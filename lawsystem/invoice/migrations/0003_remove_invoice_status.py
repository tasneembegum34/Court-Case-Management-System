# Generated by Django 3.2.4 on 2021-06-30 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_alter_lineitem_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='status',
        ),
    ]