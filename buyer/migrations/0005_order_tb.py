# Generated by Django 2.2.3 on 2023-04-06 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0004_auto_20230331_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shippingaddress', models.CharField(max_length=30)),
                ('phonenumber', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('status', models.CharField(default='pending', max_length=30)),
                ('buyerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyer_tb')),
            ],
        ),
    ]
