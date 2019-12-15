# Generated by Django 2.2.6 on 2019-12-15 15:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191215_1653'),
        ('shopping_cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='products.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 12, 15, 15, 53, 16, 292749, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
