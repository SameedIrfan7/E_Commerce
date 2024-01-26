# Generated by Django 5.0 on 2024-01-03 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0002_cart'),
        ('seller', '0004_categorytable_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(unique=True)),
                ('status', models.CharField(choices=[('Order Placed', 'Order Placed'), ('Order Shipped', 'Order Shipped'), ('In Transit', 'In Transit'), ('Delivered', 'Delivered')], max_length=255)),
                ('payment_id', models.CharField(max_length=255)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product')),
            ],
        ),
    ]
