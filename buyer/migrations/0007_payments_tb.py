# Generated by Django 4.2 on 2023-05-05 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0006_orderitems_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='payments_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.CharField(max_length=30)),
                ('cardname', models.CharField(max_length=30)),
                ('cvd', models.CharField(max_length=30)),
                ('expirydate', models.CharField(max_length=30)),
                ('buyerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyer_tb')),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.order_tb')),
            ],
        ),
    ]
