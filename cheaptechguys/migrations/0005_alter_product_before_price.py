# Generated by Django 3.2.3 on 2022-02-25 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheaptechguys', '0004_auto_20220225_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Before_price',
            field=models.CharField(max_length=200),
        ),
    ]
