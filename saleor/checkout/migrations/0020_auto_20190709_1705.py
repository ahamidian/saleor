# Generated by Django 2.2.3 on 2019-07-09 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0019_checkout_gift_cards'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='billing_address',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='shipping_address',
        ),
    ]
