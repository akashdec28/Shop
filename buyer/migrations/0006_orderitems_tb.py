# Generated by Django 2.2.3 on 2023-04-06 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_product_tb'),
        ('buyer', '0005_order_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderitems_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalprice', models.CharField(max_length=30)),
                ('quantity', models.CharField(max_length=30)),
                ('buyerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyer_tb')),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.order_tb')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product_tb')),
            ],
        ),
    ]
