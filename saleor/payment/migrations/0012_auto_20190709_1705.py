# Generated by Django 2.2.3 on 2019-07-09 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0011_auto_20190516_0901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='billing_address_1',
            new_name='address_1',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='billing_address_2',
            new_name='address_2',
        ),
    ]