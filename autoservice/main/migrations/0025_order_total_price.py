# Generated by Django 4.2.13 on 2024-05-31 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_order_orderitem_order_products_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
